import asyncio as aio
from automation.bot import Bot
from datetime import datetime as dt
from sys import exit

def logger(msg):
    dt_now = dt.now().strftime('%H:%M:%S')
    print(f'[{dt_now}] {msg}')

class World:
    def __init__(self, bot, xy):
        # initialize bot
        self.bot = bot
        self.xy = xy

    async def parlor_car(self):
        logger('\nreturn: palor car\n')
        await self.bot.switch_map(266/1080)
        await self.bot.use_teleporter(925/2400, 515/1080) # Pom-Pom