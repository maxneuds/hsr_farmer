import asyncio as aio
import cv2 as cv
import numpy as np
import sys
from logger import logger
from datetime import datetime as dt, timedelta
import time
from skimage.metrics import structural_similarity as compare_ssim
from automation.adb import ADB
from automation.xy import OnePlus7T


class PathError(Exception): pass

class Bot:
    def __init__(self, device):
        self.device = device
        # initialize bot
        self.xy = OnePlus7T()
        self.adb = ADB()
        self.dev = None

    async def shell_failsafe(self, cmd, n_try=0):
        try:
            if self.dev is None:
                self.dev = await self.adb.connect_dev(device=self.device)
            await self.dev.shell(cmd)
        except RuntimeError as e:
            if n_try < 9:
                logger.info(f"ADB connection closed: reconnect trial {n_try+1}")
                await aio.sleep(0.5)
                self.dev = await self.adb.connect_dev(device=self.device)
                await self.shell_failsafe(cmd, n_try=n_try+1)
            else:
                logger.error(f"Reconnecting to ADB failed with error:\n{e}")
    
    async def screen_failsafe(self, n_try=0):
        try:
            if self.dev is None:
                self.dev = await self.adb.connect_dev(device=self.device)
            im_byte_array = await self.dev.screencap()
            return(im_byte_array)
        except RuntimeError as e:
            if n_try < 9:
                logger.info(f"ADB connection closed: reconnect trial {n_try+1}")
                self.dev = await self.adb.connect_dev(device=self.device)
                await self.screen_failsafe(n_try=n_try+1)
            else:
                logger.error(f"Reconnecting to ADB failed with error:\n{e}")

    # unused
    # async def get_screensize(self, dev):
    #     result = await dev.shell('wm size')
    #     hxw = result.strip().split()[2]
    #     h, w = hxw.split('x')
    #     return(int(h), int(w))
    
    def click_event(self, event, x, y, flags, params):
        # function to display the coordinates of
        # of the points clicked on the image
        # checking for left mouse clicks
        if event == cv.EVENT_LBUTTONDOWN:
            logger.debug(f'{x},{y}')
    
    async def get_screen(self, custom_msg=False, debug=False):
        if custom_msg == False:
            logger.info('get screenshot from device')
        elif custom_msg == None:
            pass
        else:
            logger.info(custom_msg)
        # get screen from device
        im_byte_array = await self.screen_failsafe()
        # convert to cv image
        screenshot = cv.imdecode(np.frombuffer(bytes(im_byte_array), np.uint8), cv.IMREAD_COLOR)
        if debug == True:
            cv.imshow('debug', screenshot)
            cv.imwrite('debug.png', screenshot)
            cv.setMouseCallback('debug', self.click_event)
            cv.waitKey(0)
            cv.destroyAllWindows()
        return(screenshot)

    async def sleep(self, duration):
        logger.info(f'sleep for {duration} seconds...')
        await aio.sleep(duration)
    
    async def action_back(self, n=1):
        logger.info('send back button')
        for _ in range(n):
            await self.shell_failsafe(f'input keyevent 4')
            await aio.sleep(1.5)

    async def action_tap(self, x, y):
        logger.info(f'action: tap {x},{y}')
        await aio.sleep(0.1)
        await self.shell_failsafe(f'input tap {x} {y}')
        await aio.sleep(0.1)

    async def sprint_on(self):
        await aio.sleep(0.1)
        await self.shell_failsafe(f'input tap {self.xy.sprint[0]} {self.xy.sprint[1]}')

    async def posfix(self, direction, duration):
        logger.info(f'position fixing: move {direction} pi for {duration/1000} seconds')
        await self.movepi(direction=direction, duration=duration)
        await self.sleep(0.5)

    async def movepi(self, direction, duration):
        logger.info(f'move {direction} pi for {duration/1000} seconds')
        x = self.xy.vjoy['center'][0] + self.xy.vjoy['r'] * np.cos(direction*np.pi)
        y = self.xy.vjoy['center'][1] - self.xy.vjoy['r'] * np.sin(direction*np.pi)
        cmd = f'input swipe {x} {y} {x} {y} {int(duration)}'
        await self.shell_failsafe(cmd)

    async def open_map(self, special_exit=True, debug=False):
        if not debug: # open map for debugging
            await self.wait_for_onmap(min_duration=0)
            logger.info('open map')
            await self.attack() # animation cancle
            await self.shell_failsafe(f'input tap {self.xy.map[0]} {self.xy.map[1]}')
        # wait for map
        logger.info('wait for map')
        im_mapx = cv.imread('res/map_x_bw.png', cv.IMREAD_GRAYSCALE)
        check_map = True
        check_map_iter = 1
        while check_map:
            screen = await self.get_screen()
            screen_topright = screen[0:int(self.xy.height*0.2), int(self.xy.width*0.7):int(self.xy.width)]
            screen_topright_bw = cv.cvtColor(screen_topright, cv.COLOR_BGR2GRAY)
            _, screen_topright_bw = cv.threshold(screen_topright_bw, 240, 255, cv.THRESH_BINARY)
            if debug == True:
                cv.imwrite('debug.png', screen_topright)
                cv.imshow('debug', screen_topright)
                cv.waitKey(0)
                cv.destroyAllWindows()
                exit()
            result = cv.matchTemplate(screen_topright_bw, im_mapx, cv.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv.minMaxLoc(result)
            if max_val > 0.95:
                logger.info('map detected')
            else:
                logger.info(f'iteration {check_map_iter}, map not detected: retry')
                check_map_iter += 1
                if check_map_iter > 10:
                    logger.error('map not found: retry')
                    check_map = False
                    await self.action_back()
                    await self.wait_for_onmap(min_duration=0)
                    check = await self.open_map(special_exit=special_exit)
                    return(check)
                else:
                    await aio.sleep(0.5)
                    continue
            # check map type
            logger.info('check map type')
            im_tbp = cv.imread('res/map_tbp.png', cv.IMREAD_COLOR)
            result = cv.matchTemplate(screen_topright, im_tbp, cv.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv.minMaxLoc(result)
            if max_val > 0.95:
                logger.info('map type: normal')
            else:
                logger.info('map type: special')
                if special_exit:
                    logger.info('exit special map to normal map')
                    await self.shell_failsafe(f'input tap {int(self.xy.width*2135/2400)} {int(self.xy.height*138/1080)}')
                    await aio.sleep(1)
                    continue
            check_map = False
            await self.check_map_zoom_level()
            return(True)
        
    async def check_map_zoom_level(self, debug=False):
        logger.info('check map zoom level')
        im_zoombar_min = cv.imread('res/map_zoombar_min.png', cv.IMREAD_GRAYSCALE)
        im_zoom_minus_bw = cv.imread('res/map_zoom_minus_bw.png', cv.IMREAD_GRAYSCALE)
        screen = await self.get_screen()
        screen_botmid = screen[int(self.xy.height*0.8):int(self.xy.height), int(self.xy.width*0.3):int(self.xy.width*0.7)]
        screen_botmid_bw = cv.cvtColor(screen_botmid, cv.COLOR_BGR2GRAY)
        _, screen_botmid_bw = cv.threshold(screen_botmid_bw, 240, 255, cv.THRESH_BINARY)
        if debug == True:
            cv.imwrite('debug.png', screen_zoombar)
            cv.imshow('debug', screen_zoombar)
            cv.waitKey(0)
            cv.destroyAllWindows()
            exit()
        # locate min zoom button
        logger.info('locate min zoom button')
        matches = cv.matchTemplate(screen_botmid_bw, im_zoom_minus_bw, cv.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv.minMaxLoc(matches)
        btn_zoom_minus = (max_loc[0]+int(self.xy.width*0.3), max_loc[1]+int(self.xy.height*0.8))
        # check zoom level
        logger.info('check zoom level')
        screen_zoombar = screen_botmid_bw[max_loc[1]-8:max_loc[1]+32, max_loc[0]:max_loc[0]+96]
        matches = cv.matchTemplate(screen_botmid_bw, im_zoombar_min, cv.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv.minMaxLoc(matches)
        if max_val < 0.95: # map isn't on min zoom, change zoom level
            logger.info('zoom map to min')
            for _ in range(20):
                await self.shell_failsafe(f'input tap {btn_zoom_minus[0]} {btn_zoom_minus[1]}')
                await aio.sleep(0.05)
            await aio.sleep(0.1)

    async def use_teleporter(self, x, y, move_x=0, move_y=0, swipe=1, move_spd=500, corner='botright', open_map=True, confirm=False, special_exit=True, switch_world=False, n_try=0, debug=False):
        logger.info(f'use teleporter: {int(self.xy.width*x)},{int(self.xy.height*y)}')
        if open_map == True:
            await self.open_map(special_exit=special_exit)
        logger.info(f'move map to corner: {corner}')
        for _ in range(2+swipe):
            if corner == 'topright':
                cmd = f'input swipe {int(self.xy.width*0.6)} {int(self.xy.height*0.1)} {int(self.xy.width*(0))} {int(self.xy.height*(0.9))} {500}'
            elif corner == 'topleft':
                cmd = f'input swipe {int(self.xy.width*0.1)} {int(self.xy.height*0.25)} {int(self.xy.width*(0.7))} {int(self.xy.height*(0.9))} {500}'
            elif corner == 'botleft':
                cmd = f'input swipe {int(self.xy.width*0.1)} {int(self.xy.height*0.8)} {int(self.xy.width*(0.7))} {int(self.xy.height*(0))} {500}'
            elif corner == f'botright':
                cmd = f'input swipe {int(self.xy.width*0.6)} {int(self.xy.height*0.8)} {int(self.xy.width*(0))} {int(self.xy.height*(0))} {500}'
            else:
                logger.debug('bad corner given')
                exit()
            await self.shell_failsafe(cmd)
            await aio.sleep(1)
        await aio.sleep(1)
        if move_x != 0 or move_y != 0:
            logger.info(f'move map by {move_x},{move_y}: {swipe}x')
            for _ in range(swipe):
                if corner == 'topright':
                    cmd = f'input swipe {int(self.xy.width*0.3)} {int(self.xy.height*0.9)} {int(self.xy.width*(0.3+0.65*(move_x/10)))} {int(self.xy.height*(0.9-0.85*(move_y/10)))} {move_spd}'
                if corner == 'topleft':
                    cmd = f'input swipe {int(self.xy.width*0.65)} {int(self.xy.height*0.9)} {int(self.xy.width*(0.65-0.6*(move_x/10)))} {int(self.xy.height*(0.9-0.85*(move_y/10)))} {move_spd}'
                elif corner == 'botleft':
                    cmd = f'input swipe {int(self.xy.width*0.65)} {int(self.xy.height*0.1)} {int(self.xy.width*(0.65-0.6*(move_x/10)))} {int(self.xy.height*(0.1+0.85*(move_y/10)))} {move_spd}'
                elif corner == f'botright':
                    cmd = f'input swipe {int(self.xy.width*0.3)} {int(self.xy.height*0.1)} {int(self.xy.width*(0.3+0.65*(move_x/10)))} {int(self.xy.height*(0.1+0.85*(move_y/10)))} {move_spd}'
                await self.shell_failsafe(cmd)
                await aio.sleep(2)
        # debug: send screenshot
        if debug:
            await self.get_screen(debug=True)
            sys.exit()
        # tap teleporter
        logger.info(f'tap teleporter: {int(self.xy.width*x)},{int(self.xy.height*y)}')
        await self.shell_failsafe(f'input tap {int(self.xy.width*x)} {int(self.xy.height*y)}')
        await aio.sleep(1.25)
        # confirm teleporter if other landmark is close
        if confirm == True:
            logger.info(f'confirm teleporter selection')
            await self.shell_failsafe(f'input tap {int(self.xy.width*1200/2400)} {int(self.xy.height*700/1080)}')
            await aio.sleep(1.5)
        # teleport
        await self.shell_failsafe(f'input tap {int(self.xy.width*0.83)} {int(self.xy.height*0.9)}')
        check = await self.wait_for_onmap(min_duration=2, reason='teleport')
        if check != True: # retry
            n_try += 1
            if n_try > 10: # retry at most 10 times
                logger.error(f"Failed to teleport {n_try} times. Please fix!")
                sys.exit()
            logger.debug(f'telport failed. Try again [{n_try}]')
            await self.action_back(n=2)
            await self.wait_for_onmap(min_duration=0, reason='teleport')
            if open_map == True:
                await self.use_teleporter(x, y, move_x=move_x, move_y=move_y, swipe=swipe, move_spd=move_spd, corner=corner, open_map=open_map, confirm=confirm, special_exit=special_exit, switch_world=switch_world, n_try=n_try, debug=False)
            else:
                logger.error(f"Failed to teleport. Return False.")
                return(False)
        else:
            return(True)

    async def swipe_locations_up(self):
        logger.info('swipe locations up')
        await aio.sleep(0.1)
        cmd = f'input swipe {int(self.xy.width*0.8)} {self.xy.height-200} {int(self.xy.width*0.8)} {self.xy.height-700} 150'
        await self.shell_failsafe(cmd)
        await aio.sleep(1.5)

    async def open_star_rail_map(self):
        await self.open_map()
        logger.info('open star rail map')
        await aio.sleep(0.1)
        await self.shell_failsafe(f'input tap {self.xy.star_rail_map[0]} {self.xy.star_rail_map[1]}')
        await aio.sleep(1.5)

    async def switch_world(self, world):
        # select correct matching template
        if world == 'herta_space_station':
            logger.info('switch world: Herta Space Station')
            target = cv.imread('res/herta_space_station.png', cv.IMREAD_COLOR)
        elif world == 'jarilo_vi':
            logger.info('switch world: Jarilo-VI')
            target = cv.imread('res/jarilo-vi.png', cv.IMREAD_COLOR)
        elif world == 'the_xianzhou_luofu':
            logger.info('switch world: The Xianzhou Luofu')
            target = cv.imread('res/the_xianzhou_luofu.png', cv.IMREAD_COLOR)
        elif world == 'penacony':
            logger.info('switch world: Penacony')
            target = cv.imread('res/penacony.png', cv.IMREAD_COLOR)
        else:
            logger.debug('Error: no world selected')
            exit()
        # open star rail map
        await self.open_star_rail_map()
        # get screenshot
        screen = await self.get_screen()
        # find match
        result = cv.matchTemplate(screen, target, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # Get the top-left corner coordinates of the matched region
        top_left = max_loc
        # Get the dimensions of the template image
        h, w, _ = target.shape
        # tap planet
        await self.shell_failsafe(f'input swipe {top_left[0] + int(w/2)} {top_left[1] + int(h/2)} {top_left[0] + int(w/2)} {top_left[1] + int(h/2)} 200')
        await aio.sleep(2)
    
    async def switch_map(self, y_list, world, x, y, scroll_down=False, corner='botright', move_x=0, move_y=0, confirm=False, debug=False):
        logger.info('switch map')
        await self.switch_world(world=world)
        logger.info('scroll location list')
        x_list = int(self.xy.width*0.732)
        if scroll_down:
            y1 = int(self.xy.height*0.8)
            y2 = int(self.xy.height*0.2)
        else:
            y1 = int(self.xy.height*0.3)
            y2 = int(self.xy.height*0.8)
        cmd = f'input swipe {x_list} {y1} {x_list} {y2} 250'
        await self.shell_failsafe(cmd)
        await aio.sleep(3)
        if debug:
            await self.get_screen(debug=debug)
        logger.info('tap location')
        await self.action_tap(x_list, int(self.xy.height*y_list))
        await aio.sleep(2)
        check = await self.use_teleporter(x, y, corner=corner, move_x=move_x, move_y=move_y, confirm=confirm, open_map=False, debug=debug)
        if check == False:
            logger.warning('map change failed: retry')
            await self.switch_map(y_list=y_list, world=world, x=x, y=y, scroll_down=scroll_down, corner=corner, move_x=move_x, move_y=move_y, confirm=confirm, debug=debug)
    
    async def restore_tp(self, item='trick_snack', n=1, n_try=0):
        logger.info('action: restore TP using food, make sure it is faved first')
        ready = False
        while not ready:
            ready = await self.wait_for_onmap(min_duration=0)
        await self.attack() # animation cancle
        logger.info('open inventory')
        await self.shell_failsafe(f'input tap {self.xy.inventory[0]} {self.xy.inventory[1]}')
        await aio.sleep(2)
        logger.info('open food menu')
        await self.shell_failsafe(f'input tap {self.xy.food_menu[0]} {self.xy.food_menu[1]}')
        await aio.sleep(2)
        logger.info('select fav food')
        # select item
        count = 0
        search_item = True
        while search_item == True:
            logger.info(f'looking for item: {item}')
            # get screen
            success = False
            while not success:
                try:
                    screen = await self.get_screen(custom_msg=None)
                    success = True
                except:
                    pass
            im_item = cv.imread(f'res/item_use_{item}.png', cv.IMREAD_COLOR)
            result_food = cv.matchTemplate(screen, im_item, cv.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv.minMaxLoc(result_food)
            im_item_selected = cv.imread(f'res/item_use_selected_{item}.png', cv.IMREAD_COLOR)
            result_food_selected = cv.matchTemplate(screen, im_item_selected, cv.TM_CCOEFF_NORMED)
            _, max_val_selected, _, max_loc_selected = cv.minMaxLoc(result_food_selected)
            if max_val_selected > max_val:
                max_val = max_val_selected
                max_loc = max_loc_selected
            if max_val > 0.90: # item found
                top_left = max_loc
                await self.action_tap(top_left[0]+10, top_left[1]+10)
                logger.info(f'eat food: {item} x {n}')
                for _ in range(n):
                    await self.action_tap(int(self.xy.width*2008/2400), int(self.xy.height*990/1080))
                    await aio.sleep(1)
                    await self.action_tap(int(self.xy.width*1461/2400), int(self.xy.height*824/1080))
                    await aio.sleep(2)
                logger.info(f'exit to map')
                await self.action_back(n=3)
                await self.wait_for_onmap(min_duration=0)
                search_item = False
                return(True)
            else:
                count += 1
                if count > 9:
                    logger.error(f'"{item}" not found. Maybe in fight. Retry {n_try+1}.')
                    if n_try < 2:
                        search_item = False
                        await self.restore_tp(item=item, n=n, n_try=n_try+1)
                    else:
                        search_item = False
                        logger.error(f'"{item}" not found. Exit.')
                        exit()

    async def interact(self, check_on_map=True):
        await aio.sleep(1)
        await self.action_tap(int(self.xy.width*1600/2400), int(self.xy.height*650/1080))
        if check_on_map == True:
            await self.wait_for_onmap(min_duration=2)
        else:
            await self.sleep(5)

    async def action_button(self):
        await aio.sleep(1)
        await self.action_tap(int(self.xy.width*1580/2400), int(self.xy.height*933/1080))
        await self.wait_for_onmap(min_duration=2)
    
    async def chat_initiate(self):
        logger.info(f'chat: initiate')
        await aio.sleep(0.2)
        await self.action_tap(int(self.xy.width*1458/2400), int(self.xy.height*640/1080))
        await aio.sleep(1)
    
    async def shop_exit(self):
        logger.info(f'shop: exit')
        await self.action_back()
        await self.wait_for_onmap(min_duration=0)
        
    async def chat_advance(self):
        logger.info(f'chat: advance')
        await self.action_tap(int(self.xy.width*1200/2400), int(self.xy.height*1000/1080))
        await aio.sleep(0.2)
        await self.action_tap(int(self.xy.width*1200/2400), int(self.xy.height*1000/1080))
        await aio.sleep(1)

    async def attack(self, count=1):
        logger.info('action: attack')
        await aio.sleep(0.05)
        for _ in range(count):
            await self.shell_failsafe(f'input tap {self.xy.attack[0]} {self.xy.attack[1]}')
            await aio.sleep(0.6)

    async def action_technique(self):
        logger.info('action: technique')
        await aio.sleep(0.05)
        await self.shell_failsafe(f'input tap {self.xy.technique[0]} {self.xy.technique[1]}')
        await aio.sleep(0.3)

    async def attack_technique(self, count=1):
        logger.info(f'action: attack with technique {count} times')
        for _ in range(count):
            await self.action_technique()
                
    async def buy_item(self, name, debug=False):
        logger.info(f'buy: {name}')
        try: # catch KeyboardInterrupt
            time_start = time.perf_counter()
            while True:
                # get screen
                success = False
                while not success:
                    try:
                        screen = await self.get_screen(custom_msg=None)
                        success = True
                        if debug == True:
                            cv.imwrite('debug.png', screen)
                            cv.imshow('debug', screen)
                            cv.waitKey(0)
                            cv.destroyAllWindows()
                            exit()
                    except:
                        pass
                # load match template
                im_item = cv.imread(f'res/item_{name}.png', cv.IMREAD_COLOR)
                result_food = cv.matchTemplate(screen, im_item, cv.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv.minMaxLoc(result_food)
                if max_val > 0.90:
                    top_left = max_loc
                    await self.action_tap(top_left[0]+10, top_left[1]+10)
                    await aio.sleep(2)
                    await self.action_tap(int(self.xy.width*1808/2400), int(self.xy.height*657/1080)) # buy all
                    await aio.sleep(2)
                    await self.action_tap(int(self.xy.width*1393/2400), int(self.xy.height*787/1080)) # confirm
                    await aio.sleep(2)
                    await self.action_back()
                    return(True)
                else:
                    time_running = timedelta(seconds=time.perf_counter() - time_start)
                    if time_running.seconds > 10:
                        logger.error(f'item: {name} not found')
                        exit()
        except KeyboardInterrupt:
            logger.debug('Ctrl+C detected. Exiting gracefully.')
            exit()
            
    async def open_phone(self):
        await self.action_tap(int(self.xy.phone[0]), int(self.xy.phone[1]))
        await aio.sleep(3)
            
    async def craft_item(self, name, all=True, debug=False):
        logger.info(f'craft: {name}')
        if debug == True:
            screen = await self.get_screen(debug=True)
        im_item = cv.imread(f'res/item_{name}.png', cv.IMREAD_COLOR)
        # open phone
        await self.open_phone()
        # tap "Synthesize"
        await self.action_tap(int(self.xy.width*1933/2400), int(self.xy.height*612/1080))
        await aio.sleep(3)
        # select items
        await self.action_tap(int(self.xy.width*152/2400), int(self.xy.height*178/1080))
        await aio.sleep(2)
        # select recipe
        count = 0
        search_recipe = True
        while search_recipe == True:
            logger.info(f'looking for recipe: {name}')
            # get screen
            success = False
            while not success:
                try:
                    screen = await self.get_screen(custom_msg=None)
                    success = True
                except:
                    pass
            im_item = cv.imread(f'res/item_{name}.png', cv.IMREAD_COLOR)
            result_food = cv.matchTemplate(screen, im_item, cv.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv.minMaxLoc(result_food)
            if max_val > 0.90: # recipe found
                top_left = max_loc
                await self.action_tap(top_left[0]+10, top_left[1]+10)
                await aio.sleep(2)
                if all == True:
                    await self.action_tap(int(self.xy.width*1863/2400), int(self.xy.height*869/1080)) # craft all
                else:
                    await self.action_tap(int(self.xy.width*1550/2400), int(self.xy.height*869/1080)) # craft half
                await aio.sleep(2)
                await self.action_tap(int(self.xy.width*1550/2400), int(self.xy.height*989/1080)) # Synthesize
                await aio.sleep(3)
                await self.action_tap(int(self.xy.width*1393/2400), int(self.xy.height*737/1080)) # confirm
                await aio.sleep(5)
                logger.info('return to map')
                for _ in range(3):
                    await self.action_back()
                search_recipe = False
                return(True)
            else:
                count += 1
                if count > 9:
                    logger.error('recipe not found')
                    search_recipe = False
                    exit()
                # swipe up
                x = int(self.xy.width*492/2400)
                cmd = f'input swipe {x} {int(self.xy.height*600/1080)} {x} {int(self.xy.height*300/1080)} {500}'
                await self.shell_failsafe(cmd)
                await aio.sleep(0.5)

    async def wait_for_onmap(self, min_duration=0, reason='default', debug=False):
        logger.info(f'wait/check for character on map. reason: {reason}')
        if not debug and min_duration > 0:
            logger.info(f'wait for {min_duration}s')
            await aio.sleep(min_duration)
        img_warp= cv.imread('res/bw_warp.png', cv.IMREAD_GRAYSCALE)
        img_party= cv.imread('res/bw_party.png', cv.IMREAD_GRAYSCALE)
        img_mission= cv.imread('res/bw_mission.png', cv.IMREAD_GRAYSCALE)
        img_chat = cv.imread('res/bw_chat.png', cv.IMREAD_GRAYSCALE)
        img_sprint = cv.imread('res/bw_sprint.png', cv.IMREAD_GRAYSCALE)
        img_tpfood = cv.imread('res/food_tp.png', cv.IMREAD_COLOR)
        img_exit = cv.imread('res/exit.png', cv.IMREAD_COLOR)
        check_return = 0
        time_start = time.perf_counter()
        try: # catch KeyboardInterrupt
            while True:
                time_running = timedelta(seconds=time.perf_counter() - time_start)
                if reason == 'default' and (time_running.seconds > 10):
                    logger.debug('character stuck returning to map. maybe in fight?')
                    reason = 'unknown'
                    continue
                elif reason == 'teleport' and (time_running.seconds > 7):
                    return(False)
                elif time_running.seconds > 300:
                    logger.debug('character stuck: send back button')
                    await self.action_back()
                success = False
                while not success:
                    try:
                        if debug:
                            screen = await self.get_screen(custom_msg='still in fight')
                        else:
                            screen = await self.get_screen(custom_msg=None)
                        screen_bw = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
                        # screen_edges = cv.Canny(screen, 400, 500)
                        _, screen_bw = cv.threshold(screen_bw, 200, 255, cv.THRESH_BINARY)
                        success = True
                    except:
                        pass
                screen_warp = screen_bw[int(self.xy.height*0.03):int(self.xy.height*0.08), int(self.xy.width*0.75):int(self.xy.width*0.773)]
                screen_party = screen_bw[int(self.xy.height*0.03):int(self.xy.height*0.08), int(self.xy.width*0.88):int(self.xy.width*0.9)]
                screen_mission = screen_bw[int(self.xy.height*0.248):int(self.xy.height*0.31), int(self.xy.width*0.04):int(self.xy.width*0.062)]
                screen_chat = screen_bw[int(self.xy.height*0.868):int(self.xy.height*0.925), int(self.xy.width*0.04):int(self.xy.width*0.068)]
                screen_sprint = screen_bw[int(self.xy.height*0.815):int(self.xy.height*0.885), int(self.xy.width*0.88):int(self.xy.width*0.915)]
                screen_exit = screen[int(self.xy.height*0.34):int(self.xy.height*0.66), int(self.xy.width*0.33):int(self.xy.width*0.67)]
                # debug = True
                if debug:
                    # sc = screen_exit
                    # si = img_mission
                    # print(si.shape)
                    # print(sc.shape)
                    # cv.imwrite('img.png', sc)
                    # ssi = compare_ssim(sc, si)
                    # print(ssi)
                    # cv.imshow('debug', sc)
                    # cv.waitKey(0)
                    # cv.destroyAllWindows()
                    exit()
                check_images = [
                    (screen_warp, img_warp),
                    (screen_party, img_party),
                    (screen_mission, img_mission),
                    (screen_chat, img_chat),
                    (screen_sprint, img_sprint)
                ]
                for i in check_images:
                    ssi = compare_ssim(i[0], i[1])
                    if ssi > 0.95:
                        check_return += 1
                # check for food window (not enough TP) and in case of 0 eat food
                result_food = cv.matchTemplate(screen, img_tpfood, cv.TM_CCOEFF_NORMED)
                _, max_val_food, _, max_loc_food = cv.minMaxLoc(result_food)
                # check for mistake (exit window)
                result_exit = cv.matchTemplate(screen_exit, img_exit, cv.TM_CCOEFF_NORMED)
                _, max_val_exit, _, _ = cv.minMaxLoc(result_exit)
                if max_val_exit > 0.95:
                    logger.info('exit window found: cancel')
                    await self.action_back()
                    return(True)
                elif max_val_food > 0.95: # food menu found, eat TP food
                    logger.info('food menu found: eat TP food')
                    await self.action_back()
                    await self.restore_tp(item='trick_snack')
                    return(True)
                elif check_return > 2: # back to map, continue
                    logger.info('character on map: continue')
                    await aio.sleep(0.5)
                    return(True)
        except KeyboardInterrupt:
            logger.debug('Ctrl+C detected. Exiting gracefully.')
            exit()