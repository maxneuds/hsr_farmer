from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Central_Starskiff_Haven:
    def __init__(self, device):
        self.map = 'Central Starskiff Haven'
        self.bot = Bot(device)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: Central Starskiff Haven')
        logger.info('---')
        await self.bot.switch_map(y_list=388/1080, world='the_xianzhou_luofu', scroll_down=False,
                                    x=803/2400, y=654/1080, corner='topleft', move_x=0, move_y=0) # Starskiff Jetty
        await self.bot.move(0.0, 6000)
        await self.bot.move(1.5, 7200)
        await self.bot.move(1.7, 1000)
    async def shop_salesby(self):
        logger_set_path(self.map, 'Shop Salesby')
        await self.bot.chat_initiate()
        await self.bot.chat_advance(n=2)
        await self.bot.action_tap(int(self.bot.xy.width*1654/2400), int(self.bot.xy.height*484/1080))
        await self.bot.sleep(1)
        await self.bot.chat_advance(n=1)
        await self.bot.buy_item('gaseous_liquid')
        await self.bot.buy_item('seed')
        # await self.bot.buy_item('virtual_particle', amount_percentage=20) # disabled, not needed anymore
        await self.bot.shop_exit()