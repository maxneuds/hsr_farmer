from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt


class The_Reverie_Dreamscape:
    '''
    TODO: there is one more 3D room
    37/??? fights
    R2/4: 1 / 2 
    # TP:-22->1 XP:14580/15552 Time:?
    '''
    def __init__(self, device):
        self.map = 'The Reverie Dreamscape'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self, mode='credits'):
        t_start = dt.now()
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.path_7()
        await self.path_8()
        await self.path_9()
        await self.path_10()
        await self.path_11()
        await self.path_12()
        await self.path_13()
        await self.path_14()
        await self.path_15()
        await self.extra.restore_tp(tp=4, info='The Reverie Dreamscape 1')
        await self.path_16()
        await self.extra.restore_tp(tp=4, info='The Reverie Dreamscape 2')
        await self.path_17()
        await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: The Reverie (Dreamscape)")
        logger.info('---')
        await self.bot.switch_map(y_list=1011/1080, world='penacony', scroll_down=False, # Dreamjolt Hostelry
                                    x=865/2400, y=461/1080, move_x=0, move_y=0, corner='topleft')
        await self.bot.move(0.5, 7500)
        await self.bot.move(1.0, 500)
        await self.bot.sleep(2)
        await self.bot.move(1.0, 2500)
        await self.bot.sleep(2)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(2) # -1TP
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(935/2400, 587/1080, move_x=0, move_y=5, corner='topleft') # VIP Lounge Corridor
        await self.bot.move(1.25, 1300)
        await self.bot.move(1, 5000)
        await self.bot.move(0.45, 600)
        await self.bot.attack() # items
        await self.bot.move(1.4, 500)
        for _ in range(10):
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.9, 300)
        await self.bot.attack_technique(8) # -2TP
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(1021/2400, 546/1080, move_x=0, move_y=3, corner='botright') # Bud of Treasures
        await self.bot.move(1.5, 800)
        await self.bot.move(0.0, 4000)
        await self.bot.move(0.5, 4300)
        await self.bot.attack() # +2TP
        await self.bot.move(1.4, 1700)
        await self.bot.move(1.5, 4300)
        await self.bot.attack() # items
        await self.bot.move(1.5, 6300)
        await self.bot.move(1.4, 500)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(1132/2400, 660/1080, move_x=0, move_y=8, corner='botleft') # Bud of Harmony
        await self.bot.move(1.0, 2500)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(12) # -2TP, roamer
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(1241/2400, 520/1080, move_x=0, move_y=5, corner='topright', confirm=True) # Platinum Guest Room
        await self.bot.move(0.5, 2700)
        await self.bot.move(0.9, 1400)
        await self.bot.attack() # items
        await self.bot.move(1.1, 1700)
        await self.bot.move(1.0, 3000)
        await self.bot.sleep(0.5)
        await self.bot.attack() # +2TP
        await self.bot.move(1.05, 4000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.5, 500)
        await self.bot.move(1.0, 4400)
        await self.bot.move(0.5, 3200)
        await self.bot.attack_technique(1)
        for _ in range(6): # -3TP, roamer
            await self.bot.move(0.75, 300)
            await self.bot.attack_technique(2)
        for _ in range(6):
            await self.bot.move(1.8, 300)
            await self.bot.attack_technique(2)
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(850/2400, 296/1080, move_x=0, move_y=4, corner='botright') # Dreamscape Lobby
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(19)
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.0, 900)
        await self.bot.move(0.48, 300)
        await self.bot.attack_technique(22)
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(2)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(4) # +2TP
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(935/2400, 587/1080, move_x=0, move_y=5, corner='topleft') # VIP Lounge Corridor
        await self.bot.move(1.25, 1200)
        await self.bot.move(1.0, 5100)
        await self.bot.move(0.5, 4800)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(10) # -1TP
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(935/2400, 587/1080, move_x=0, move_y=5, corner='topleft') # VIP Lounge Corridor
        await self.bot.move(0.5, 1600)
        await self.bot.move(1.0, 2300)
        await self.bot.move(0.6, 1600)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.45, 2600)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(10) # -1TP
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(574/2400, 482/1080, move_x=0, move_y=6, corner='topleft') # Shape of Nectar
        await self.bot.move(1.5, 2600)
        await self.bot.attack() # +2TP
    async def path_9(self):
        logger_set_path(self.map, 9)
        await self.bot.use_teleporter(865/2400, 461/1080, move_x=0, move_y=0, corner='topleft') # Dreamjolt Hostelry
        await self.bot.move(0.1, 2300)
        await self.bot.move(0.5, 4500)
        await self.bot.move(0.0, 700)
        await self.bot.attack() # items
        await self.bot.move(0.6, 2500)
        await self.bot.move(0.5, 4000)
        await self.bot.sleep(2)
        await self.bot.move(0.5, 500)
        await self.bot.sleep(2)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.1, 300)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(9) # items
    async def path_10(self):
        logger_set_path(self.map, 10)
        await self.bot.use_teleporter(865/2400, 461/1080, move_x=0, move_y=0, corner='topleft') # Dreamjolt Hostelry
        await self.bot.move(1.95, 500)
        await self.bot.attack_technique(8) # items
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(11) # items
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.75, 700)
        await self.bot.move(0.5, 700)
        await self.bot.attack_technique(20) # move
        await self.bot.move(1.8, 500)
        await self.bot.attack_technique(6) # +2TP
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.55, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(3) # items
    async def path_11(self):
        logger_set_path(self.map, 11)
        await self.bot.use_teleporter(865/2400, 461/1080, move_x=0, move_y=0, corner='topleft') # Dreamjolt Hostelry
        await self.bot.move(0.1, 2300)
        await self.bot.move(0.5, 13100)
        await self.bot.move(1.0, 1900)
        await self.bot.move(0.5, 600)
        await self.bot.attack() # items
        await self.bot.move(1.0, 1300)
        await self.bot.interact()
        await self.bot.move(0.5, 3000)
        await self.bot.attack() # +2TP
        await self.bot.move(0.5, 1500)
        await self.bot.action_button()
        await self.bot.move(1.0, 1800)
        await self.bot.move(1.1, 1000)
        await self.bot.interact()
        await self.bot.move(0.7, 700)
        await self.bot.attack() # items
        await self.bot.move(0.0, 2500)
        await self.bot.action_button()
        await self.bot.move(0.00, 1000)
        await self.bot.move(1.7, 800)
        await self.bot.move(1.5, 4200)
        await self.bot.move(1.7, 1200)
        await self.bot.action_button()
        await self.bot.move(1.5, 4000)
        await self.bot.move(0.00, 2800)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(0.5, 1300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.25, 3500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.45, 3250)
        await self.bot.move(0.0, 500)
        await self.bot.action_button()
        await self.bot.move(0.0, 2100)
        await self.bot.move(0.16, 1900)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(0.4, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.move(1.6, 300)
        await self.bot.attack_technique(6) # items
    async def path_12(self):
        logger_set_path(self.map, 12)
        await self.bot.use_teleporter(1241/2400, 520/1080, move_x=0, move_y=5, corner='topright', confirm=True) # Platinum Guest Room
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(4) # move
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(21) # move
        await self.bot.move(0.55, 500)
        await self.bot.attack_technique(8) # move
        await self.bot.move(0.825, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(12) # items
        await self.bot.move(0.8, 2000)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.5, 700)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(2) # move
        await self.bot.attack()
        await self.bot.move(1.0, 300)
        await self.bot.interact(wait_for_ready=True)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(10) # move
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(11) # move
        await self.bot.attack()
        await self.bot.move(1.0, 300)
        await self.bot.interact(wait_for_ready=True)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(3) # move
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.2, 800)
        await self.bot.move(0.5, 2300)
        await self.bot.move(1.85, 1500)
        await self.bot.interact()
        await self.bot.move(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.75, 2700)
        await self.bot.move(1.0, 1100)
        await self.bot.action_button()
        await self.bot.move(1.0, 1500)
        await self.bot.attack_technique(4) # move
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(9) # move
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.5, 600)
        await self.bot.move(0.0, 400)
        await self.bot.move(1.5, 300)
        await self.bot.action_button()
        await self.bot.move(1.5, 1500)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(1.7, 1500)
        await self.bot.attack_technique(4) # items
    async def path_13(self):
        logger_set_path(self.map, 13)
        await self.bot.use_teleporter(1241/2400, 520/1080, move_x=0, move_y=5, corner='topright', confirm=True) # Platinum Guest Room
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(4) # move
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(28) # move
        await self.bot.sleep(3)
        await self.bot.attack_technique(11) # move
        await self.bot.sleep(3)
        await self.bot.move(1.25, 800)
        await self.bot.move(1.5, 2700)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.move(0.9, 1000)
        await self.bot.move(1.0, 2000)
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.25, 400)
        await self.bot.move(0.5, 7300) 
        await self.bot.attack() # items
        await self.bot.move(1.75, 300)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(0.75, 4000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.restore_tp(item='punitive_energy', n=1) # +4TP
        await self.bot.move(1.8, 3600)
        await self.bot.move(1.5, 1900)
        await self.bot.interact()
        await self.bot.move(1.5, 1900)
        await self.bot.move(1.3, 2000)
        await self.bot.action_button()
        await self.bot.move(1.5, 2000)
        await self.bot.move(0.0, 1800)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.4, 1900)
        await self.bot.action_button()
        await self.bot.move(1.5, 1200)
        await self.bot.move(1.0, 2000)
        await self.bot.move(1.3, 1300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.5, 2000)
        await self.bot.move(1.0, 1000)
        await self.bot.attack() # items
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.3, 1500)
        await self.bot.move(1.5, 1200)
        for _ in range(4): # -1TP, roamer
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(1.75, 3000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.7, 1000)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(12) # move
        await self.bot.attack()
        await self.bot.interact()
        await self.bot.move(0.7, 1000)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.5, 600)
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(5) # move
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(4) # move
        await self.bot.move(0.1, 500)
        await self.bot.attack_technique(3) # items
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.9, 2000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.9, 600)
        await self.bot.action_button()
        await self.bot.move(1.5, 1500)
        await self.bot.move(1.1, 500)
        await self.bot.attack_technique(4) # +2TP
    async def path_14(self):
        logger_set_path(self.map, 14)
        await self.bot.use_teleporter(748/2400, 533/1080, move_x=0, move_y=3, corner='topleft') # Monitoring Room
        await self.bot.move(0.7, 2400)
        await self.bot.move(1.0, 8500)
        await self.bot.attack() # items
        await self.bot.move(0.0, 8100)
        await self.bot.move(0.2, 4000)
        await self.bot.move(0.0, 1500)
        await self.bot.move(1.9, 500)
        await self.bot.attack() # items
        await self.bot.move(0.4, 600)
        await self.bot.move(0.0, 6000)
        await self.bot.move(0.3, 1000)
        await self.bot.move(0.2, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.4, 800)
        await self.bot.move(1.7, 800)
        await self.bot.attack() # items
        await self.bot.move(1.4, 1000)
        await self.bot.move(1.5, 6000)
        await self.bot.move(1.2, 700)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(1.9, 300)
        await self.bot.attack_technique(3) # -1TP, roamer
        await self.bot.move(0.2, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.restore_tp(item='trick_snack', n=1) # +2TP
    async def path_15(self):
        logger_set_path(self.map, 15)
        await self.bot.use_teleporter(935/2400, 587/1080, move_x=0, move_y=5, corner='topleft') # VIP Lounge Corridor
        await self.bot.move(1.25, 1200)
        await self.bot.move(1, 5500)
        await self.bot.move(0.9, 2000)
        await self.bot.move(1.0, 3000)
        await self.bot.move(1.1, 2400)
        await self.bot.sleep(2)
        await self.bot.move(1.0, 6500)
        await self.bot.sleep(2)
        await self.bot.move(1.1, 600)
        await self.bot.move(1.0, 6400)
        await self.bot.move(0.5, 600)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.move(1.4, 2000)
        await self.bot.move(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.4, 4000)
        await self.bot.move(0.0, 4800)
        await self.bot.move(0.5, 900)
        await self.bot.attack() # items
        await self.bot.move(1.55, 1800)
        await self.bot.interact()
        await self.bot.move(0.5, 4500)
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.2, 1000)
        await self.bot.action_button()
        await self.bot.move(1.0, 3500)
        await self.bot.move(1.4, 1200)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(1.1, 2000)
        await self.bot.restore_tp(item='punitive_energy', n=1) # +4TP
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.3, 3500)
        await self.bot.move(0.0, 3000)
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.3, 1100)
        await self.bot.move(1.5, 4100)
        await self.bot.interact()
        await self.bot.move(1.52, 3000)
        await self.bot.action_button()
        await self.bot.move(1.5, 2100)
        await self.bot.move(1.0, 2500)
        await self.bot.move(0.5, 2100)
        await self.bot.action_button()
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.7, 900)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(2) # -1TP, spawn roamer
        await self.bot.move(1.3, 2000)
        await self.bot.move(1.4, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.4, 1500)
        await self.bot.move(0.5, 3900)
        for _ in range(5): # items -1TP
            await self.bot.move(1.9, 300)
            await self.bot.attack_technique(1)
        await self.bot.move(0.4, 2000) # move to top right corner
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.1, 600)
        await self.bot.interact()
        await self.bot.move(1.0, 2500)
        await self.bot.move(0.5, 2300)
        await self.bot.action_button()
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(0.7, 500)
        await self.bot.attack_technique(5) # items
        await self.bot.move(1.4, 500)
        await self.bot.attack_technique(3) # -1TP
    async def path_16(self):
        logger_set_path(self.map, 16)
        await self.bot.switch_map(y_list=1011/1080, world='penacony', scroll_down=False, # Platinum Guest Room
                                    x=1241/2400, y=520/1080, corner='topright', move_x=0, move_y=5, confirm=True)
        await self.bot.move(0.5, 2600)
        await self.bot.move(1.0, 12900)
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.25, 1500)
        await self.bot.move(0.6, 3000)
        await self.bot.move(0.5, 3100)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.3, 3000)
        await self.bot.move(0.5, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.0, 600)
        await self.bot.move(0.5, 1000)
        await self.bot.move(0.9, 300)
        await self.bot.attack_technique(10) # -2TP
    async def path_17(self):
        logger_set_path(self.map, 17)
        await self.bot.switch_map(y_list=1011/1080, world='penacony', scroll_down=False, # Monitoring Room
                                    x=748/2400, y=533/1080, corner='topleft', move_x=0, move_y=3)
        await self.bot.move(1.5, 6300)
        await self.bot.interact()
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.0, 3500)
        await self.bot.move(0.5, 4100)
        await self.bot.interact()
        await self.bot.move(0.5, 3500)
        await self.bot.move(1.0, 7000)
        await self.bot.move(0.9, 1100)
        await self.bot.move(1.0, 100)
        await self.bot.action_button()
        await self.bot.move(1.0, 1400)
        await self.bot.move(1.52, 1400)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.9, 300)
        await self.bot.attack_technique(5) # move
        await self.bot.move(0.6, 3000)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.5, 800)
        await self.bot.move(0.0, 400)
        await self.bot.action_button()
        await self.bot.move(0.5, 1500)
        await self.bot.attack_technique(12) # move
        await self.bot.move(0.75, 2500)
        await self.bot.posfix(0.75, 500)
        await self.bot.interact()
        await self.bot.move(0.0, 700)
        await self.bot.move(0.5, 1500)
        await self.bot.action_button()
        await self.bot.move(0.5, 1500)
        await self.bot.move(1.9, 2400)
        await self.bot.move(1.5, 700)
        await self.bot.action_button()
        await self.bot.move(1.5, 1500)
        await self.bot.move(0.0, 1000)
        await self.bot.move(0.4, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(4) # -1TP, roamer
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(4)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(6)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(5)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(8)
    async def path_18(self):
        logger_set_path(self.map, 18)
        # TODO: one more room


