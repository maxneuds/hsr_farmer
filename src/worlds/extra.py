from logger import logger, logger_set_path
from automation.bot import Bot
from datetime import datetime as dt
import pandas as pd
import os


class Extra:
    '''
    craft_extra: trick snack, punitive energy
    restore_tp: 2 TP x n in Herta Storage Zone
    '''
    def __init__(self, device):
        self.bot = Bot(device)
    async def metrics(self, map_name, t_start):
        row = {'map': [map_name], 'time': int((dt.now() - t_start).total_seconds())}
        df_row = pd.DataFrame(row)
        df_row.to_csv('data/metrics.csv', mode='a', index=False, header=False)
    
    async def craft_items(self, items=[]):
        '''
        available: trick_snack , punitive_energy
        '''
        for item in items:
            await self.bot.craft_item(item, all=True)
    async def restore_tp(self, tp=4, info=None):
        if info is None:
            logger_set_path('Storage Zone', 'TP Restore')
        else:
            logger_set_path(info, 'TP Restore')
        logger.info('---')
        logger.info("--- Map: Storage Zone")
        logger.info('---')
        t_start = dt.now()
        await self.bot.switch_map(y_list=630/1080, world='herta_space_station', scroll_down=False, # Outside the Control Center
                                x=576/2400, y=569/1080, corner='botright', move_x=0, move_y=0)
        await self.bot.move(1.0, 3600)
        await self.bot.move(1.35, 1500)
        n = int(tp/2)
        for i in range(n):
            logger.info(f'[{i+1}/{n}] Restore TP in Signs of Fragmentum')
            await self.bot.chat_initiate()
            await self.bot.chat_advance(n=3)
            await self.bot.action_tap(int(self.bot.xy.width*1750/2400), int(self.bot.xy.height*600/1080))
            await self.bot.sleep(2.5)
            await self.bot.action_tap(int(self.bot.xy.width*1900/2400), int(self.bot.xy.height*970/1080))
            await self.bot.sleep(2.5)
            await self.bot.action_tap(int(self.bot.xy.width*2000/2400), int(self.bot.xy.height*988/1080))
            await self.bot.wait_for_ready(min_duration=3, reason='wait for mission start')
            await self.bot.action_tap(int(self.bot.xy.width*1000/2400), int(self.bot.xy.height*250/1080))
            await self.bot.wait_for_ready(min_duration=2, reason='wait for info screen gone')
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
            await self.bot.sleep(2.5)
            await self.bot.action_tap(int(self.bot.xy.width*820/2400), int(self.bot.xy.height*791/1080))
            await self.bot.sleep(2.5)
            await self.bot.action_tap(int(self.bot.xy.width*1396/2400), int(self.bot.xy.height*705/1080))
            await self.bot.wait_for_ready(min_duration=3, reason='wait for mission exit')
        await self.metrics(f'Extra TP {tp}', t_start)


