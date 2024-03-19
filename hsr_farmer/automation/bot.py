import asyncio as aio
import cv2 as cv
import numpy as np
import sys
from datetime import datetime as dt
from time import time
from skimage.metrics import structural_similarity as compare_ssim

def logger(msg):
    dt_now = dt.now().strftime('%H:%M:%S')
    print(f'[{dt_now}] {msg}')

class PathError(Exception): pass

class Bot:
    def __init__(self, adb, dev, xy, character_speed=1):
        self.adb = adb
        self.dev = dev
        self.xy = xy
        self.character_speed = character_speed

    async def sleep(self, duration):
        logger(f'sleep for {duration} seconds...')
        await aio.sleep(duration)

    async def action_tap(self, x, y):
        logger(f'action: tap {x},{y}')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {x} {y}')
        await aio.sleep(0.1)

    async def sprint_on(self):
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.sprint[0]} {self.xy.sprint[1]}')

    async def move(self, direction, duration):
        logger(f'move {direction} for {duration/1000} seconds')
        if direction not in self.xy.vjoy:
            logger('bad direction')
        else:
            cmd = f'input swipe {self.xy.vjoy[direction][0]} {self.xy.vjoy[direction][1]} {self.xy.vjoy[direction][0]} {self.xy.vjoy[direction][1]} {duration}'
            await self.dev.shell(cmd)

    async def movepi(self, direction, duration):
        logger(f'move {direction} pi for {duration/1000} seconds')
        x = self.xy.vjoy['center'][0] + self.xy.vjoy['r'] * np.cos(direction*np.pi)
        y = self.xy.vjoy['center'][1] - self.xy.vjoy['r'] * np.sin(direction*np.pi)
        cmd = f'input swipe {x} {y} {x} {y} {int(duration*self.character_speed)}'
        await self.dev.shell(cmd)

    async def open_map(self, penacony=False):
        logger('open map')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.map[0]} {self.xy.map[1]}')
        await aio.sleep(2.5)
        if penacony == True:
            await self.dev.shell(f'input tap {int(self.xy.width*2135/2400)} {int(self.xy.height*138/1080)}')
            await aio.sleep(2.5)
        await self.check_map_zoom_level(penacony=penacony) # in case of map already open, already done by the previous instance
        
    async def check_map_zoom_level(self, penacony=False):
        logger('check map zoom level')
        screen = await self.adb.get_screen(dev=self.dev, custom_msg=None)
        # img_zoombar_min = cv.imread('res/zoombar_min_penacony.png', cv.IMREAD_COLOR)
        # screen_zoombar = screen[int(self.xy.height*980/1080):int(self.xy.height*1000/1080), int(self.xy.width*1054/2400):int(self.xy.width*1078/2400)]
        img_zoombar_min = cv.imread('res/zoombar_min.png', cv.IMREAD_COLOR)
        screen_zoombar = screen[int(self.xy.height*965/1080):int(self.xy.height*1015/1080), int(self.xy.width*780/2400):int(self.xy.width*1250/2400)]
        matches = cv.matchTemplate(screen_zoombar, img_zoombar_min, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(matches)
        if max_val < 0.95: # map isn't on min zoom, change zoom level
            logger('zoom map to min')
            for _ in range(20):
                # await self.dev.shell(f'input tap {self.xy.width*1000/2400} {self.xy.height*990/1080}') # penacony
                await self.dev.shell(f'input tap {self.xy.width*783/2400} {self.xy.height*993/1080}')
                await aio.sleep(0.075)
            await aio.sleep(0.1)
            logger('re-open map')
            await self.dev.shell(f'input keyevent 4')
            await aio.sleep(2.5)
            await self.open_map(penacony=penacony)

    async def use_teleporter(self, x, y, move_x=0, move_y=0, move_spd=1000, open_map=True, confirm=False, debug=False):
        # open map
        if open_map:
            await self.open_map()
        logger(f'use teleporter: {int(self.xy.width*x)},{int(self.xy.height*y)}; move map by {move_x},{move_y}')# move map
        if move_x != 0 or move_y != 0:
            cmd = f'input swipe {int(self.xy.width*0.45)} {int(self.xy.height*0.5)} {int(self.xy.width*(0.45+move_x))} {int(self.xy.height*(0.5+move_y))} {move_spd}'
            await self.dev.shell(cmd)
            await aio.sleep(3)
        # debug: send screenshot
        if debug:
            await self.adb.get_screen(dev=self.dev, debug=True)
            sys.exit()
        # tap teleporter
        await self.dev.shell(f'input tap {int(self.xy.width*x)} {int(self.xy.height*y)}')
        await aio.sleep(1.25)
        # confirm teleporter if other landmark is close
        if confirm == True:
            await self.dev.shell(f'input tap {int(self.xy.width*1200/2400)} {int(self.xy.height*700/1080)}')
            await aio.sleep(1.5)
        # teleport
        await self.dev.shell(f'input tap {int(self.xy.width*0.83)} {int(self.xy.height*0.9)}')
        await self.wait_for_onmap(min_duration=1, mapexit=True)

    async def switch_map(self, y_percentage, scroll_down=False, open_map=True, debug=False):
        logger('switch map')
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
        logger('swipe locations up')
        await aio.sleep(0.1)
        cmd = f'input swipe {int(self.xy.width*0.8)} {self.xy.height-200} {int(self.xy.width*0.8)} {self.xy.height-700} 150'
        await self.dev.shell(cmd)
        await aio.sleep(1.5)

    async def open_star_rail_map(self):
        await self.open_map()
        logger('open star rail map')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.star_rail_map[0]} {self.xy.star_rail_map[1]}')
        await aio.sleep(1.5)

    async def switch_world(self, world):
        logger('switch to world:')
        # select correct matching template
        if world == 'herta_space_station':
            logger('Herta Space Station')
            target = cv.imread('res/herta_space_station.png', cv.IMREAD_COLOR)
        if world == 'jarilo_vi':
            logger('Jarilo-VI')
            target = cv.imread('res/jarilo-vi.png', cv.IMREAD_COLOR)
        if world == 'the_xianzhou_luofu':
            logger('The Xianzhou Luofu')
            target = cv.imread('res/the_xianzhou_luofu.png', cv.IMREAD_COLOR)
        if world == 'penacony':
            logger('Penacony')
            target = cv.imread('res/penacony.png', cv.IMREAD_COLOR)
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

    async def interact(self):
        await aio.sleep(1)
        await self.action_tap(int(self.xy.width*1600/2400), int(self.xy.height*650/1080))
        await self.wait_for_onmap(min_duration=2)

    async def action_button(self):
        await aio.sleep(1)
        await self.action_tap(int(self.xy.width*1580/2400), int(self.xy.height*933/1080))
        await self.wait_for_onmap(min_duration=2)

    async def attack(self):
        logger('action: attack')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.attack[0]} {self.xy.attack[1]}')
        await aio.sleep(0.1)

    async def wait_for_onmap(self, min_duration=15, mapexit=False, debug=False):
        logger('wait for fight to end')
        if not debug:
            await aio.sleep(min_duration)
        img_warp= cv.imread('res/bw_warp.png', cv.IMREAD_GRAYSCALE)
        img_party= cv.imread('res/bw_party.png', cv.IMREAD_GRAYSCALE)
        img_mission= cv.imread('res/bw_mission.png', cv.IMREAD_GRAYSCALE)
        img_chat = cv.imread('res/bw_chat.png', cv.IMREAD_GRAYSCALE)
        img_sprint = cv.imread('res/bw_sprint.png', cv.IMREAD_GRAYSCALE)
        check = 0
        time_start = time()
        while check < 1:
            success = False
            while not success:
                try:
                    if debug:
                        screen = await self.adb.get_screen(dev=self.dev, custom_msg='still in fight')
                    else:
                        screen = await self.adb.get_screen(dev=self.dev, custom_msg=None)
                    screen = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
                    # screen_edges = cv.Canny(screen, 400, 500)
                    _, screen_bw = cv.threshold(screen, 200, 255, cv.THRESH_BINARY)
                    success = True
                except:
                    pass
            screen_warp = screen_bw[int(self.xy.height*0.03):int(self.xy.height*0.08), int(self.xy.width*0.75):int(self.xy.width*0.773)]
            screen_party = screen_bw[int(self.xy.height*0.03):int(self.xy.height*0.08), int(self.xy.width*0.88):int(self.xy.width*0.9)]
            screen_mission = screen_bw[int(self.xy.height*0.248):int(self.xy.height*0.31), int(self.xy.width*0.04):int(self.xy.width*0.062)]
            screen_chat = screen_bw[int(self.xy.height*0.868):int(self.xy.height*0.925), int(self.xy.width*0.04):int(self.xy.width*0.068)]
            screen_sprint = screen_bw[int(self.xy.height*0.815):int(self.xy.height*0.885), int(self.xy.width*0.88):int(self.xy.width*0.915)]
            if debug:
                # sc = screen_mission
                # si = img_mission
                # print(si.shape)
                # print(sc.shape)
                # ssi = compare_ssim(sc, si)
                # print(ssi)
                # cv.imwrite('img.png', sc)
                # cv.imshow('debug', sc)
                # cv.waitKey(0)
                # cv.destroyAllWindows()
                exit()
            images = [
                (screen_warp, img_warp),
                (screen_party, img_party),
                (screen_mission, img_mission),
                (screen_chat, img_chat),
                (screen_sprint, img_sprint)
            ]
            for i in images:
                ssi = compare_ssim(i[0], i[1])
                if ssi > 0.95:
                    check += 1
            if check > 2:
                await aio.sleep(1)
                logger('out of fight')
            time_running = time()
            if mapexit and (time_running - time_start > 400):
                raise PathError