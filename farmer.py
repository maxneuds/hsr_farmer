from pynput.keyboard import Key, Controller as PyKB
from pynput.mouse import Button, Controller as PyMouse
from time import sleep
from datetime import datetime as dt
from mss import mss
from difflib import get_close_matches
import pytesseract as tes
import numpy as np
import cv2 as cv
import re
from ppadb.client_async import ClientAsync as AdbClient
import asyncio as aio
# from asyncio import sleep, run, subprocess, create_subprocess_shell

def logger(msg):
  dt_now = dt.now().strftime('%H:%M:%S')
  print(f'[{dt_now}] {msg}')

class HSR_bot:
    def __init__(self):
        self.dev = aio.run(self.get_dev())
        self.height, self.width = aio.run(self.get_screensize())
        self.xy = self.OnePlus7T(self.width, self.height)
        logger(f'Screensize: {self.width} x {self.height}')

    class OnePlus7T():
        def __init__(self, w, h):
            # OnePlus 7T
            self.map = (int(w*240/2400), int(h*190/1080))
            self.star_rail_map = (int(w*2000/2400), int(h*145/1080))
            self.sprint = (int(w*2145/2400), int(h*925/1080))
            self.attack = (int(w*1965/2400), int(h*825/1080))
            self.skill = (int(w*1765/2400), int(h*925/1080))
            self.vjoy = {}
            self.vjoy['mid'] = (int(w*440/2400), int(h*839/1080))
            self.vjoy['n'] = (self.vjoy['mid'][0], self.vjoy['mid'][1]-150)
            self.vjoy['s'] = (self.vjoy['mid'][0], self.vjoy['mid'][1]+150)
            self.vjoy['w'] = (self.vjoy['mid'][0]-150, self.vjoy['mid'][1])
            self.vjoy['e'] = (self.vjoy['mid'][0]+150, self.vjoy['mid'][1])
            self.vjoy['ne'] = (self.vjoy['mid'][0]+100, self.vjoy['mid'][1]-100)
            self.vjoy['se'] = (self.vjoy['mid'][0]+100, self.vjoy['mid'][1]+100)
            self.vjoy['sw'] = (self.vjoy['mid'][0]-100, self.vjoy['mid'][1]+100)
            self.vjoy['nw'] = (self.vjoy['mid'][0]-100, self.vjoy['mid'][1]-100)

    async def get_dev(self):
        logger('get device connection to adb')
        client = AdbClient(host='127.0.0.1', port=5037)
        devices = await client.devices()
        dev = devices[0]
        print(f'Connected to: {dev.serial}')
        return dev

    async def get_screensize(self):
        result = await self.dev.shell('wm size')
        hxw = result.strip().split()[2]
        h, w = hxw.split('x')
        return(int(h), int(w))

    async def get_screen(self, custom_msg=False, debug=False):
        if custom_msg == False:
            logger('get screenshot from device')
        else:
            logger(custom_msg)
        # get screen from device
        im_byte_array = await self.dev.screencap()
        # convert to cv image
        screenshot = cv.imdecode(np.frombuffer(bytes(im_byte_array), np.uint8), cv.IMREAD_COLOR)
        if debug == True:
            cv.imshow('debug', screenshot)
            cv.waitKey(0)
            cv.destroyAllWindows()
        return(screenshot)

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
        bot_left = (int(self.width*0.2), int(self.height*0.8))
        top_right = (int(self.width*0.6), int(self.height*0.2))
        mid = (int(self.width*0.4), int(self.height*0.5))
        cmd = f'input swipe {bot_left[0]} {bot_left[1]} {mid[0]} {mid[1]} 1500 & input swipe {top_right[0]} {top_right[1]} {mid[0]} {mid[1]} 1500'
        await self.dev.shell(cmd)

    async def use_teleporter(self, x, y):
        logger(f'use teleporter: {x},{y}')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {x} {y}')
        await aio.sleep(1)
        await self.dev.shell(f'input tap {int(self.width*0.83)} {int(self.height*0.9)}')
        await aio.sleep(5)


    async def swipe_locations_up(self):
        logger('swipe locations up')
        await aio.sleep(0.1)
        cmd = f'input swipe {int(self.width*0.8)} {self.height-200} {int(self.width*0.8)} {self.height-700} 150'
        await self.dev.shell(cmd)
        await aio.sleep(1.5)

    async def open_star_rail_map(self):
        await self.open_map()
        logger('open star rail map')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.star_rail_map[0]} {self.xy.star_rail_map[1]}')
        await aio.sleep(1)

    async def switch_planet(self, planet):
        logger('switch to planet:')
        # open star rail map
        await self.open_star_rail_map()
        # get screenshot
        screen = await self.get_screen()
        # select correct matching template
        if planet == 'the_xianzhou_luofu':
            logger('The Xianzhou Luofu')
            target = cv.imread('res/the_xianzhou_luofu.png', cv.IMREAD_COLOR)
        # find match
        result = cv.matchTemplate(screen, target, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # Get the top-left corner coordinates of the matched region
        top_left = max_loc
        # Get the dimensions of the template image
        h, w, _ = target.shape
        # tap planet
        await self.dev.shell(f'input swipe {top_left[0] + int(w/2)} {top_left[1] + int(h/2)} {top_left[0] + int(w/2)} {top_left[1] + int(h/2)} 200')
        await aio.sleep(1.5)

    async def attack(self):
        logger('action: attack')
        await aio.sleep(0.1)
        await self.dev.shell(f'input tap {self.xy.attack[0]} {self.xy.attack[1]}')
        await aio.sleep(0.1)

    async def wait_fight_end(self, min_duration=15):
        logger('wait for fight to end...')
        sleep(min_duration)
        img_menu = cv.imread('res/edges_menu.png', cv.IMREAD_GRAYSCALE)
        img_chat = cv.imread('res/edges_chat.png', cv.IMREAD_GRAYSCALE)
        img_sprint = cv.imread('res/edges_sprint.png', cv.IMREAD_GRAYSCALE)
        check = 0
        while check < 1:
            screen = await self.get_screen(custom_msg='still in fight...')
            screen = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
            screen = cv.Canny(screen, 400, 500)
            screen_menu = screen[0:int(bot.height*0.2), int(bot.width*0.60):int(bot.width*0.975)]
            screen_chat = screen[int(bot.height*0.85):int(bot.height*0.975), int(bot.width*0.025):int(bot.width*0.075)]
            screen_sprint = screen[int(bot.height*0.775):int(bot.height*0.925), int(bot.width*0.875):int(bot.width*0.95)]
            images = [
                (screen_menu, img_menu),
                (screen_chat, img_chat),
                (screen_sprint, img_sprint)
            ]
            for i in images:
                result = cv.matchTemplate(i[0], i[1], cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
                if max_val > 0.75:
                    check += 1
            if check > 1:
                await aio.sleep(1)
                logger('out of fight')

    async def farm_xianzhou(self):
        logger('Farm: The Xianzhou Luofu')
        await self.switch_planet('the_xianzhou_luofu')
        # farm from bot to top
        await self.farm_scalegorge_waterscape()
        await self.farm_alchemy_commission()
        await self.farm_fyxestroll_garden()
        await self.farm_artisan_commission()

    async def farm_x(self):
        # switch map
        await self.open_map()
        await self.swipe_locations_up()
        await self.action_tap(int(self.width*0.8), int(self.height*0.745)) # modify
        await aio.sleep(1)

    async def farm_scalegorge_waterscape(self):
        # switch map
        await self.swipe_locations_up()
        await self.action_tap(int(self.width*0.8), int(self.height*0.85))
        await aio.sleep(1)
        # group 1
        cmd = f'input swipe {int(self.width*0.6)} {int(self.height*0.5)} {int(self.width*0.4)} {int(self.height*0.5)} 1000'
        await self.dev.shell(cmd)
        await aio.sleep(2)
        await self.use_teleporter(int(self.width*0.605), int(self.height*0.49))
        await self.move('s', 4400)
        await self.move('e', 2000)
        await self.move('n', 3300)
        await self.move('e', 3800)
        await self.attack()
        await aio.sleep(240) # wait for fight end
        # group 2
        await self.open_map()
        cmd = f'input swipe {int(self.width*0.2)} {int(self.height*0.5)} {int(self.width*0.6)} {int(self.height*0.5)} 1000'
        await self.dev.shell(cmd)
        await aio.sleep(2)
        await self.use_teleporter(int(self.width*0.464), int(self.height*0.6))
        await self.move('w', 5400)
        await self.move('s', 1300)
        await self.move('w', 6500)
        await self.attack()
        await self.sleep(60) # wait for fight end
        await self.move('n', 1000)
        await self.move('w', 2000)
        await self.attack()
        await self.sleep(60) # wait for fight end
        await self.move('n', 1500)
        await self.move('w', 750)
        await self.attack()
        await self.sleep(60) # wait for fight end
        # group 3
        await self.open_map()
        await self.use_teleporter(int(self.width*0.2346), int(self.height*0.6574))
        await self.move('s', 10500)
        await self.move('e', 333)
        await self.attack()
        # group 4
        await self.open_map()
        await self.use_teleporter(int(self.width*0.40125), int(self.height*0.70648))
        await self.move('s', 7100)
        await self.move('w', 9000)
        await self.attack()
        # group 5
        await self.open_map()
        await self.use_teleporter(int(self.width*0.3104), int(self.height*0.642))
        await self.move('s', 1600)
        await self.move('e', 3000)
        for _ in range(12):
            await self.move('s', 650)
            await self.move('e', 650)
        await self.move('e', 6000)
        await self.move('s', 2000)
        await self.attack()
        await self.sleep(60)
        await self.move('e', 1500)
        await self.move('s', 500)
        await self.attack()
        # group 6
        await self.open_map()
        await self.use_teleporter(int(self.width*0.5533), int(self.height*0.2583))
        await self.move('s', 3000)
        await self.move('e', 6300)
        await self.attack()
        await self.sleep(120)
        # group 7
        await self.open_map()
        await self.use_teleporter(int(self.width*0.37875), int(self.height*0.6083))
        await self.move('s', 3000)
        await self.move('e', 3500)
        await self.move('s', 3500)
        await self.move('s', 3500)
        await self.attack()
        await self.sleep(120)
        # group 8
        await self.open_map()
        await self.use_teleporter(int(self.width*0.33), int(self.height*0.1083))
        await self.move('w', 3000)
        await self.move('n', 750)
        await self.move('w', 6500)
        await self.attack()
        await self.sleep(120)

    async def farm_alchemy_commission(self):
        # switch map
        await self.open_map()
        await self.action_tap(int(self.width*0.8), int(self.height*0.745))
        await aio.sleep(1)
        # group 1
        cmd = f'input swipe {int(self.width*0.5)} {int(self.height*0.85)} {int(self.width*0.5)} {int(self.height*0.15)} 1500'
        await self.dev.shell(cmd)
        await aio.sleep(2)
        await self.use_teleporter(int(self.width*0.3658), int(self.height*0.70833))
        await self.move('s', 4000)
        await self.move('w', 1000)
        await self.move('s', 1500)
        await self.attack()
        await self.sleep(60)
        # group 2
        await self.open_map()
        await self.use_teleporter(int(self.width*0.3854), int(self.height*0.6796))
        await self.move('s', 4000)
        await self.move('w', 1000)
        await self.move('s', 2750)
        for _ in range(7):
            await self.move('w', 500)
            await self.move('s', 500)
        await self.move('w', 500)
        await self.attack()
        await self.sleep(60)
        # group 3
        await self.open_map()
        await self.use_teleporter(int(self.width*0.27875), int(self.height*0.2009))
        await self.move('w', 1500)
        await self.move('n', 4000)
        await self.move('w', 500)
        await self.move('n', 500)
        await self.attack()
        await self.sleep(60)
        # group 4
        await self.open_map()
        await self.use_teleporter(int(self.width*0.3721), int(self.height*0.3574))
        await self.move('w', 2500)
        await self.move('n', 3000)
        await self.move('w', 5000)
        await self.move('s', 2500)
        await self.attack()
        await self.sleep(60)
        # group 5
        await self.move('w', 1500)
        await self.attack()
        await self.sleep(120)
        # group 6
        await self.open_map()
        await self.use_teleporter(int(self.width*0.2717), int(self.height*0.4898))
        await self.move('w', 500)
        await self.move('s', 5000)
        await self.move('w', 4000)
        await self.move('s', 2000)
        await self.move('e', 5000)
        await self.move('s', 750)
        await self.move('e', 1800)
        await self.attack()
        await self.sleep(120)
        # group 7
        await self.open_map()
        await self.use_teleporter(int(self.width*0.6025), int(self.height*0.3102))
        await self.move('n', 3500)
        await self.move('w', 3000)
        await self.move('n', 1500)
        await self.move('w', 750)
        await self.move('n', 1250)
        await self.move('w', 1500)
        await self.move('n', 800)
        await self.move('w', 3500)
        for _ in range(4):
            await self.move('s', 500)
            await self.move('w', 500)
        await self.move('s', 750)
        await self.move('w', 2500)
        for _ in range(2):
            await self.move('s', 750)
            await self.move('w', 2000)
        await self.move('s', 750)
        await self.move('w', 750)
        await self.attack()
        await self.sleep(180)
        # group 8
        await self.open_map()
        await self.use_teleporter(int(self.width*0.2604), int(self.height*0.5102))
        await self.move('n', 1500)
        await self.move('w', 500)
        await self.move('n', 1500)
        for _ in range(8):
            await self.move('e', 325)
            await self.move('n', 500)
        await self.move('n', 750)
        for _ in range(4):
            await self.move('e', 300)
            await self.move('n', 500)
        await self.move('e', 1500)
        await self.move('n', 250)
        await self.move('e', 1000)
        await self.attack()
        await self.sleep(120)
        # group 9
        await self.open_map()
        await self.use_teleporter(int(self.width*0.5479), int(self.height*0.48796))
        await self.move('n', 1500)
        await self.move('w', 500)
        await self.move('n', 1500)
        for _ in range(8):
            await self.move('e', 325)
            await self.move('n', 500)
        await self.move('n', 750)
        for _ in range(4):
            await self.move('e', 300)
            await self.move('n', 500)
        await self.move('e', 1500)
        await self.move('n', 250)
        await self.move('e', 1000)
        await self.move('n', 1500)
        await self.move('e', 2500)
        await self.move('s', 500)
        await self.move('e', 1500)
        await self.move('n', 750)
        await self.move('e', 1500)
        await self.move('s', 800)
        await self.move('e', 1700)
        await self.move('s', 1200)
        await self.attack()
        await self.sleep(120)
        # group 10
        await self.open_map()
        await self.use_teleporter(int(self.width*0.5833), int(self.height*0.6852))
        await self.move('n', 1500)
        await self.move('w', 500)
        await self.move('n', 1500)
        for _ in range(8):
            await self.move('e', 325)
            await self.move('n', 500)
        await self.move('n', 750)
        for _ in range(4):
            await self.move('e', 300)
            await self.move('n', 500)
        await self.move('e', 1500)
        await self.move('n', 250)
        await self.move('e', 1000)
        await self.move('n', 1500)
        await self.move('e', 2500)
        await self.move('s', 500)
        await self.move('e', 1500)
        await self.move('n', 750)
        await self.move('e', 1500)
        await self.move('s', 800)
        await self.move('e', 1700)
        await self.move('s', 3200)
        for _ in range(4):
            await self.move('w', 400)
            await self.move('s', 500)
        await self.move('s', 2000)
        await self.move('e', 750)
        await self.move('s', 4000)
        await self.move('w', 1500)
        await self.move('s', 500)
        await self.move('w', 2250)
        await self.attack()
        await self.sleep(180)

    async def farm_fyxestroll_garden(self):
        # switch map
        await self.open_map()
        await self.action_tap(int(self.width*0.8), int(self.height*0.745)) # modify
        await aio.sleep(1)
        # group 1
        await self.use_teleporter(int(self.width*0.2825), int(self.height*0.40926))
        await self.move('s', 1000)
        await self.move('e', 4000)
        await self.move('s', 500)
        await self.move('e', 2000)
        await self.move('s', 500)
        await self.move('e', 1500)
        await self.move('n', 500)
        await self.attack()
        await self.wait_fight_end()
        # group 2
        await self.open_map()
        await self.use_teleporter(int(self.width*0.4417), int(self.height*0.699))
        await self.move('s', 1000)
        await self.move('e', 4000)
        await self.move('se', 2500)
        await self.move('ne', 3000)
        await self.move('e', 1400)
        await self.move('n', 1100)
        await self.attack()
        await self.wait_fight_end()
        # group 3
        await self.move('e', 750)
        await self.move('ne', 1100)
        await self.attack()
        await self.wait_fight_end()
        # group 4
        await self.open_map()
        await self.use_teleporter(int(self.width*0.3183), int(self.height*0.7704))
        await self.move('s', 5000)
        await self.attack()
        await self.wait_fight_end()
        # group 5
        await self.move('ne', 500)
        await self.attack()
        await self.wait_fight_end()
        # group 6
        await self.open_map()
        await self.use_teleporter(int(self.width*0.3183), int(self.height*0.3537))
        await self.move('s', 6500)
        await self.move('se', 2000)
        await self.move('s', 1000)
        await self.move('se', 2500)
        await self.move('s', 2000)
        await self.move('se', 1000)
        await self.move('s', 3000)
        await self.move('w', 1500)
        await self.move('n', 1200)
        await self.move('w', 1800)
        await self.attack()
        await self.wait_fight_end()
        # group 7
        await self.open_map()
        cmd = f'input swipe {int(self.width*0.5)} {int(self.height*0.2)} {int(self.width*0.5)} {int(self.height*0.6)} 1500'
        await self.dev.shell(cmd)
        await aio.sleep(3)
        await self.use_teleporter(int(self.width*0.31875), int(self.height*0.46759))
        await self.move('s', 6500)
        await self.move('se', 2000)
        await self.move('s', 1000)
        await self.move('se', 2500)
        await self.move('s', 2000)
        await self.move('se', 1000)
        await self.move('s', 3000)
        await self.move('e', 3000)
        await self.move('s', 700)
        await self.move('se', 1000)
        await self.attack()
        await self.wait_fight_end()
        # group 8
        await self.move('s', 4000)
        await self.attack()
        await self.sleep(30)
        await self.wait_fight_end()

    async def farm_artisan_commission(self):
        # switch map
        await self.open_map()
        await self.action_tap(int(self.width*0.8), int(self.height*0.5231))
        await aio.sleep(1)
        # group 1
        await self.use_teleporter(int(self.width*0.5121), int(self.height*0.10926))
        await self.move('n', 5400)
        await self.move('e', 6000)
        await self.attack()
        await self.wait_fight_end(min_duration=45)
        # group 2
        await self.open_map()
        await self.use_teleporter(int(self.width*0.3333), int(self.height*0.6685))
        await self.move('n', 9500)
        await self.move('w', 1000)
        await self.sleep(2)
        await self.move('s', 500)
        await self.attack()
        await self.wait_fight_end(min_duration=30)
        # group 3
        await self.open_map()
        await self.use_teleporter(int(self.width*0.4358), int(self.height*0.78056))
        await self.move('n', 10700)
        await self.move('e', 3900)
        await self.move('n', 5800)
        await self.move('e', 1400)
        await self.sleep(2)
        await self.move('s', 100)
        await self.attack()
        # group 4
        await self.open_map()
        cmd = f'input swipe {int(self.width*0.4)} {int(self.height*0.5)} {int(self.width*0.6)} {int(self.height*0.5)} 1500'
        await self.dev.shell(cmd)
        await aio.sleep(3)
        await self.use_teleporter(int(self.width*0.27917), int(self.height*0.812))



    async def farm_next(self):
        pass



bot = HSR_bot()
aio.run(bot.farm_next())
# aio.run(bot.get_screen(debug=True))
# aio.run(bot.farm_xianzhou())
#


# Load the image


        # break
