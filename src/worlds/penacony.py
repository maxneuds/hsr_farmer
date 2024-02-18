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
        await self.bot.switch_world('penacony')
        # farm locations
        await self.farm_dreams_edge()
        # await self.farm_next()

    async def farm_next(self):
        # await self.bot.adb.get_screen(dev=self.bot.dev, debug=True)
        pass

    async def farm_dreams_edge(self):
        await self.bot.switch_map(0.7176, open_map=False)
        # group 1
        cmd = f'input swipe {int(self.xy.width*0.6)} {int(self.xy.height*0.2)} {int(self.xy.width*0.3)} {int(self.xy.height*0.6)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*0.3834), int(self.xy.height*0.3334))
        await self.bot.move('e', 4000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 2
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.4742), int(self.xy.height*0.4676))
        await self.bot.move('ne', 1500)
        await self.bot.move('n', 4500)
        await self.bot.move('e', 3700)
        await self.bot.move('n', 5500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 3
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.48375), int(self.xy.height*0.12315))
        await self.bot.move('ne', 1500)
        await self.bot.move('n', 4500)
        await self.bot.move('e', 3700)
        await self.bot.move('n', 11250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 4
        await self.bot.move('e', 250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 5
        await self.bot.open_map()
        cmd = f'input swipe {int(self.xy.width*0.3)} {int(self.xy.height*0.8)} {int(self.xy.width*0.6)} {int(self.xy.height*0.2)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*0.46125), int(self.xy.height*0.4112))
        await self.bot.move('n', 3000)
        await self.bot.move('nw', 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 5, part 2
        await self.bot.move('w', 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 6
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.43412), int(self.xy.height*0.4204))
        await self.bot.move('n', 2000)
        await self.bot.move('e', 2500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 6, part 2
        await self.bot.move('n', 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 7
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.46083), int(self.xy.height*0.5334))
        await self.bot.move('n', 5000)
        await self.bot.move('nw', 1500)
        await self.bot.move('n', 3000)
        await self.bot.move('w', 2500)
        await self.bot.attack()
        # group 8
        await self.bot.open_map()
        cmd = f'input swipe {int(self.xy.width*0.3)} {int(self.xy.height*0.5)} {int(self.xy.width*0.6)} {int(self.xy.height*0.5)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*0.355), int(self.xy.height*0.4343))
        await self.bot.move('s', 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 9
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.3684), int(self.xy.height*0.5213))
        await self.bot.move('sw', 2750)
        await self.bot.move('nw', 1500)
        await self.bot.move('w', 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 10
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
        # group 11
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
