import asyncio as aio
from logger import logger
from automation.bot import Bot
from datetime import datetime as dt
from sys import exit

class World:
    def __init__(self, bot):
        self.bot = bot


    async def parlor_car(self):
        x = self.Parlor_Car(bot=self.bot)
        await x.teleport()
    class Parlor_Car:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Parlor Car")
            logger.info('---')
            await self.bot.switch_map(y_list=266/1080, world='herta_space_station', scroll_down=False,
                                      x=923/2400, y=206/1080, corner='botleft', move_x=0, move_y=0) # Pom-Pom

