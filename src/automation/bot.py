import asyncio as aio
import cv2 as cv
from datetime import datetime as dt

def logger(msg):
    dt_now = dt.now().strftime('%H:%M:%S')
    print(f'[{dt_now}] {msg}')


class Bot:
    def __init__(self, adb, dev, xy):
        self.adb = adb
        self.dev = dev
        self.xy = xy

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

    async def open_map(self):
        logger('open map')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.map[0]} {self.xy.map[1]}')
        await aio.sleep(2)

    # doesn't work
    async def zoom_map(self):
        logger('zoom map')
        await aio.sleep(0.1)
        bot_left = (int(self.xy.width*0.2), int(self.xy.height*0.8))
        top_right = (int(self.xy.width*0.6), int(self.xy.height*0.2))
        mid = (int(self.xy.width*0.4), int(self.xy.height*0.5))
        cmd = f'input swipe {bot_left[0]} {bot_left[1]} {mid[0]} {mid[1]} 1500 & input swipe {top_right[0]} {top_right[1]} {mid[0]} {mid[1]} 1500'
        await self.dev.shell(cmd)

    async def use_teleporter(self, x, y):
        logger(f'use teleporter: {x},{y}')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {x} {y}')
        await aio.sleep(1)
        await self.dev.shell(f'input tap {int(self.xy.width*0.83)} {int(self.xy.height*0.9)}')
        await self.wait_for_onmap(min_duration=3)

    async def switch_map(self, y_percentage, open_map=True, scroll_down=False):
        logger('switch map')
        if open_map:
            await self.open_map()
        if scroll_down:
            cmd = f'input swipe {int(self.xy.width*0.8)} {int(self.xy.height*0.8)} {int(self.xy.width*0.8)} {int(self.xy.height*0.3)} 1500'
            await self.dev.shell(cmd)
            await self.sleep(3)
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
        await aio.sleep(1)

    async def switch_world(self, world):
        logger('switch to world:')
        # open star rail map
        await self.open_star_rail_map()
        # get screenshot
        screen = await self.adb.get_screen(dev=self.dev)
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

    async def attack(self):
        logger('action: attack')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.attack[0]} {self.xy.attack[1]}')
        await aio.sleep(0.1)

    async def wait_for_onmap(self, min_duration=15):
        logger('wait for fight to end...')
        await aio.sleep(min_duration)
        img_menu = cv.imread('res/edges_menu.png', cv.IMREAD_GRAYSCALE)
        img_chat = cv.imread('res/edges_chat.png', cv.IMREAD_GRAYSCALE)
        img_sprint = cv.imread('res/edges_sprint.png', cv.IMREAD_GRAYSCALE)
        check = 0
        while check < 1:
            screen = await self.adb.get_screen(dev=self.dev, custom_msg='still in fight...')
            screen = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
            screen = cv.Canny(screen, 400, 500)
            screen_menu = screen[0:int(self.xy.height*0.2), int(self.xy.width*0.60):int(self.xy.width*0.975)]
            screen_chat = screen[int(self.xy.height*0.85):int(self.xy.height*0.975), int(self.xy.width*0.025):int(self.xy.width*0.075)]
            screen_sprint = screen[int(self.xy.height*0.775):int(self.xy.height*0.925), int(self.xy.width*0.875):int(self.xy.width*0.95)]
            images = [
                (screen_menu, img_menu),
                (screen_chat, img_chat),
                (screen_sprint, img_sprint)
            ]
            for i in images:
                result = cv.matchTemplate(i[0], i[1], cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                if max_val > 0.8:
                    check += 1
            if check > 0:
                await aio.sleep(1)
                logger('out of fight')