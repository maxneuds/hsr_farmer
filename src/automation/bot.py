import asyncio as aio
import cv2 as cv
import numpy as np
import sys
from logger import logger
from datetime import datetime as dt, timedelta
import time
from skimage.metrics import structural_similarity as compare_ssim

class PathError(Exception): pass

class Bot:
    def __init__(self, adb, dev, xy, character_speed=1):
        self.adb = adb
        self.dev = dev
        self.xy = xy
        self.character_speed = character_speed

    async def sleep(self, duration):
        logger.info(f'sleep for {duration} seconds...')
        await aio.sleep(duration)

    async def action_tap(self, x, y):
        logger.info(f'action: tap {x},{y}')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {x} {y}')
        await aio.sleep(0.1)

    async def sprint_on(self):
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.sprint[0]} {self.xy.sprint[1]}')

    async def move(self, direction, duration):
        logger.info(f'move {direction} for {duration/1000} seconds')
        if direction not in self.xy.vjoy:
            logger.error('bad direction')
        else:
            cmd = f'input swipe {self.xy.vjoy[direction][0]} {self.xy.vjoy[direction][1]} {self.xy.vjoy[direction][0]} {self.xy.vjoy[direction][1]} {duration}'
            await self.dev.shell(cmd)

    async def movepi(self, direction, duration):
        logger.info(f'move {direction} pi for {duration/1000} seconds')
        x = self.xy.vjoy['center'][0] + self.xy.vjoy['r'] * np.cos(direction*np.pi)
        y = self.xy.vjoy['center'][1] - self.xy.vjoy['r'] * np.sin(direction*np.pi)
        cmd = f'input swipe {x} {y} {x} {y} {int(duration*self.character_speed)}'
        await self.dev.shell(cmd)

    async def open_map(self, penacony=False):
        logger.info('open map')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.map[0]} {self.xy.map[1]}')
        await aio.sleep(2.5)
        if penacony == True:
            await self.dev.shell(f'input tap {int(self.xy.width*2135/2400)} {int(self.xy.height*138/1080)}')
            await aio.sleep(2.5)
        await self.check_map_zoom_level(penacony=penacony) # in case of map already open, already done by the previous instance
        
    async def check_map_zoom_level(self, penacony=False):
        logger.info('check map zoom level')
        screen = await self.adb.get_screen(dev=self.dev, custom_msg=None)
        # img_zoombar_min = cv.imread('res/zoombar_min_penacony.png', cv.IMREAD_COLOR)
        # screen_zoombar = screen[int(self.xy.height*980/1080):int(self.xy.height*1000/1080), int(self.xy.width*1054/2400):int(self.xy.width*1078/2400)]
        img_zoombar_min = cv.imread('res/zoombar_min.png', cv.IMREAD_COLOR)
        screen_zoombar = screen[int(self.xy.height*965/1080):int(self.xy.height*1015/1080), int(self.xy.width*780/2400):int(self.xy.width*1250/2400)]
        matches = cv.matchTemplate(screen_zoombar, img_zoombar_min, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(matches)
        if max_val < 0.95: # map isn't on min zoom, change zoom level
            logger.info('zoom map to min')
            for _ in range(20):
                # await self.dev.shell(f'input tap {self.xy.width*1000/2400} {self.xy.height*990/1080}') # penacony
                await self.dev.shell(f'input tap {self.xy.width*783/2400} {self.xy.height*993/1080}')
                await aio.sleep(0.075)
            await aio.sleep(0.1)
            logger.info('re-open map')
            await self.dev.shell(f'input keyevent 4')
            await self.sleep(2.5)
            await self.open_map(penacony=penacony)

    async def use_teleporter(self, x, y, move_x=0, move_y=0, move_spd=500, corner='botright', open_map=True, penacony=False, confirm=False, debug=False):
        logger.info(f'use teleporter: {int(self.xy.width*x)},{int(self.xy.height*y)}')
        # open map
        if open_map:
            if penacony:
                await self.open_map(penacony=True)
            else:
                await self.open_map()
        logger.info(f'reset map to corner [default: botright]')
        for _ in range(3):
            if corner == 'topright':
                cmd = f'input swipe {int(self.xy.width*0.6)} {int(self.xy.height*0.1)} {int(self.xy.width*(0))} {int(self.xy.height*(0.9))} {500}'
            elif corner == 'botleft':
                cmd = f'input swipe {int(self.xy.width*0.1)} {int(self.xy.height*0.8)} {int(self.xy.width*(0.7))} {int(self.xy.height*(0))} {500}'
            else:
                cmd = f'input swipe {int(self.xy.width*0.6)} {int(self.xy.height*0.8)} {int(self.xy.width*(0))} {int(self.xy.height*(0))} {500}'
            await self.dev.shell(cmd)
            await aio.sleep(1)
        await aio.sleep(1)
        if move_x != 0 or move_y != 0:
            logger.info(f'move map by {move_x},{move_y}')
            if corner == 'topright':
                cmd = f'input swipe {int(self.xy.width*0.3)} {int(self.xy.height*0.9)} {int(self.xy.width*(0.3+0.65*(move_x/10)))} {int(self.xy.height*(0.9-0.85*(move_y/10)))} {move_spd}'
            elif corner == 'botleft':
                cmd = f'input swipe {int(self.xy.width*0.65)} {int(self.xy.height*0.1)} {int(self.xy.width*(0.65-0.6*(move_x/10)))} {int(self.xy.height*(0.1+0.85*(move_y/10)))} {move_spd}'
            else:
                cmd = f'input swipe {int(self.xy.width*0.3)} {int(self.xy.height*0.1)} {int(self.xy.width*(0.3+0.65*(move_x/10)))} {int(self.xy.height*(0.1+0.85*(move_y/10)))} {move_spd}'
            await self.dev.shell(cmd)
            await aio.sleep(2)
        # debug: send screenshot
        if debug:
            await self.adb.get_screen(dev=self.dev, debug=True)
            sys.exit()
        # tap teleporter
        logger.info(f'tap teleporter: {int(self.xy.width*x)},{int(self.xy.height*y)}')
        await self.dev.shell(f'input tap {int(self.xy.width*x)} {int(self.xy.height*y)}')
        await aio.sleep(1.25)
        # confirm teleporter if other landmark is close
        if confirm == True:
            await self.dev.shell(f'input tap {int(self.xy.width*1200/2400)} {int(self.xy.height*700/1080)}')
            await aio.sleep(1.5)
        # teleport
        await self.dev.shell(f'input tap {int(self.xy.width*0.83)} {int(self.xy.height*0.9)}')
        check = await self.wait_for_onmap(min_duration=1, no_fight=True)
        if check == 'stuck': # retry
            logger.error(f'telport failed. Try again')
            await self.dev.shell(f'input keyevent 4')
            await self.wait_for_onmap(min_duration=1, no_fight=True)
            # retry
            await self.use_teleporter(x, y, move_x=move_x, move_y=move_y, move_spd=move_spd, corner=corner, open_map=open_map, confirm=confirm, penacony=penacony, debug=False)

    async def switch_map(self, y_percentage, scroll_down=False, open_map=True, debug=False):
        logger.info('switch map')
        if open_map:
            await self.open_map()
        x = int(self.xy.width*0.8)
        if scroll_down:
            y1 = int(self.xy.height*0.8)
            y2 = int(self.xy.height*0.2)
        else:
            y1 = int(self.xy.height*0.3)
            y2 = int(self.xy.height*0.8)
        cmd = f'input swipe {x} {y1} {x} {y2} 250'
        await self.dev.shell(cmd)
        await aio.sleep(3)
        if debug:
            await self.adb.get_screen(dev=self.dev, debug=True)
            sys.exit()
        await self.action_tap(int(self.xy.width*0.8), int(self.xy.height*y_percentage))
        await aio.sleep(2)

    async def swipe_locations_up(self):
        logger.info('swipe locations up')
        await aio.sleep(0.1)
        cmd = f'input swipe {int(self.xy.width*0.8)} {self.xy.height-200} {int(self.xy.width*0.8)} {self.xy.height-700} 150'
        await self.dev.shell(cmd)
        await aio.sleep(1.5)

    async def open_star_rail_map(self):
        await self.open_map()
        logger.info('open star rail map')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.star_rail_map[0]} {self.xy.star_rail_map[1]}')
        await aio.sleep(1.5)

    async def switch_world(self, world):
        logger.info('###')
        # select correct matching template
        if world == 'herta_space_station':
            logger.info('### Herta Space Station ###')
            target = cv.imread('res/herta_space_station.png', cv.IMREAD_COLOR)
        if world == 'jarilo_vi':
            logger.info('### Jarilo-VI ###')
            target = cv.imread('res/jarilo-vi.png', cv.IMREAD_COLOR)
        if world == 'the_xianzhou_luofu':
            logger.info('### The Xianzhou Luofu ###')
            target = cv.imread('res/the_xianzhou_luofu.png', cv.IMREAD_COLOR)
        if world == 'penacony':
            logger.info('### Penacony ###')
            target = cv.imread('res/penacony.png', cv.IMREAD_COLOR)
        logger.info('###')
        # open star rail map
        await self.open_star_rail_map()
        # get screenshot
        screen = await self.adb.get_screen(dev=self.dev)
        # find match
        result = cv.matchTemplate(screen, target, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # Get the top-left corner coordinates of the matched region
        top_left = max_loc
        # Get the dimensions of the template image
        h, w, _ = target.shape
        # tap planet
        await self.dev.shell(f'input swipe {top_left[0] + int(w/2)} {top_left[1] + int(h/2)} {top_left[0] + int(w/2)} {top_left[1] + int(h/2)} 200')
        await aio.sleep(2)
    
    async def restore_tp(self, n=1):
        logger.info('action: restore TP using food, make sure it is faved first')
        await aio.sleep(0.05)
        logger.info('open inventory')
        await self.dev.shell(f'input tap {self.xy.inventory[0]} {self.xy.inventory[1]}')
        await aio.sleep(2)
        logger.info('open food menu')
        await self.dev.shell(f'input tap {self.xy.food_menu[0]} {self.xy.food_menu[1]}')
        await aio.sleep(1)
        logger.info('select fav food')
        await self.dev.shell(f'input tap {self.xy.food_fav[0]} {self.xy.food_fav[1]}')
        await aio.sleep(0.5)
        logger.info(f'eat food {n} times')
        for _ in range(n):
            await self.action_tap(int(self.xy.width*2008/2400), int(self.xy.height*990/1080))
            await aio.sleep(1)
            await self.action_tap(int(self.xy.width*1461/2400), int(self.xy.height*824/1080))
            await aio.sleep(2)
        logger.info(f'exit to map')
        await self.dev.shell(f'input keyevent 4')
        await self.wait_for_onmap(min_duration=2)

    async def interact(self):
        await aio.sleep(1)
        await self.action_tap(int(self.xy.width*1600/2400), int(self.xy.height*650/1080))
        await self.wait_for_onmap(min_duration=2)

    async def action_button(self):
        await aio.sleep(1)
        await self.action_tap(int(self.xy.width*1580/2400), int(self.xy.height*933/1080))
        await self.wait_for_onmap(min_duration=2)
    
    async def attack(self):
        logger.info('action: attack')
        await aio.sleep(0.05)
        await self.dev.shell(f'input tap {self.xy.attack[0]} {self.xy.attack[1]}')
        await aio.sleep(0.5)

    async def action_technique(self):
        logger.info('action: technique')
        await aio.sleep(0.05)
        await self.dev.shell(f'input tap {self.xy.technique[0]} {self.xy.technique[1]}')
        await aio.sleep(0.3)

    async def attack_technique(self, count=2):
        logger.info(f'action: attack with technique {count} times')
        for _ in range(count):
            await self.action_technique()
        check = await self.wait_for_onmap(min_duration=3)
        if check == 'food':
            # had to eat food, repeat
            await self.attack_technique(count=count)

    async def wait_for_onmap(self, min_duration=5, no_fight=False, debug=False):
        logger.info('wait/check for character on map')
        if not debug:
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
                if no_fight == True and (time_running.seconds > 10):
                    logger.debug('character stuck returning to map')
                    return('stuck')
                elif time_running.seconds > 300:
                    logger.debug('character stuck returning to map')
                    return('stuck')
                success = False
                while not success:
                    try:
                        if debug:
                            screen = await self.adb.get_screen(dev=self.dev, custom_msg='still in fight')
                        else:
                            screen = await self.adb.get_screen(dev=self.dev, custom_msg=None)
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
                    await self.dev.shell(f'input keyevent 4')
                    await self.sleep(0.5)
                elif max_val_food > 0.95: # food menu found, eat TP food
                    logger.info('food menu found: eat TP food')
                    top_left = max_loc_food
                    await self.action_tap(top_left[0]+5, top_left[1]+5)
                    await self.action_tap(int(self.xy.width*1470/2400), int(self.xy.height*885/1080))
                    await self.dev.shell(f'input keyevent 4')
                    for _ in range(4): # directly continue attacking
                        await self.action_technique()
                    return('food')
                elif check_return > 2: # back to map, continue
                    logger.info('character on map: continue')
                    await aio.sleep(0.5)
                    return(True)
        except KeyboardInterrupt:
            logger.debug('Ctrl+C detected. Exiting gracefully.')
            exit()