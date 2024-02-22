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
        logger('Farm: Jarilo-VI')
        await self.bot.switch_world('jarilo_vi')
        # farm locations
        await self.farm_outlying_snow_plains()
        await self.farm_backwater_pass()
        await self.farm_corridor()

    async def farm_corridor(self):
        await self.bot.switch_map(866/1080)
        logger('### group 1 ###')
        cmd = f'input swipe {int(self.xy.width*0.5)} {int(self.xy.height*0.8)} {int(self.xy.width*0.5)} {int(self.xy.height*0.2)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*966/2400), int(self.xy.height*745/1080))

        # await self.bot.adb.get_screen(dev=self.bot.dev, debug=True)
        pass

    async def farm_backwater_pass(self):
        await self.bot.switch_map(637/1080)
        logger('### group 1 ###')
        await self.bot.use_teleporter(int(self.xy.width*941/2400), int(self.xy.height*892/1080))
        await self.bot.move('s', 5500)
        await self.bot.move('w', 6000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 2 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*790/2400), int(self.xy.height*310/1080))
        await self.bot.move('s', 6000)
        await self.bot.move('se', 3000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 2, part 2 ###') # stability: roamer
        await self.bot.move('s', 500)
        await self.bot.move('e', 2000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 3 ###')
        await self.bot.move('e', 7000)
        await self.bot.move('n', 3500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 4 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*980/2400), int(self.xy.height*250/1080))
        await self.bot.move('s', 6000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 5 ###')
        await self.bot.move('s', 2500)
        await self.bot.move('se', 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()

    async def farm_outlying_snow_plains(self):
        await self.bot.switch_map(506/1080, open_map=False)
        logger('### group 1 ###')
        await self.bot.use_teleporter(int(self.xy.width*1608/2400), int(self.xy.height*594/1080))
        await self.bot.move('sw', 3000)
        await self.bot.move('w', 3000)
        await self.bot.move('sw', 2000)
        await self.bot.attack()
        await self.bot.wait_for_onmap(min_duration=20)
        logger('### group 2 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*944/2400), int(self.xy.height*159/1080), confirm=True)
        await self.bot.move('w', 2500)
        await self.bot.move('sw', 3000)
        await self.bot.move('w', 4000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 3 ###')
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*948/2400), int(self.xy.height*121/1080))
        await self.bot.move('sw', 1500)
        await self.bot.move('w', 6000)
        await self.bot.move('sw', 3000)
        await self.bot.move('w', 4100)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 4 ###')
        await self.bot.move('n', 3000)
        await self.bot.move('nw', 1200)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
