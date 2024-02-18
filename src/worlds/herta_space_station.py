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
        logger('Farm: Herta Space Station')
        await self.bot.switch_world('herta_space_station')
        # farm locations
        await self.farm_base_zone()
        # await self.farm_storage_zone()
        # await self.farm_supply_zone()
        # await self.farm_seclusion_zone()

    async def farm_next(self):
        # group 1
        pass

    async def farm_storage_zone(self):
        await self.bot.switch_map(0.5833)
        await self.bot.use_teleporter(int(self.xy.width*0.18167), int(self.xy.height*0.4546))
        # group 1

    async def farm_supply_zone(self):
        await self.bot.switch_map(0.463)
        # group 1

    async def farm_seclusion_zone(self):
        await self.bot.switch_map(0.463)
        # group 1

    async def farm_base_zone(self):
        await self.bot.switch_map(0.463)
        # group 1
        cmd = f'input swipe {int(self.xy.width*0.5)} {int(self.xy.height*0.3)} {int(self.xy.width*0.5)} {int(self.xy.height*0.6)} 1000'
        await self.bot.dev.shell(cmd)
        await aio.sleep(2)
        await self.bot.use_teleporter(int(self.xy.width*0.4533), int(self.xy.height*0.1815))
        await self.bot.move('s', 2500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()