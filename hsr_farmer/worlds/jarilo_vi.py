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
        # await self.bot.switch_world('jarilo_vi')
        # farm locations
        await self.farm_next()

    async def farm_next(self):

        # await self.bot.adb.get_screen(dev=self.bot.dev, debug=True)
        pass

    async def farm_outlying_snow_plains(self):
        await self.bot.switch_map(505/1080, open_map=False)
        await self.bot.use_teleporter(int(self.xy.width*1604/2400), int(self.xy.height*593/1080))
        # group 1
