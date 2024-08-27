from logger import logger, logger_set_path
from automation.bot import Bot


class Init:
    '''
    Status: 1/1
    Time:
    '''
    def __init__(self, device):
        self.bot = Bot(device)
    
    async def crafting(self):
        logger_set_path('craft tp restore items')
        await self.bot.craft_item('trick_snack', all=True)
        await self.bot.craft_item('punitive_energy', all=True)
    
    async def restore_tp(self, tp=4):
        logger_set_path('Teleport: TP Restore')
        logger.info('---')
        logger.info("--- Map: Storage Zone")
        logger.info('---')
        await self.bot.switch_map(y_list=630/1080, world='herta_space_station', scroll_down=False, # Outside the Control Center
                                x=576/2400, y=569/1080, corner='botright', move_x=0, move_y=0)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(5) # move
        await self.bot.move(1.35, 1600)
        n = int(tp/2)
        for i in range(n):
            logger.info(f'[{i+1}/{n}] Restore TP in Signs of Fragmentum')
            await self.bot.chat_initiate()
            await self.bot.chat_advance(n=3)
            await self.bot.action_tap(int(self.bot.xy.width*1750/2400), int(self.bot.xy.height*600/1080))
            await self.bot.sleep(2)
            await self.bot.action_tap(int(self.bot.xy.width*1900/2400), int(self.bot.xy.height*970/1080))
            await self.bot.sleep(2)
            await self.bot.action_tap(int(self.bot.xy.width*2000/2400), int(self.bot.xy.height*988/1080))
            await self.bot.wait_for_onmap()
            await self.bot.action_tap(int(self.bot.xy.width*1000/2400), int(self.bot.xy.height*250/1080))
            await self.bot.wait_for_onmap()
            await self.bot.move(0.5, 800)
            await self.bot.attack_technique(9) # move
            await self.bot.move(1.95, 950)
            await self.bot.attack_technique(5) # move
            await self.bot.move(0.3, 2000)
            await self.bot.move(0.12, 1600)
            await self.bot.move(1.9, 1500)
            await self.bot.move(1.75, 1600)
            await self.bot.move(1.6, 2000)
            await self.bot.move(1.5, 500)
            await self.bot.attack_technique(10) # +2TP
            await self.bot.attack()
            await self.bot.action_tap(int(self.bot.xy.width*118/2400), int(self.bot.xy.height*88/1080))
            await self.bot.sleep(2)
            await self.bot.action_tap(int(self.bot.xy.width*820/2400), int(self.bot.xy.height*791/1080))
            await self.bot.sleep(2)
            await self.bot.action_tap(int(self.bot.xy.width*1396/2400), int(self.bot.xy.height*705/1080))
            await self.bot.wait_for_onmap()


