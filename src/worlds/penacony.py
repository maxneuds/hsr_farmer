from logger import logger, logger_set_path
from sys import exit


class Golden_Hour:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self, tp_restore=False):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Golden Hour')
        logger.info('---')
        if tp_restore == 4:
            await self.bot.switch_map(y_list=650/1080, world='penacony',
                                        x=588/2400, y=356/1080, move_x=4, move_y=3,) # Sweet Corner
            exit() # also grab item
            await self.bot.movepi(1.6, 5000)
            await self.bot.movepi(1.25, 3000)
            await self.bot.attack() # +2TP
            await self.bot.use_teleporter(815/2400, 245/1080, move_x=0, move_y=2) # Oti Mall
            await self.bot.movepi(0.7, 2000)
            await self.bot.movepi(0.9, 4400)
            await self.bot.attack() # +2TP
        elif tp_restore == 2:
            await self.bot.switch_map(y_list=650/1080, world='penacony',
                                        x=330/2400, y=498/1080, corner='botright', move_x=0, move_y=0) # The Reverie Hotel Entrance
            await self.bot.movepi(0.35, 9000)
            await self.bot.movepi(0.8, 1000)
            await self.bot.attack_technique(3) # +2TP
        else:
            logger.debug('bad parameter')
            exit()


class Dreams_Edge:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Dream's Edge")
        logger.info('---')
        await self.bot.switch_map(y_list=771/1080, world='penacony', scroll_down=False, # Bud of Memories
                                    x=658/2400, y=738/1080, move_x=0, move_y=7, corner='botleft')
        await self.bot.movepi(1.65, 2300)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.movepi(1.2, 2000)
        await self.bot.movepi(1.7, 2000)
        await self.bot.posfix(1.65, 1000)
        await self.bot.movepi(0.8, 5700)
        await self.bot.attack_technique(1) # items
        await self.bot.movepi(1.8, 1400)
        await self.bot.movepi(1.3, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
        await self.bot.movepi(0.9, 1000)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.0, 1600)
        await self.bot.movepi(0.5, 2400)
        await self.bot.movepi(0.9, 900)
        await self.bot.attack_technique(1) # -3TP
        await self.bot.movepi(0.05, 400)
        await self.bot.attack_technique(8)
        await self.bot.restore_tp(n=4) # +4TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
        await self.bot.movepi(0.5, 3500)
        await self.bot.movepi(0.00, 2500)
        await self.bot.movepi(1.90, 1400)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.movepi(0.9, 1100)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(543/2400, 503/1080, move_x=3, move_y=1, corner='topright', confirm=True) # The Family's Construction Authority
        await self.bot.movepi(0.25, 3000)
        await self.bot.movepi(0.5, 8500)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.05, 5000)
        await self.bot.attack_technique(7) # -2TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
        await self.bot.movepi(0.5, 5000)
        await self.bot.movepi(0.75, 1500)
        await self.bot.movepi(0.5, 2000)
        await self.bot.movepi(0.38, 1800)
        await self.bot.attack() # items
        await self.bot.movepi(1.0, 500)
        await self.bot.attack_technique(8) # -1TP     
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(933/2400, 535/1080, move_x=0, move_y=5, corner='topright') # Dreamweaver Plaza
        await self.bot.movepi(1.97, 2000)
        await self.bot.attack_technique(8) # -1TP
        await self.bot.restore_tp(n=4) # +4TP
    async def path_6(self): # roamer
        logger_set_path(6)
        await self.bot.use_teleporter(933/2400, 535/1080, move_x=0, move_y=5, corner='topright') # Dreamweaver Plaza
        await self.bot.movepi(0.25, 1500)
        await self.bot.movepi(0.5, 4500)
        await self.bot.movepi(0.00, 3700)
        await self.bot.movepi(0.5, 11000)
        await self.bot.attack_technique(8) # -3TP
        await self.bot.movepi(1.2, 300)
        await self.bot.attack_technique(4) # stability
    async def path_7(self): # roamer
        logger_set_path(7)
        await self.bot.use_teleporter(909/2400, 345/1080, move_x=0, move_y=7, corner='botleft') # Shape of Roast
        exit() # check
        await self.bot.movepi(1.5, 3000)
        await self.bot.movepi(0.05, 1300)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.3, 300)
        await self.bot.attack_technique(5)
        await self.bot.movepi(0.75, 300)
        await self.bot.attack_technique(5)
        await self.bot.movepi(1.75, 300)
        await self.bot.attack_technique(5)
        await self.bot.restore_tp(n=4) # +4TP
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(933/2400, 535/1080, move_x=0, move_y=5, corner='topright') # Dreamweaver Plaza
        await self.bot.movepi(0.25, 1500)
        await self.bot.movepi(0.5, 4500)
        await self.bot.movepi(0.00, 3700)
        await self.bot.movepi(0.49, 5500)
        await self.bot.attack_technique(4) # -2TP


class Childs_Dream:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Childs's Dream")
        logger.info('---')
        await self.bot.switch_map(y_list=893/1080, world='penacony', scroll_down=False, # Corridor of Memories
                                    x=1010/2400, y=304/1080, move_x=0, move_y=4, corner='botright')
        await self.bot.movepi(0.25, 2000)
        await self.bot.movepi(0.0, 1900)
        await self.bot.movepi(0.5, 3300)
        await self.bot.attack() # items
        await self.bot.movepi(1.8, 3)
        await self.bot.attack_technique(8) # -2TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(962/2400, 356/1080, move_x=0, move_y=0, corner='botright') # Eddying Dreamscape
        await self.bot.movepi(1.9, 1600)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.1, 1700)
        await self.bot.movepi(1.5, 2900)
        await self.bot.movepi(1.9, 700)
        await self.bot.attack_technique(3) # -2TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(962/2400, 519/1080, move_x=0, move_y=0, corner='botright') # Bud of Aether
        await self.bot.movepi(1.45, 2200)
        await self.bot.movepi(1.88, 9500)
        await self.bot.interact()
        await self.bot.movepi(1.95, 2800)
        await self.bot.action_button()
        await self.bot.movepi(0.00, 3000)
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.25, 500)
        await self.bot.attack_technique(5)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(1010/2400, 304/1080, move_x=0, move_y=4, corner='botright') # Corridor of Memories
        await self.bot.movepi(1.5, 9300)
        await self.bot.movepi(1.0, 7000)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 500)
        await self.bot.attack_technique(6) # -3TP
        await self.bot.restore_tp(n=4) # +4TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(962/2400, 356/1080, move_x=0, move_y=0, corner='botright') # Eddying Dreamscape
        # exit() # check
        await self.bot.movepi(0.5, 9000)
        await self.bot.movepi(1.0, 3200)
        await self.bot.movepi(0.6, 300)
        await self.bot.movepi(0.5, 500)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 800)
        await self.bot.movepi(1.0, 3000)
        for _ in range(2): # -3TP
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.movepi(0.7, 2200)
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(0.0, 1500)
        await self.bot.restore_tp(n=2) # +2TP
        await self.bot.posfix(0.25, 1000)
        await self.bot.interact()
        await self.bot.movepi(1.25, 2500)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 2600)
        await self.bot.movepi(0.5, 2300)
        await self.bot.attack()
        await self.bot.movepi(1.0, 1300)
        await self.bot.movepi(0.5, 2200)
        await self.bot.action_button()
        await self.bot.movepi(0.46, 4700)
        await self.bot.movepi(0.0, 1600)
        await self.bot.action_button()
        await self.bot.movepi(0.0, 3000)
        await self.bot.movepi(0.5, 5000)
        await self.bot.movepi(1.0, 1300)
        await self.bot.movepi(0.5, 3800)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.movepi(0.25, 3000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.4, 2500)
        await self.bot.movepi(1.0, 700)
        await self.bot.interact()
        await self.bot.movepi(1.2, 1100)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 2700)
        await self.bot.movepi(0.5, 3000)
        await self.bot.action_button()
        await self.bot.movepi(0.5, 2000)
        await self.bot.movepi(1.0, 1600)
        await self.bot.movepi(1.5, 3000)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.restore_tp(n=2) # +2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(1122/2400, 617/1080, move_x=0, move_y=0, corner='botright') # Clock Factory
        await self.bot.movepi(0.5, 5000)
        await self.bot.movepi(1.0, 600)
        await self.bot.attack() # items
        await self.bot.movepi(1.3, 800)
        await self.bot.movepi(1.0, 500)
        await self.bot.attack_technique(5) # -1TP


class The_Reverie_Dreamscape:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: The Reverie (Dreamscape)")
        logger.info('---')
        await self.bot.switch_map(y_list=681/1080, world='penacony', scroll_down=True, # Shape of Nectar
                                    x=659/2400, y=697/1080, move_x=0, move_y=7, corner='topleft')
        await self.bot.movepi(1.5, 2600)
        await self.bot.attack() # +2TP  
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(1100/2400, 680/1080, move_x=0, move_y=7, corner='topleft') # VIP Lounge Corridor
        await self.bot.movepi(0.5, 1600)
        await self.bot.movepi(1.0, 2300)
        await self.bot.movepi(0.6, 1600)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(0.45, 2600)
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(10) # -1TP
    async def path_2(self): # roamer
        logger_set_path(2)
        await self.bot.use_teleporter(1133/2400, 634/1080, move_x=0, move_y=7, corner='topright', confirm=True) # Platinum Guest Room
        exit() # check
        await self.bot.movepi(0.5, 2800)
        await self.bot.movepi(1.0, 1200)
        await self.bot.attack() # items
        await self.bot.movepi(1.0, 3500)
        await self.bot.movepi(1.1, 800)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.movepi(1.05, 4000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.5, 500)
        await self.bot.movepi(1.0, 4300)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(6)
        for _ in range(5):
            await self.bot.movepi(0.8, 300)
            await self.bot.attack_technique(2)
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(864/2400, 506/1080, move_x=0, move_y=5, corner='botright') # Bud of Treasures
        await self.bot.movepi(1.5, 800)
        await self.bot.movepi(0.0, 4000)
        await self.bot.movepi(0.5, 4300)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.4, 1700)
        await self.bot.movepi(1.5, 4300)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 6300)
        await self.bot.movepi(1.4, 500)
        await self.bot.attack() # +2TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(1133/2400, 634/1080, move_x=0, move_y=7, corner='topright', confirm=True) # Platinum Guest Room
        await self.bot.movepi(0.5, 2600)
        await self.bot.movepi(1.0, 12900)
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.25, 1500)
        await self.bot.movepi(0.56, 6500)
        await self.bot.attack_technique(2)
        await self.bot.movepi(0.5, 500)
        await self.bot.movepi(0.4, 500)
        await self.bot.movepi(0.25, 500)
        await self.bot.movepi(0.5, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.0, 500)
        await self.bot.movepi(0.5, 1000)
        await self.bot.movepi(0.9, 300)
        await self.bot.attack_technique(8)
        await self.bot.restore_tp(n=4) # +4TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(1133/2400, 634/1080, move_x=0, move_y=7, corner='topright', confirm=True) # Platinum Guest Room
        await self.bot.movepi(0.5, 2800)
        await self.bot.movepi(1.0, 28000)
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1.5, 1000)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.movepi(0.6, 1800)
        await self.bot.attack_technique(3)
        await self.bot.movepi(1.25, 3000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.25, 400)
        await self.bot.movepi(0.5, 7300) 
        await self.bot.attack() # items
        await self.bot.movepi(1.75, 300)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.movepi(0.75, 4000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.8, 3600)
        await self.bot.movepi(1.5, 1900)
        await self.bot.interact()
        await self.bot.movepi(1.5, 1900)
        await self.bot.movepi(1.3, 2000)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(0.0, 1800)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.movepi(0.25, 1000)
        await self.bot.restore_tp(n=4) # +4TP
        exit()
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.4, 2300)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.2, 2000)
        exit() # precise kill into item
        await self.bot.attack_technique(1) # -1TP
        # works good starting here
        await self.bot.movepi(1.9, 1000)
        await self.bot.movepi(0.0, 2000)
        await self.bot.movepi(0.5, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.4, 1000)
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(1.0, 300)
        await self.bot.attack_technique(6)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.switch_map(y_list=681/1080, world='penacony', scroll_down=True, # Bud of Harmony
                                    x=1344/2400, y=255/1080, move_x=0, move_y=8, corner='botleft')
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 500)
        await self.bot.attack_technique(12) # -2TP
    async def path_7(self): # roamer
        logger_set_path(7)
        # await self.bot.use_teleporter(1100/2400, 680/1080, move_x=0, move_y=7, corner='topleft') # VIP Lounge Corridor
        # exit() # redo
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 4700)
        await self.bot.movepi(0.5, 900)
        # await self.bot.attack() # items
        exit()
        await self.bot.movepi(0.7, 4000)
        await self.bot.movepi(0.5, 800)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(1.0, 500)
        await self.bot.attack_technique(8) # -1TP
        await self.bot.restore_tp(n=4) # +4 TP
    
        
    async def path_12(self): # roamer
        logger_set_path(12)
        await self.bot.use_teleporter(1100/2400, 680/1080, move_x=0, move_y=7, corner='topleft') # VIP Lounge Corridor
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 5200)
        await self.bot.movepi(0.3, 400)
        await self.bot.attack()
        await self.bot.movepi(1.05, 3000)
        await self.bot.attack_technique(3)
        await self.bot.movepi(0.65, 900)
        await self.bot.attack_technique(3)
    
    async def path_14(self):
        logger_set_path(14)
        await self.bot.use_teleporter(1100/2400, 680/1080, move_x=0, move_y=7, corner='topleft') # VIP Lounge Corridor
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 5500)
        await self.bot.movepi(0.9, 2000)
        await self.bot.movepi(1.0, 3000)
        await self.bot.movepi(1.1, 2100)
        await self.bot.movepi(0.5, 200)
        await self.bot.attack()
        await self.bot.movepi(1.5, 900)
        await self.bot.movepi(1.0, 5800)
        await self.bot.sleep(2)
        await self.bot.movepi(1.1, 600)
        await self.bot.movepi(1.0, 6500)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(2)
        await self.bot.movepi(1.5, 1500)
        await self.bot.attack_technique(3)
    async def path_15(self):
        logger_set_path(15)
        await self.bot.use_teleporter(1100/2400, 680/1080, move_x=0, move_y=7, corner='topleft') # VIP Lounge Corridor
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 5500)
        await self.bot.movepi(0.9, 2000)
        await self.bot.movepi(1.0, 3000)
        await self.bot.movepi(1.15, 2000)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 5800)
        await self.bot.sleep(2)
        await self.bot.movepi(0.91, 2700)
        await self.bot.attack()
        await self.bot.movepi(1.55, 1800)
        await self.bot.interact()
        await self.bot.movepi(0.4, 200)
        await self.bot.movepi(0.5, 3800)
        await self.bot.movepi(0.6, 600)
        await self.bot.movepi(1.0, 200)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 3500)
        await self.bot.movepi(1.4, 1200)
        await self.bot.attack_technique(4)
        await self.bot.restore_tp(n=4) # +4 TP
    async def path_16(self):
        logger_set_path(16)
        await self.bot.use_teleporter(1100/2400, 680/1080, move_x=0, move_y=7, corner='topleft') # VIP Lounge Corridor
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 5500)
        await self.bot.movepi(0.9, 2000)
        await self.bot.movepi(1.0, 3000)
        await self.bot.movepi(1.1, 2000)
        await self.bot.sleep(2)
        await self.bot.movepi(1.1, 500)
        await self.bot.movepi(1.0, 5500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 600)
        await self.bot.movepi(1.15, 2100)
        await self.bot.interact()
        await self.bot.movepi(1.52, 3000)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 2100)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 2100)
        await self.bot.action_button()
        await self.bot.movepi(0.5, 2000)
        await self.bot.attack_technique(2)
        await self.bot.movepi(0.45, 2200)
        await self.bot.attack_technique(3)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_17(self):
        logger_set_path(17)
        await self.bot.use_teleporter(1100/2400, 680/1080, move_x=0, move_y=7, corner='topleft') # VIP Lounge Corridor
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 5500)
        await self.bot.movepi(0.9, 2000)
        await self.bot.movepi(1.0, 3000)
        await self.bot.movepi(1.1, 2000)
        await self.bot.sleep(2)
        await self.bot.movepi(1.1, 500)
        await self.bot.movepi(1.0, 5500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 600)
        await self.bot.movepi(1.15, 2000)
        await self.bot.movepi(1, 200)
        await self.bot.interact()
        await self.bot.movepi(0.5, 800)
        await self.bot.movepi(1.0, 6000)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 2100)
        await self.bot.movepi(0.5, 3500)
        await self.bot.action_button()
        await self.bot.movepi(0.49, 3000)
        await self.bot.movepi(0.05, 200)
        await self.bot.movepi(1.0, 300)
        await self.bot.attack_technique(4)
        await self.bot.movepi(0.1, 1700)
        await self.bot.attack_technique(3)
    
    
    async def path_20(self):
        logger_set_path(20)
        await self.bot.use_teleporter(1015/2400, 580/1080, move_x=0, move_y=0, corner='topleft') # Dreamjolt Hostelry
        await self.bot.movepi(0.5, 7500)
        await self.bot.movepi(1.0, 500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 500)
        await self.bot.attack_technique(2)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_21(self):
        logger_set_path(21)
        await self.bot.use_teleporter(1015/2400, 580/1080, move_x=0, move_y=0, corner='topleft') # Dreamjolt Hostelry
        await self.bot.movepi(0.1, 2300)
        await self.bot.movepi(0.5, 4500)
        await self.bot.movepi(0.0, 700)
        await self.bot.attack()
        await self.bot.movepi(0.6, 2500)
        await self.bot.movepi(0.5, 4000)
        await self.bot.sleep(2)
        await self.bot.movepi(0.5, 500)
        await self.bot.sleep(0.5)
        await self.bot.attack_technique(2)
        await self.bot.movepi(0.1, 200)
        await self.bot.attack_technique(3)
    async def path_22(self):
        logger_set_path(22)
        await self.bot.use_teleporter(1015/2400, 580/1080, move_x=0, move_y=0, corner='topleft') # Dreamjolt Hostelry
        await self.bot.movepi(0.1, 2300)
        await self.bot.movepi(0.5, 13100)
        await self.bot.movepi(1.0, 1900)
        await self.bot.movepi(0.5, 600)
        await self.bot.attack()
        await self.bot.movepi(1.0, 1300)
        await self.bot.interact()
        await self.bot.movepi(0.5, 3000)
        await self.bot.attack()
        await self.bot.movepi(0.5, 1500)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 1800)
        await self.bot.movepi(1.1, 1000)
        await self.bot.interact()
        await self.bot.movepi(0.7, 700)
        await self.bot.attack()
        await self.bot.movepi(0.0, 2500)
        await self.bot.action_button()
        await self.bot.movepi(0.00, 1000)
        await self.bot.movepi(1.7, 800)
        await self.bot.movepi(1.5, 4200)
        await self.bot.movepi(1.7, 1200)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(0.00, 2800)
        await self.bot.attack_technique(3)
        await self.bot.movepi(0.5, 1300)
        await self.bot.attack_technique(3)
        await self.bot.movepi(0.25, 3500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.45, 3250)
        await self.bot.movepi(0.0, 200)
        await self.bot.action_button()
        await self.bot.movepi(0.0, 2100)
        await self.bot.movepi(0.16, 1900)
        await self.bot.attack_technique(4)
        await self.bot.movepi(0.5, 1000)
        await self.bot.attack_technique(2)
        await self.bot.movepi(1.65, 3200)
        await self.bot.attack_technique(2)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_23(self):
        logger_set_path(23)
        await self.bot.use_teleporter(871/2400, 802/1080, move_x=0, move_y=3, corner='topleft') # Monitoring Room
        await self.bot.movepi(1.5, 6300)
        await self.bot.interact()
        await self.bot.movepi(0.5, 2000)
        await self.bot.movepi(0.0, 3500)
        await self.bot.movepi(0.5, 4100)
        await self.bot.interact()
        await self.bot.movepi(0.5, 3500)
        await self.bot.movepi(1.0, 7000)
        await self.bot.movepi(0.9, 1100)
        await self.bot.movepi(1.0, 100)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 1400)
        await self.bot.movepi(1.52, 1400)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.restore_tp(n=2) # +2TP
        # TODO: there is one more enemy, but far away
    async def path_24(self):
        logger_set_path(24)
        await self.bot.use_teleporter(871/2400, 802/1080, move_x=0, move_y=3, corner='topleft') # Monitoring Room
        await self.bot.movepi(0.7, 2400)
        await self.bot.movepi(1.0, 8500)
        await self.bot.attack()
        await self.bot.movepi(0.0, 8100)
        await self.bot.movepi(0.2, 4000)
        await self.bot.movepi(0.0, 1500)
        await self.bot.movepi(1.9, 500)
        await self.bot.attack()
        await self.bot.movepi(0.4, 600)
        await self.bot.movepi(0.0, 6500)
        await self.bot.movepi(1.7, 800)
        await self.bot.attack()
        await self.bot.movepi(1.4, 1000)
        await self.bot.movepi(1.5, 6000)
        await self.bot.movepi(1.25, 800)
        await self.bot.attack_technique(5)
        

class Dewlight_Pavilion:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Dewlight Pavilion")
        logger.info('---')
        await self.bot.switch_map(y_list=808/1080, world='penacony', scroll_down=True,
                                    x=801/2400, y=569/1080, corner='botright', move_x=0, move_y=0) # Reception Counter
        await self.bot.movepi(0.67, 3900)
        await self.bot.attack() # items
        await self.bot.movepi(0.1, 2100)
        await self.bot.movepi(0.5, 1800)
        await self.bot.movepi(1.09, 1900)
        await self.bot.attack() # items
        await self.bot.movepi(0.09, 2200)
        await self.bot.movepi(1.89, 1700)
        await self.bot.attack() # items
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(801/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Reception Counter
        await self.bot.movepi(0.5, 10350)
        await self.bot.movepi(0.0, 7000)
        await self.bot.movepi(1.5, 7000)
        await self.bot.movepi(1.7, 2100)
        await self.bot.movepi(1.3, 1900)
        await self.bot.interact()
        await self.bot.movepi(0.3, 2000)
        await self.bot.movepi(0.4, 1700)
        await self.bot.action_button()
        await self.bot.movepi(0.0, 1900)
        await self.bot.movepi(1.9, 400)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.5, 1300)
        await self.bot.movepi(0.1, 900)
        await self.bot.movepi(0.5, 500)
        await self.bot.attack_technique(2) # items
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(801/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Reception Counter
        await self.bot.movepi(0.5, 10350)
        await self.bot.movepi(0.0, 7000)
        await self.bot.movepi(1.5, 7000)
        await self.bot.movepi(1.7, 2100)
        await self.bot.movepi(1.3, 1900)
        await self.bot.interact()
        await self.bot.movepi(0.75, 2000)
        await self.bot.movepi(0.60, 1900)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 2300)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 1000)
        await self.bot.attack_technique(2)
        await self.bot.movepi(0.8, 1200)
        await self.bot.movepi(0.5, 800)
        await self.bot.attack_technique(5)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(801/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Reception Counter
        await self.bot.movepi(0.5, 10350)
        await self.bot.movepi(0.0, 7000)
        await self.bot.movepi(1.5, 7000)
        await self.bot.movepi(1.7, 2100)
        await self.bot.movepi(1.3, 1900)
        await self.bot.interact()
        await self.bot.movepi(0.75, 2000)
        await self.bot.movepi(0.60, 1900)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 1700)
        await self.bot.movepi(1.41, 3300)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 1700)
        await self.bot.movepi(1.7, 500)
        await self.bot.attack_technique(3)
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(1080/2400, 285/1080, move_x=0, move_y=5, corner='botleft') # Dreammaster Hall
        await self.bot.movepi(1.1, 1000)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.7, 1000)
        await self.bot.movepi(0.5, 5900)
        await self.bot.attack() # items
        await self.bot.movepi(0.0, 3100)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 1200)
        await self.bot.movepi(0.0, 800)
        await self.bot.movepi(0.5, 3800)
        await self.bot.movepi(0.0, 800)
        await self.bot.movepi(1.6, 3000)
        await self.bot.attack() # items
        await self.bot.movepi(1.4, 3300)
        await self.bot.attack_technique(1)
        await self.bot.movepi(0.1, 1000)
        await self.bot.movepi(1.5, 3500)
        await self.bot.attack_technique(2) # items
        await self.bot.restore_tp(n=2) # +2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(1080/2400, 285/1080, move_x=0, move_y=5, corner='botleft') # Dreammaster Hall
        await self.bot.movepi(0.2, 2300)
        await self.bot.movepi(0.5, 4200)
        await self.bot.movepi(0.0, 1000)
        await self.bot.movepi(0.5, 3800)
        await self.bot.movepi(0.0, 900)
        await self.bot.movepi(1.5, 7700)
        await self.bot.movepi(0.0, 10200)
        await self.bot.movepi(0.5, 3600)
        await self.bot.movepi(0.0, 2600)
        await self.bot.movepi(0.7, 2200)
        await self.bot.interact()
        await self.bot.movepi(1.8, 3550)
        await self.bot.movepi(1.5, 2350)
        await self.bot.attack() # items # TODO problem here
        await self.bot.movepi(1.5, 1300)
        await self.bot.attack() # items
        await self.bot.movepi(0.0, 3200)
        await self.bot.attack() # items
        await self.bot.posfix(1.75, 1500)
        await self.bot.movepi(0.6, 2800)
        await self.bot.movepi(0.1, 200)
        await self.bot.action_button()
        await self.bot.movepi(0.0, 2000)
        await self.bot.attack_technique(6)
        await self.bot.posfix(0.25, 5000)
        await self.bot.restore_tp(n=2) # +2TP
        await self.bot.movepi(1.04, 4200)
        await self.bot.attack() # items
        await self.bot.movepi(0.29, 1300)
        await self.bot.attack() # items
        await self.bot.movepi(0.95, 1200)
        await self.bot.attack() # items
        await self.bot.movepi(1.1, 1400)
        await self.bot.interact()
        await self.bot.movepi(0.0, 2000)
        await self.bot.movepi(1.5, 3300)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 1500)
        await self.bot.movepi(1.6, 2500)
        await self.bot.posfix(1.75, 1500)
        await self.bot.movepi(1.0, 3300)
        await self.bot.movepi(0.5, 2550)
        await self.bot.action_button()
        await self.bot.movepi(0.0, 2000)
        await self.bot.movepi(1.5, 2100)
        await self.bot.posfix(1.25, 1500)
        await self.bot.movepi(0.0, 2900)
        await self.bot.movepi(0.5, 6200)
        await self.bot.action_button()
        await self.bot.movepi(0.49, 5500)
        await self.bot.attack() # items
        await self.bot.posfix(0.25, 1500)
        await self.bot.movepi(1.1, 1250)
        await self.bot.movepi(1.0, 5500)
        await self.bot.attack() # items
        await self.bot.posfix(0.75, 1500)
        await self.bot.movepi(1.5, 1700)
        await self.bot.movepi(0.0, 1000)
        await self.bot.movepi(0.1, 600)
        await self.bot.movepi(0.25, 600)
        await self.bot.movepi(1.5, 600)
        await self.bot.movepi(1.4, 200)
        await self.bot.attack_technique(6)
        await self.bot.movepi(1.75, 2000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.movepi(0.7, 1000)
        await self.bot.movepi(0.4, 2500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.2, 2000)
        await self.bot.movepi(1.5, 4600)
        await self.bot.attack() # items
        await self.bot.movepi(0.2, 1800)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(2)
        await self.bot.movepi(0.25, 5000) # position fixing
        await self.bot.restore_tp(n=2) # +2TP
        await self.bot.movepi(1.5, 2800)
        await self.bot.movepi(0.0, 2000)
        await self.bot.movepi(0.3, 300)
        await self.bot.attack() # items
        await self.bot.movepi(0.1, 1000)
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(3)
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(1080/2400, 285/1080, move_x=0, move_y=5, corner='botleft') # Dreammaster Hall
        await self.bot.movepi(0.8, 2300)
        await self.bot.movepi(0.5, 4600)
        await self.bot.movepi(1.0, 1600)
        await self.bot.attack() # items
        await self.bot.movepi(0.1, 1000)
        await self.bot.movepi(0.5, 3400)
        await self.bot.movepi(1.0, 800)
        await self.bot.movepi(1.5, 6000)
        await self.bot.attack_technique(2)
        await self.bot.movepi(1.5, 3000)
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(2)
        await self.bot.restore_tp(n=4) # +2TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(1080/2400, 285/1080, move_x=0, move_y=5, corner='botleft') # Dreammaster Hall
        await self.bot.movepi(0.8, 2300)
        await self.bot.movepi(0.5, 4600)
        await self.bot.movepi(1.0, 900)
        await self.bot.movepi(0.5, 3400)
        await self.bot.movepi(1.0, 1200)
        await self.bot.movepi(1.5, 7700)
        await self.bot.movepi(1.0, 10100)
        await self.bot.movepi(0.49, 2700)
        await self.bot.attack() # items
        await self.bot.movepi(1.51, 4900)
        await self.bot.interact()
        await self.bot.movepi(1.5, 500)
        await self.bot.movepi(1.1, 1100)
        await self.bot.attack() # items
        await self.bot.posfix(1.25, 2000)
        await self.bot.movepi(0.1, 1200)
        await self.bot.movepi(0.0, 550)
        await self.bot.action_button()
        await self.bot.movepi(1.48, 2800)
        await self.bot.attack_technique(2)
        await self.bot.posfix(1.75, 6000)
        await self.bot.restore_tp(n=2) # +2TP
        await self.bot.movepi(1.75, 5000)
        await self.bot.movepi(0.95, 1600)
        await self.bot.attack() # items
        await self.bot.movepi(0.95, 3300)
        await self.bot.movepi(0.6, 1200)
        await self.bot.attack_technique(2)
        await self.bot.restore_tp(n=2) # +2TP
        await self.bot.movepi(0.45, 1900)
        await self.bot.attack_technique(1)
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(1080/2400, 285/1080, move_x=0, move_y=5, corner='botleft') # Dreammaster Hall
        await self.bot.movepi(0.8, 2300)
        await self.bot.movepi(0.5, 4600)
        await self.bot.movepi(1.0, 900)
        await self.bot.movepi(0.5, 3400)
        await self.bot.movepi(1.0, 1200)
        await self.bot.movepi(1.5, 7700)
        await self.bot.movepi(1.0, 10100)
        await self.bot.movepi(1.51, 1500)
        await self.bot.interact()
        await self.bot.movepi(0.5, 3000)
        await self.bot.posfix(0.25, 3500)
        await self.bot.movepi(1.2, 2000)
        await self.bot.movepi(1.0, 6000)
        await self.bot.movepi(0.6, 900)
        await self.bot.action_button()
        await self.bot.movepi(0.5, 1900)
        await self.bot.movepi(0.0, 2000)
        await self.bot.attack_technique(1)
        await self.bot.movepi(0.55, 2800)
        await self.bot.attack() # items
        await self.bot.posfix(0.9, 5000)
        await self.bot.movepi(1.78, 5800)
        await self.bot.movepi(1.5, 100)
        await self.bot.attack() # items
        await self.bot.movepi(0.32, 1700)
        await self.bot.movepi(0.48, 700)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.7, 1700)
        await self.bot.attack_technique(3)
    async def path_9(self):
        logger_set_path(9)
        await self.bot.use_teleporter(1080/2400, 285/1080, move_x=0, move_y=5, corner='botleft') # Dreammaster Hall
        await self.bot.movepi(0.5, 1000)
        await self.bot.interact()
        await self.bot.wait_for_onmap(min_duration=3, no_fight=True)
        await self.bot.movepi(0.51, 2800)
        await self.bot.attack() # items
        await self.bot.movepi(0.69, 1500)
        await self.bot.attack() # items
    async def path_10(self): # TP restore
        logger_set_path(10)
        await self.bot.use_teleporter(1093/2400, 629/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # Shape of Ire
        await self.bot.movepi(1.2, 1600)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 3300)
        await self.bot.movepi(0.0, 600)
        await self.bot.attack() # +2TP
    async def path_11(self): # roamer
        logger_set_path(11)
        await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.movepi(0.3, 2500)
        await self.bot.movepi(1.83, 6300)
        await self.bot.movepi(0.45, 700)
        await self.bot.attack_technique(2)
        await self.bot.movepi(1.7, 1500)
        await self.bot.attack_technique(3)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_12(self): # roamer
        logger_set_path(12)
        await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.movepi(0.3, 2500)
        await self.bot.movepi(1.83, 7000)
        await self.bot.movepi(0.3, 7000)
        await self.bot.movepi(0.5, 4200)
        await self.bot.attack_technique(2)
        await self.bot.movepi(1.5, 1100)
        await self.bot.attack_technique(3)
        await self.bot.movepi(0.0, 600)
        await self.bot.attack_technique(4)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_13(self):
        logger_set_path(13)
        await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.movepi(0.5, 11500)
        await self.bot.interact(check_on_map=False)
        await self.bot.action_tap(1535, 960)
        await self.bot.wait_for_onmap(min_duration=5)
        await self.bot.movepi(0.51, 5500)
        await self.bot.interact(check_on_map=False)
        await self.bot.action_tap(1535, 960)
        await self.bot.wait_for_onmap(min_duration=5)
        await self.bot.movepi(0.47, 2200)
        await self.bot.attack() # items
        await self.bot.movepi(0.65, 2200)
        await self.bot.attack_technique(1)
        await self.bot.movepi(0.1, 1600)
        await self.bot.attack_technique(2)
        await self.bot.restore_tp(n=4) # +2TP
    async def path_14(self):
        logger_set_path(14)
        logger.info('exit special map')
        await self.bot.dev.shell(f'input tap {self.bot.xy.map[0]} {self.bot.xy.map[1]}')
        await self.bot.sleep(5)
        await self.bot.action_tap(2160, 150)
        await self.bot.sleep(5)
        await self.bot.use_teleporter(1080/2400, 285/1080, move_x=0, move_y=5, corner='botleft') # Dreammaster Hall
        await self.bot.movepi(0.2, 2300)
        await self.bot.movepi(0.5, 4300)
        await self.bot.movepi(0.0, 8000)
        await self.bot.attack() # items
        await self.bot.posfix(0.2, 1200)
        await self.bot.movepi(1.45, 3000)
        await self.bot.movepi(1.5, 3300)
        await self.bot.movepi(0.3, 800)
        await self.bot.attack_technique(2)
        await self.bot.movepi(1.2, 500)
        await self.bot.movepi(1.0, 500)
        await self.bot.movepi(0.9, 100)
        await self.bot.attack_technique(3)


class Clock_Studios_Theme_Park:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Clock Studios Theme Park')
        logger.info('---')
        await self.bot.switch_map(y_list=925/1080, world='penacony', scroll_down=True,
                                    x=1100/2400, y=423/1080, move_x=3, move_y=3) # Bud of Preservation
        await self.bot.movepi(1.7, 2500)
        await self.bot.attack() # +2TP
    async def path_0(self):
        logger.info('### Path 0 ###')
        await self.bot.use_teleporter(1216/2400, 299/1080, move_x=1, move_y=6) # Theme Park Entrance
        await self.bot.movepi(0.45, 6300)
        await self.bot.attack(2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.attack(2)
        await self.bot.movepi(0.3, 6000)
        await self.bot.attack(3)
        await self.bot.movepi(1.0, 5800)
        await self.bot.attack(3)
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(1209/2400, 276/1080, move_x=1, move_y=6, confirm=True) # Theme Park Entrance
        await self.bot.movepi(0.36, 6000)
        await self.bot.movepi(0.2, 2600)
        await self.bot.movepi(0.5, 12900)
        await self.bot.movepi(0.25, 3000)
        await self.bot.movepi(0.5, 2000)
        await self.bot.movepi(0.2, 1000)
        await self.bot.movepi(0.5, 2700)
        await self.bot.movepi(0.9, 4000)
        await self.bot.movepi(0.6, 2000)
        await self.bot.movepi(0.8, 3000)
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.7, 2000)
        await self.bot.movepi(1.6, 900)
        await self.bot.attack_technique(2)
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(1209/2400, 276/1080, move_x=1, move_y=6, confirm=True) # Theme Park Entrance
        await self.bot.movepi(0.36, 6000)
        await self.bot.movepi(0.2, 2600)
        await self.bot.movepi(0.5, 12900)
        await self.bot.movepi(0.25, 3000)
        await self.bot.movepi(0.5, 2000)
        await self.bot.movepi(0.2, 1000)
        await self.bot.movepi(0.5, 2700)
        await self.bot.movepi(0.9, 4000)
        await self.bot.movepi(0.6, 2000)
        await self.bot.movepi(0.8, 3000)
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.1, 2500)
        await self.bot.movepi(1.5, 3000)
        await self.bot.movepi(1.6, 1800)
        await self.bot.movepi(1.2, 600)
        await self.bot.movepi(0.7, 3200)
        await self.bot.movepi(0.5, 2500)
        await self.bot.attack_technique(2)
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(1209/2400, 276/1080, move_x=1, move_y=6, confirm=True) # Theme Park Entrance
        await self.bot.movepi(0.7, 8300)
        await self.bot.movepi(0.5, 12800)
        await self.bot.movepi(0.8, 1800)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.7, 800)
        await self.bot.attack_technique(4)
    async def path_4(self):
        logger_set_path(4) # roamer
        await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
        await self.bot.movepi(0.7, 4400)
        await self.bot.movepi(1.0, 800)
        await self.bot.attack_technique(5)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
        await self.bot.movepi(0.75, 4500)
        await self.bot.movepi(0.99, 1800)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(8)
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(929/2400, 549/1080, corner='topleft', move_x=0, move_y=7) # Screening Area Entrance
        await self.bot.movepi(0.6, 2500)
        await self.bot.attack() # +2TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
        await self.bot.movepi(0.75, 4500)
        await self.bot.movepi(0.99, 2000)
        await self.bot.movepi(0.7, 2000)
        await self.bot.attack_technique(2)
        await self.bot.movepi(1.45, 1000)
        await self.bot.attack_technique(4)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
        await self.bot.movepi(0.49, 7000)
        await self.bot.movepi(0.01, 5500)
        await self.bot.movepi(0.5, 500)
        await self.bot.attack() # items
        await self.bot.movepi(0.52, 4500)
        await self.bot.attack_technique(3)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_9(self):
        logger_set_path(9)
        await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
        await self.bot.movepi(0.00, 5000)
        await self.bot.movepi(1.46, 3800)
        await self.bot.attack_technique(3)
    async def path_10(self):
        logger_set_path(10) # roamer
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
        await self.bot.movepi(1.55, 3500)
        await self.bot.movepi(1.35, 1500)
        await self.bot.movepi(1.2, 1000)
        await self.bot.attack_technique(8)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_11(self):
        logger_set_path(11)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
        await self.bot.movepi(1.58, 7000)
        await self.bot.attack_technique(2)
    async def path_12(self):
        logger_set_path(12)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
        await self.bot.movepi(0.2, 3000)
        await self.bot.movepi(1.98, 4500)
        await self.bot.attack()
        await self.bot.movepi(0.4, 1000)
        await self.bot.movepi(0.55, 1500)
        await self.bot.attack_technique(2)
        await self.bot.movepi(0.5, 2000)
        await self.bot.attack_technique(2)
        await self.bot.restore_tp(n=2) # +2TP
    async def path_13(self): # roamer
        logger_set_path(13)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
        await self.bot.movepi(0.51, 3000)
        await self.bot.movepi(0.6, 3100)
        await self.bot.movepi(0.57, 2100)
        await self.bot.attack()
        await self.bot.movepi(0.05, 2300)
        await self.bot.attack_technique(4)
        await self.bot.movepi(0.0, 1000)
        await self.bot.attack_technique(4)
        await self.bot.movepi(1.8, 2000)
    async def path_14(self): # TP regeneration
        logger_set_path(14)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
        await self.bot.movepi(0.25, 2000)
        await self.bot.movepi(0.05, 9000)
        await self.bot.attack()
        await self.bot.movepi(1.55, 6000)
        await self.bot.movepi(0.05, 600)
        await self.bot.attack() # +2TP
    async def path_15(self): # roamer
        logger_set_path(15)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
        await self.bot.movepi(0.51, 3000)
        await self.bot.movepi(0.6, 3100)
        await self.bot.movepi(0.57, 3100)
        await self.bot.movepi(0.1, 2000)
        await self.bot.attack_technique(2)
        await self.bot.movepi(0.0, 500)
        await self.bot.attack_technique(6)

    