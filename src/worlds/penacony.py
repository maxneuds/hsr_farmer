import asyncio as aio
from automation.bot import Bot
from datetime import datetime as dt

def logger(msg):
    dt_now = dt.now().strftime('%H:%M:%S')
    print(f'[{dt_now}] {msg}')


class World:
    def __init__(self, bot, xy):
        # initialize bot
        self.bot = bot
        self.xy = xy

    async def farm(self):
        logger('Farm: Penacony')
        # await self.bot.switch_world('penacony')
        # farm locations
        # await self.farm_dreams_edge()
        await self.farm_next()

    async def farm_next(self):
        cmd = f'input swipe {int(self.xy.width*0.5)} {int(self.xy.height*0.5)} {int(self.xy.width*0.2)} {int(self.xy.height*0.5)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)


        await aio.sleep(0.1)
        await self.bot.dev.shell(f'input tap {1136/2400} {114/1080}')
        await aio.sleep(1)
        # await self.dev.shell(f'input tap {int(self.xy.width*0.83)} {int(self.xy.height*0.9)}')
        # await self.wait_for_onmap(min_duration=1)


        await self.bot.adb.get_screen(dev=self.bot.dev, debug=True)
        pass

    async def farm_reverie_dreamscape(self):
        await self.bot.switch_map(925/1080)
        logger('### group 1 ###')
        cmd = f'input swipe {int(self.xy.width*0.5)} {int(self.xy.height*0.5)} {int(self.xy.width*0.2)} {int(self.xy.height*0.5)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*1136/2400), int(self.xy.height*114/1080))

    async def farm_childs_dream(self):
        # TODO: add the simple 3D map
        await self.bot.switch_map(891/1080)
        logger('### group 1 ###')
        await self.bot.use_teleporter(int(self.xy.width*1010/2400), int(self.xy.height*376/1080))
        await self.bot.move('ne', 2000)
        await self.bot.move('e', 2000)
        await self.bot.move('n', 1000)
        await self.bot.move('ne', 1100)
        await self.bot.move('e', 250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 2 ###')
        await self.bot.open_map()
        cmd = f'input swipe {int(self.xy.width*0.5)} {int(self.xy.height*0.8)} {int(self.xy.width*0.5)} {int(self.xy.height*0.4)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*960/2400), int(self.xy.height*705/1080))
        await self.bot.move('s', 3500)
        await self.bot.move('se', 250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 3 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*960/2400), int(self.xy.height*435/1080))
        await self.bot.move('s', 14500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()


    async def farm_dreams_edge(self):
        await self.bot.switch_map(0.7176, open_map=False)
        logger('### group 1 ###')
        cmd = f'input swipe {int(self.xy.width*0.6)} {int(self.xy.height*0.2)} {int(self.xy.width*0.3)} {int(self.xy.height*0.6)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*0.3834), int(self.xy.height*0.3334))
        await self.bot.move('e', 4000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 2 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.4742), int(self.xy.height*0.4676))
        await self.bot.move('ne', 1500)
        await self.bot.move('n', 4500)
        await self.bot.move('e', 3700)
        await self.bot.move('n', 5500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 3 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.48375), int(self.xy.height*0.12315))
        await self.bot.move('ne', 1500)
        await self.bot.move('n', 4500)
        await self.bot.move('e', 3700)
        await self.bot.move('n', 11250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 4 ###')
        await self.bot.move('e', 250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 5 ###')
        await self.bot.open_map()
        cmd = f'input swipe {int(self.xy.width*0.3)} {int(self.xy.height*0.8)} {int(self.xy.width*0.6)} {int(self.xy.height*0.2)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*0.46125), int(self.xy.height*0.4112))
        await self.bot.move('n', 3000)
        await self.bot.move('nw', 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 5, part 2 ###')
        await self.bot.move('w', 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 6 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.43412), int(self.xy.height*0.4204))
        await self.bot.move('n', 3500)
        await self.bot.move('e', 2750)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 6, part 2 ###')
        await self.bot.move('n', 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 7 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.46083), int(self.xy.height*0.5334))
        await self.bot.move('n', 5000)
        await self.bot.move('nw', 1500)
        await self.bot.move('n', 3000)
        await self.bot.move('w', 2500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 8 ###')
        await self.bot.open_map()
        cmd = f'input swipe {int(self.xy.width*0.3)} {int(self.xy.height*0.5)} {int(self.xy.width*0.6)} {int(self.xy.height*0.5)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*0.355), int(self.xy.height*0.4343))
        await self.bot.move('s', 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 9 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.3684), int(self.xy.height*0.5213))
        await self.bot.move('sw', 2750)
        await self.bot.move('nw', 1500)
        await self.bot.move('w', 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 10 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.3546), int(self.xy.height*0.3861))
        await self.bot.open_map()
        cmd = f'input swipe {int(self.xy.width*0.5)} {int(self.xy.height*0.2)} {int(self.xy.width*0.5)} {int(self.xy.height*0.5)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*0.36584), int(self.xy.height*0.2112))
        await self.bot.move('n', 5000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 11 ###')
        await self.bot.open_map()
        cmd = f'input swipe {int(self.xy.width*0.5)} {int(self.xy.height*0.15)} {int(self.xy.width*0.5)} {int(self.xy.height*0.9)} 600'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*1281/2400), int(self.xy.height*125/1080))
        await self.bot.move('ne', 3000)
        await self.bot.move('n', 8500)
        await self.bot.move('w', 6000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
