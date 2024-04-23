from logger import logger, logger_set_path
from sys import exit


class Central_Starskiff_Haven:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Central Starskiff Haven')
        logger.info('---')
        await self.bot.switch_map(y_list=388/1080, world='the_xianzhou_luofu', scroll_down=False,
                                    x=803/2400, y=654/1080, corner='topleft', move_x=0, move_y=0) # Starskiff Jetty
        await self.bot.movepi(0.0, 6000)
        await self.bot.movepi(1.5, 7200)
        await self.bot.movepi(1.7, 1000)
    async def shop_salesby(self):
        logger_set_path('Shop Salesby')
        await self.bot.chat_initiate()
        for _ in range(2):
            await self.bot.chat_advance()
        await self.bot.action_tap(int(self.bot.xy.width*1654/2400), int(self.bot.xy.height*484/1080))
        await self.bot.sleep(1)
        await self.bot.chat_advance()
        await self.bot.buy_item('gaseous_liquid')
        await self.bot.buy_item('seed')
        await self.bot.shop_exit()
        await self.bot.craft_item('trick_snack')

class Cloudford:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Cloudford')
        logger.info('---')
        await self.bot.switch_map(y_list=500/1080, world='the_xianzhou_luofu', scroll_down=False,
                                    x=925/2400, y=663/1080, corner='topleft', move_x=0, move_y=5) # Trove of Verdure
        await self.bot.movepi(1.75, 2300)
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(1.75, 2400)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 10000)
        await self.bot.movepi(1.7, 4000)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(0.62, 1500)
        await self.bot.attack_technique(3) # -1TP
        exit() # check: get TP & items
        await self.bot.movepi(1.0, 4000)
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.5, 1900)
        await self.bot.movepi(1.0, 1700)
        await self.bot.attack() # +2TP
    async def path_1(self): # roamer
        logger_set_path(1)
        await self.bot.use_teleporter(813/2400, 349/1080, move_x=0, move_y=0, corner='botright') # Bud of Memories
        await self.bot.movepi(1.65, 2900)
        await self.bot.movepi(1.8, 400)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(1.25, 500)
        await self.bot.attack_technique(3, wait=False) # -1TP
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(2)
    async def path_2(self): # roamer
        logger_set_path(2)
        await self.bot.use_teleporter(1129/2400, 642/1080, move_x=0, move_y=1, corner='topright') # Cargo Lane
        await self.bot.movepi(0.54, 5300)
        await self.bot.attack() # items
        await self.bot.movepi(0.3, 3500)
        await self.bot.movepi(0.0, 3000)
        await self.bot.movepi(1.88, 2900)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.5, 2600)
        await self.bot.attack() # items
        await self.bot.movepi(0.55, 2700)
        for _ in range(2): # -2TP
            await self.bot.movepi(0.25, 300)
            await self.bot.attack_technique(2, wait=False)
        for _ in range(3):
            await self.bot.movepi(0.0, 300)
            await self.bot.attack_technique(2, wait=False)
        for _ in range(3):
            await self.bot.movepi(1.1, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.attack_technique(1)
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(925/2400, 663/1080, move_x=0, move_y=5, corner='topleft') # Trove of Verdure
        await self.bot.movepi(0.4, 8000)
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.37, 2300)
        await self.bot.attack() # +2TP
    async def path_4(self): # roamer
        logger_set_path(4)
        await self.bot.use_teleporter(925/2400, 663/1080, move_x=0, move_y=5, corner='topleft') # Trove of Verdure
        exit() # TODO: make sure to get the TP
        await self.bot.movepi(0.75, 2100)
        await self.bot.movepi(1.0, 7500)
        await self.bot.attack_technique(2, wait=False) # -1TP
        await self.bot.movepi(0.0, 2500)
        await self.bot.movepi(1.7, 1000)
        await self.bot.movepi(1.9, 1000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.movepi(0.75, 500)
        await self.bot.movepi(1.0, 1000)
        for _ in range(2): # -1TP
            await self.bot.movepi(1.0, 300)
            await self.bot.attack_technique(3, wait=False)
        await self.bot.movepi(0.7, 300)
        await self.bot.attack_technique(3) # +2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(973/2400, 532/1080, move_x=0, move_y=0, corner='botright') # Skiff Boarding Area
        await self.bot.movepi(0, 9900)
        await self.bot.movepi(1.5, 1900)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(0.5, 2500)
        await self.bot.movepi(0.75, 1900)
        await self.bot.movepi(1, 1500)
        await self.bot.attack_technique(7, wait=False) # -1TP
        await self.bot.movepi(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.75, 900)
        await self.bot.movepi(0, 3500)
        await self.bot.movepi(1.75, 400)
        await self.bot.movepi(0, 2900)
        await self.bot.attack() # +2TP
    async def path_6(self): # roamer
        logger_set_path(6)
        await self.bot.use_teleporter(813/2400, 349/1080, move_x=0, move_y=0, corner='botright') # Bud of Memories
        await self.bot.movepi(1.65, 1700)
        await self.bot.movepi(0.15, 3500)
        await self.bot.movepi(1.6, 1200)
        await self.bot.movepi(0.0, 200)
        await self.bot.attack_technique(3, wait=False) # -3TP
        await self.bot.movepi(1.3, 500)
        for _ in range(3):
            await self.bot.movepi(0.7, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.attack_technique(2)
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(1163/2400, 530/1080, move_x=0, move_y=0, corner='botright') # Shape of Icicle
        await self.bot.movepi(0.0, 1300)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.5, 1000)
        await self.bot.attack() # items
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(930/2400, 259/1080, move_x=0, move_y=0, corner='botright') # Path of Holy Hymn
        await self.bot.movepi(1.25, 1000)
        await self.bot.attack() # +2TP
        exit()
       
 
class Stargazer_Navalia:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Stargazer Navalia')
        logger.info('---')
        await self.bot.switch_map(y_list=630/1080, world='the_xianzhou_luofu', scroll_down=False,
                                    x=1240/2400, y=538/1080, corner='topright', move_x=0, move_y=0, confirm=True) # Astral Cottage
        await self.bot.movepi(0.25, 2500)
        await self.bot.movepi(0.16, 6000)
        await self.bot.movepi(0.27, 700)
        await self.bot.movepi(0.52, 400)
        await self.bot.movepi(1.05, 2000)
        await self.bot.attack_technique(2, wait=False) # -1TP
        await self.bot.movepi(0.25, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.3, 900)
        await self.bot.movepi(1.11, 5000)
        await self.bot.movepi(1.17, 2700)
        await self.bot.movepi(0.6, 2800)
        for _ in range(4): # -2TP
            await self.bot.movepi(0.2, 300)
            await self.bot.attack_technique(3, wait=False)
        for _ in range(3):
            await self.bot.movepi(1.2, 300)
            await self.bot.attack_technique(3, wait=False)
        await self.bot.attack_technique(1)
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(1240/2400, 538/1080, move_x=0, move_y=0, corner='topright', confirm=True) # Astral Cottage
        await self.bot.movepi(0.25, 2500)
        await self.bot.movepi(0.16, 6000)
        await self.bot.movepi(0.27, 700)
        await self.bot.movepi(0.52, 400)
        await self.bot.movepi(1.05, 2200)
        await self.bot.movepi(1.07, 5000)
        await self.bot.movepi(1.17, 2900)
        await self.bot.movepi(0.62, 3000)
        await self.bot.movepi(0.84, 4300)
        await self.bot.movepi(0.9, 100)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.15, 3100)
        await self.bot.attack_technique(2, wait=False) # -1TP
        await self.bot.movepi(0.15, 1500)
        await self.bot.movepi(0.4, 1500)
        await self.bot.movepi(0.25, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.15, 4900)
        await self.bot.movepi(1.25, 300)
        await self.bot.attack_technique(2) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(1106/2400, 610/1080, move_x=0, move_y=0, corner='botright') # Shape of Doom
        await self.bot.movepi(1.5, 700)
        await self.bot.attack() # +2TP
        await self.bot.posfix(1.5, 1000)
        await self.bot.movepi(0.3, 500)
        await self.bot.movepi(0.00, 5400)
        await self.bot.movepi(1.7, 900)
        await self.bot.movepi(0.00, 2400)
        for _ in range(3): # -1TP +2TP
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.7, 1000)
        await self.bot.movepi(0.0, 4000)
        await self.bot.movepi(0.3, 300)
        await self.bot.movepi(0.0, 4000)
        await self.bot.movepi(0.1, 900)
        await self.bot.attack() # items
        await self.bot.movepi(0.1, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.25, 900)
        for _ in range(6): # -2TP
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.75, 3000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.movepi(0.7, 1700)
        await self.bot.movepi(0.5, 4900)
        await self.bot.movepi(0.0, 4200)
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(1.0, 500)
        await self.bot.attack_technique(2)
    async def path_3(self): # roamer
        logger_set_path(3)
        await self.bot.use_teleporter(768/2400, 696/1080, move_x=0, move_y=0, corner='topright') # Path of Conflagration
        await self.bot.movepi(1.7, 3300)
        await self.bot.movepi(1.9, 300)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(0.4, 1800)
        await self.bot.attack() # +2TP
    async def path_4(self): # roamer
        logger_set_path(4)
        await self.bot.use_teleporter(855/2400, 184/1080, move_x=0, move_y=0, corner='botleft') # Ship Nursery - The Budding
        await self.bot.movepi(0.7, 800)
        await self.bot.movepi(0.5, 900)
        await self.bot.movepi(0.00, 2500)
        for _ in range(2): # -1TP
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(2, wait=False)
        for _ in range(2):
            await self.bot.movepi(1.0, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(2, wait=False)
        for _ in range(2):
            await self.bot.movepi(0.0, 300)
            await self.bot.attack_technique(2, wait=False)
        for _ in range(2):
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.attack_technique(1)
    async def path_5(self): # roamer
        logger_set_path(5)
        await self.bot.use_teleporter(855/2400, 184/1080, move_x=0, move_y=0, corner='botleft') # Ship Nursery - The Budding
        await self.bot.movepi(0.7, 800)
        await self.bot.movepi(0.5, 900)
        await self.bot.movepi(0.00, 2500)
        await self.bot.movepi(0.5, 5000)
        await self.bot.movepi(0.3, 1800)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.25, 1900)
        await self.bot.movepi(1.0, 5500)
        await self.bot.movepi(0.9, 1500)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.4, 1500)
        await self.bot.attack_technique(4, wait=False) # -3TP
        await self.bot.movepi(0.3, 300)
        await self.bot.attack_technique(4)
    async def path_6(self): # roamer
        logger_set_path(6)
        await self.bot.use_teleporter(855/2400, 184/1080, move_x=0, move_y=0, corner='botleft') # Ship Nursery - The Budding
        await self.bot.movepi(1.5, 700)
        await self.bot.movepi(0.00, 2300)
        await self.bot.movepi(0.5, 800)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.5, 800)
        await self.bot.movepi(1.9, 500)
        await self.bot.movepi(0.00, 8300)
        await self.bot.attack_technique(4, wait=False) # -2TP
        await self.bot.movepi(0.25, 1000)
        await self.bot.movepi(1.25, 1000)
        await self.bot.movepi(1.5, 500)
        await self.bot.attack_technique(10) # -1TP


class Divination_Commission:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Divination Commission')
        logger.info('---')
        await self.bot.switch_map(y_list=447/1080, world='the_xianzhou_luofu', scroll_down=True,
                                    x=848/2400, y=524/1080, corner='botright', move_x=0, move_y=0) # Bud of Aether
        await self.bot.movepi(1.25, 2600)
        await self.bot.attack_technique(6) # -1TP
        await self.bot.restore_tp(n=1) # +2TP
    async def path_1(self): # roamer
        logger_set_path(1)
        await self.bot.use_teleporter(1089/2400, 284/1080, corner='botright', move_x=0, move_y=0) # Conclave Hall
        await self.bot.movepi(1.5, 23000)
        await self.bot.movepi(1.25, 2000)
        await self.bot.attack_technique(3, wait=False) # -2TP
        await self.bot.movepi(1.0, 2000)
        await self.bot.movepi(0.75, 1000)
        await self.bot.movepi(0.5, 2000)
        await self.bot.restore_tp(n=1) # +2TP
        await self.bot.posfix(0.5, 1000)
        await self.bot.movepi(0.0, 500)
        await self.bot.movepi(0.5, 500)
        await self.bot.movepi(1.0, 2900)
        for _ in range(3): # -3TP
            await self.bot.movepi(0.75, 300)
            await self.bot.attack_technique(3, wait=False)
        for _ in range(4):
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(3, wait=False)
        for _ in range(3):
            await self.bot.movepi(0.4, 300)
            await self.bot.attack_technique(3, wait=False)
        for _ in range(4):
            await self.bot.movepi(1.4, 300)
            await self.bot.attack_technique(3, wait=False)
        await self.bot.attack_technique(2)
        await self.bot.movepi(1.0, 2000)
        await self.bot.movepi(1.5, 2000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.3, 4500)
        await self.bot.movepi(0.0, 3500)
        await self.bot.movepi(1.7, 1600)
        await self.bot.movepi(0.0, 3000)
        await self.bot.movepi(0.3, 1500)
        await self.bot.movepi(0.0, 3000)
        await self.bot.movepi(0.0, 1400)
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.35, 1400)
        await self.bot.movepi(1.5, 3200)
        await self.bot.movepi(1.76, 2000)
        await self.bot.attack_technique(3)
    async def path_2(self): # roamer
        logger_set_path(2)
        await self.bot.use_teleporter(743/2400, 586/1080, corner='topleft', move_x=0, move_y=0) # Spatial Terminal
        await self.bot.movepi(0.4, 1500)
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(0.7, 1200)
        await self.bot.movepi(0.9, 300)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.12, 1900)
        await self.bot.attack() # items
        await self.bot.movepi(0.25, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.3, 1500)
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(1.3, 800)
        await self.bot.movepi(1.5, 2900)
        await self.bot.movepi(1.75, 4500)
        await self.bot.attack_technique(4, wait=False) # -1TP
        await self.bot.movepi(0.6, 500)
        await self.bot.attack_technique(6) # -1TP
        await self.bot.restore_tp(n=1) # +2TP
    async def path_3(self): # roamer
        logger_set_path(3)
        await self.bot.use_teleporter(743/2400, 586/1080, corner='topleft', move_x=0, move_y=0) # Spatial Terminal
        await self.bot.movepi(1.5, 3700)
        await self.bot.movepi(1.75, 5800)
        await self.bot.movepi(0.0, 1500)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.0, 1900)
        await self.bot.movepi(1.25, 2800)
        await self.bot.movepi(0.75, 300)
        await self.bot.attack_technique(2, wait=False) # -1TP
        for _ in range(2): # -1TP
            await self.bot.movepi(1.25, 300)
            await self.bot.attack_technique(2, wait=False)
        for _ in range(2):
            await self.bot.movepi(1.75, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.attack_technique(1)
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(743/2400, 586/1080, corner='topleft', move_x=0, move_y=0) # Spatial Terminal
        await self.bot.movepi(1.5, 3700)
        await self.bot.movepi(1.75, 11300)
        await self.bot.movepi(0.0, 4000)
        await self.bot.movepi(0.25, 1500)
        await self.bot.movepi(0.0, 2000)
        await self.bot.movepi(1.75, 1500)
        await self.bot.movepi(0.0, 3000)
        await self.bot.movepi(0.25, 3200)
        await self.bot.movepi(0.0, 1500)
        await self.bot.movepi(0.2, 300)
        await self.bot.attack_technique(3)
        await self.bot.restore_tp(n=1) # +2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(445/2400, 720/1080, move_x=0, move_y=0, corner='botright') # Fortuna Augurstead
        await self.bot.movepi(0.5, 4000)
        await self.bot.movepi(0.7, 1500)
        await self.bot.attack() # items
        await self.bot.movepi(1.1, 1600)
        await self.bot.movepi(0.75, 500)
        await self.bot.attack_technique(5, wait=False) # -1TP
        await self.bot.movepi(1.5, 500)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.restore_tp(n=1) # +2TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(848/2400, 524/1080, move_x=0, move_y=0, corner='botright') # Bud of Aether
        await self.bot.movepi(1.2, 8000)
        await self.bot.movepi(1.0, 3500)
        await self.bot.movepi(0.63, 5500)
        await self.bot.movepi(0.0, 1400)
        await self.bot.attack_technique(3, wait=False) # -2TP
        await self.bot.movepi(0.65, 300)
        await self.bot.attack_technique(7, wait=False) # -1TP
        await self.bot.movepi(1.2, 300)
        await self.bot.attack_technique(6)
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(848/2400, 524/1080, move_x=0, move_y=0, corner='botright') # Bud of Aether
        await self.bot.movepi(1.2, 8000)
        await self.bot.movepi(1.0, 3500)
        await self.bot.movepi(0.63, 5500)
        await self.bot.movepi(1.23, 2400)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.4, 1000)
        await self.bot.posfix(1.4, 1000)
        await self.bot.movepi(0.65, 2100)
        await self.bot.movepi(1.17, 11000)
        await self.bot.attack_technique(5) # -1TP


class Artisanship_Commission:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Artisanship Commission')
        logger.info('---')
        await self.bot.switch_map(y_list=567/1080, world='the_xianzhou_luofu', scroll_down=True,
                                    x=933/2400, y=530/1080, corner='topright', move_x=0, move_y=4) # Passage of the Finery Foundry
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(0.0, 6200)
        await self.bot.movepi(0.25, 700)
        await self.bot.movepi(0.1, 500)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(0.0, 500)
        await self.bot.attack_technique(2, wait=False) # -1TP
        await self.bot.movepi(1.25, 700)
        await self.bot.attack_technique(3, wait=False) # -1TP
        await self.bot.movepi(1.25, 300)
        await self.bot.attack_technique(4) # +2TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(933/2400, 530/1080, corner='topright', move_x=0, move_y=4) # Passage of the Finery Foundry
        await self.bot.movepi(0.5, 4100)
        await self.bot.movepi(0.25, 2500)
        await self.bot.attack() # items
        await self.bot.movepi(1.0, 1800)
        await self.bot.movepi(0.5, 3500)
        await self.bot.movepi(1.0, 1000)
        await self.bot.sleep(1.5)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(804/2400, 487/1080, corner='topleft', move_x=0, move_y=5) # Shape of Puppetry
        await self.bot.movepi(1.22, 2100)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(933/2400, 530/1080, corner='topright', move_x=0, move_y=4) # Passage of the Finery Foundry
        await self.bot.movepi(0.5, 10900)
        await self.bot.movepi(0.0, 3900)
        await self.bot.movepi(0.55, 2300)
        await self.bot.movepi(0.8, 150)
        await self.bot.attack() # items
        await self.bot.movepi(0.25, 500)
        await self.bot.movepi(0.5, 2800)
        await self.bot.movepi(0.0, 2200)
        await self.bot.attack() # items
        await self.bot.movepi(1.1, 500)
        await self.bot.movepi(1.5, 100)
        await self.bot.attack_technique(4) # -1TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(893/2400, 833/1080, corner='topleft', move_x=0, move_y=0) # Passage to the Sapientia Academe
        await self.bot.movepi(0.5, 4400)
        await self.bot.movepi(0.75, 1700)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.2, 2000)
        await self.bot.movepi(0.5, 300)
        for _ in range(5): # -2TP
            await self.bot.movepi(0.0, 300)
            await self.bot.attack_technique(3, wait=False)
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(0.0, 1500)
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.75, 1000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.movepi(1.0, 1000)
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.0, 4500)
        await self.bot.movepi(1.5, 750)
        await self.bot.movepi(1.72, 2800)
        await self.bot.attack_technique(2, wait=False) # -1TP
        await self.bot.movepi(0.1, 300)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.restore_tp(n=2) # +4TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(893/2400, 833/1080, corner='topleft', move_x=0, move_y=0) # Passage to the Sapientia Academe
        await self.bot.movepi(1.25, 3000)
        await self.bot.movepi(1.0, 8000)
        await self.bot.movepi(0.75, 200)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(1.5, 500)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.restore_tp(n=1) # +2TP
        await self.bot.movepi(1.25, 2000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.25, 500)
        await self.bot.movepi(0.5, 600)
        await self.bot.movepi(1.0, 5000)
        await self.bot.movepi(0.45, 2500)
        for _ in range(2): # -2TP
            await self.bot.movepi(1.0, 300)
            await self.bot.attack_technique(3, wait=False)
        await self.bot.movepi(0.6, 1000)
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.75, 2000)
        for _ in range(3): # +2TP
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(3, wait=False)
        await self.bot.movepi(0.6, 3000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.6, 1000)
        await self.bot.movepi(1.5, 8200)
        for _ in range(4): # -1TP
            await self.bot.movepi(1.0, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.0, 2000)
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(0.0, 2000)
        await self.bot.movepi(0.5, 1000)
        await self.bot.attack() # items
        await self.bot.movepi(0.25, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.2, 1500)
        await self.bot.movepi(1.0, 3300)
        await self.bot.movepi(0.5, 2500)
        await self.bot.movepi(0.83, 900)
        await self.bot.attack() # items
        await self.bot.movepi(0.5, 900)
        await self.bot.movepi(1.0, 2000)
        await self.bot.movepi(0.25, 2000)
        await self.bot.restore_tp(n=1) # +2TP
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.25, 1500)
        await self.bot.movepi(1.0, 3000)
        for _ in range(2): # -1TP
            await self.bot.movepi(1.0, 300)
            await self.bot.attack_technique(5, wait=False)
        for _ in range(2): # -1TP
            await self.bot.movepi(0.75, 300)
            await self.bot.attack_technique(2, wait=False)
        for _ in range(2): # -1TP
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.4, 4000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.2, 3100)
        await self.bot.attack() # +2 TP
    async def path_6(self): # roamer
        logger_set_path(6)
        await self.bot.use_teleporter(854/2400, 418/1080, corner='botright', move_x=0, move_y=4) # Creation Furnace
        await self.bot.movepi(1.0, 1100)
        await self.bot.movepi(1.5, 900)
        await self.bot.movepi(0.00, 1800)
        await self.bot.movepi(0.5, 2500)
        await self.bot.movepi(0.00, 3300)
        await self.bot.movepi(1.5, 3000)
        await self.bot.movepi(1.75, 1200)
        await self.bot.attack_technique(2, wait=False) # -1TP
        for _ in range(2): # -1TP
            await self.bot.movepi(0.25, 300)
            await self.bot.attack_technique(3, wait=False)
        for _ in range(2): # -1TP
            await self.bot.movepi(0.0, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.0, 500)
        await self.bot.attack_technique(10)
        await self.bot.restore_tp(n=1) # +2TP
    async def path_7(self): # roamer
        logger_set_path(7)
        await self.bot.use_teleporter(854/2400, 418/1080, corner='botright', move_x=0, move_y=4) # Creation Furnace
        await self.bot.movepi(1.0, 1100)
        await self.bot.movepi(1.5, 900)
        await self.bot.movepi(0.0, 1900)
        await self.bot.movepi(0.5, 2300)
        await self.bot.movepi(0.25, 2500)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.5, 1600)
        await self.bot.movepi(0.0, 1800)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.25, 600)
        await self.bot.movepi(1.5, 3000)
        await self.bot.movepi(1.75, 1000)
        await self.bot.movepi(0.25, 4500)
        await self.bot.movepi(0.5, 5700)
        await self.bot.movepi(1.05, 1000)
        await self.bot.movepi(1.25, 100)
        await self.bot.attack_technique(3, wait=False) # -2TP
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(2, wait=False) # -1TP
        await self.bot.movepi(0.4, 300)
        await self.bot.attack_technique(4)


class Fyxestroll_Garden:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Fyxestroll Garden')
        logger.info('---')
        await self.bot.switch_map(y_list=688/1080, world='the_xianzhou_luofu', scroll_down=True,
                                    x=412/2400, y=603/1080, move_x=0, move_y=0, corner='botright', confirm=False) # Bud of Abundance
        await self.bot.movepi(1.49, 3900)
        await self.bot.attack_technique(2) # -1TP
    async def path_1(self): # roamer
        logger_set_path(1)
        await self.bot.use_teleporter(697/2400, 153/1080, move_x=0, move_y=0) # Path of Darkness
        await self.bot.movepi(1.75, 2100)
        await self.bot.movepi(0.05, 2800)
        await self.bot.movepi(1.8, 2500)
        await self.bot.attack_technique(5) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(510/2400, 423/1080, corner='botleft', move_x=0, move_y=0) # Shape of Perdition
        await self.bot.movepi(0.95, 2500)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(697/2400, 153/1080, move_x=0, move_y=0) # Path of Darkness
        await self.bot.movepi(1.75, 2100)
        await self.bot.movepi(0.05, 2800)
        await self.bot.movepi(1.8, 2500)
        await self.bot.movepi(0.224, 4100)
        await self.bot.movepi(0.61, 700)
        await self.bot.attack_technique(4) # -1TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(697/2400, 153/1080, move_x=0, move_y=0) # Path of Darkness
        await self.bot.movepi(1.8, 2000)
        await self.bot.attack() # +2TP
        await self.bot.sleep(0.5)
        await self.bot.movepi(0.01, 2800)
        await self.bot.movepi(1.8, 2300)
        await self.bot.movepi(0.23, 6000)
        await self.bot.movepi(1.95, 700)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.restore_tp(n=1) # +2TP
    async def path_5(self): # roamer
        logger_set_path(5)
        await self.bot.use_teleporter(579/2400, 368/1080, move_x=1, move_y=2) # Locufox Forest Backdoor
        await self.bot.movepi(1.5, 4400)
        await self.bot.movepi(1.95, 600)
        await self.bot.attack_technique(3, wait=False) # -2TP
        await self.bot.movepi(1.0, 1000)
        await self.bot.movepi(1.2, 500)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.restore_tp(n=1) # +2TP
    async def path_6(self):
        logger_set_path(6) # roamer
        await self.bot.use_teleporter(412/2400, 603/1080, move_x=0, move_y=0)  # Bud of Abundance
        await self.bot.movepi(0.9, 4000)
        await self.bot.movepi(1.2, 3000)
        await self.bot.attack_technique(8) # -1TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(412/2400, 603/1080, move_x=0, move_y=0)  # Bud of Abundance
        await self.bot.movepi(1.47, 5000)
        await self.bot.movepi(1.2, 2000)
        await self.bot.movepi(0.9, 1500)
        await self.bot.movepi(1.12, 2300)
        await self.bot.attack() # +2TP
        await self.bot.sleep(0.5)
        await self.bot.movepi(1.2, 1500)
        await self.bot.movepi(0.7, 1000)
        await self.bot.attack_technique(5) # -2TP


class Alchemy_Commission:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Alchemy Comission')
        logger.info('---')
        await self.bot.switch_map(y_list=810/1080, world='the_xianzhou_luofu', scroll_down=True,
                                    x=867/2400, y=438/1080, corner='topleft', move_x=0, move_y=6) # Elixir Research Terrace
        await self.bot.movepi(0.5, 6900)
        await self.bot.movepi(0.0, 3600)
        await self.bot.movepi(1.5, 3700)
        await self.bot.movepi(0.0, 4200)
        await self.bot.attack_technique(2) # -1TP
    async def path_1(self): # roamer
        logger_set_path(1)
        await self.bot.use_teleporter(659/2400, 363/1080, corner='botright', move_x=0, move_y=0) # Cavern of Corrosion
        await self.bot.movepi(1.5, 2800)
        await self.bot.movepi(1.2, 1600)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.75, 2000)
        for _ in range(3): # -1TP
            await self.bot.movepi(1.25, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(0.25, 1000)
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.5, 600)
        await self.bot.movepi(1.25, 3500)
        await self.bot.attack_technique(6) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(583/2400, 241/1080, corner='botright', move_x=0, move_y=3) # Bud of Nihility
        await self.bot.movepi(1.0, 1500)
        await self.bot.movepi(0.5, 4200)
        await self.bot.movepi(0.7, 1800)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(0.8, 1900)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(0.0, 1000)
        await self.bot.movepi(1.9, 2000)
        await self.bot.movepi(1.4, 1000)
        await self.bot.movepi(1.5, 6900)
        await self.bot.movepi(0.0, 4800)
        await self.bot.movepi(1.8, 700)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(583/2400, 241/1080, corner='botright', move_x=0, move_y=3) # Bud of Nihility
        exit() # check for kill
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 3100)
        await self.bot.movepi(1.0, 5200)
        await self.bot.movepi(1.5, 2200)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(1.2, 2500)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(0.75, 500) # -1TP
        await self.bot.movepi(1.0, 300)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(3, wait=False)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(4, wait=False)
        await self.bot.movepi(1.7, 300)
        await self.bot.attack_technique(1, wait=False)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(12)
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(854/2400, 689/1080, corner='topright', move_x=0, move_y=6, confirm=True) # Healer's Market
        await self.bot.movepi(1.4, 4600)
        await self.bot.movepi(1.9, 2100)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.2, 1000)
        await self.bot.movepi(0.9, 2800)
        await self.bot.movepi(1.4, 9300)
        await self.bot.movepi(1.9, 4700)
        await self.bot.attack_technique(8) # -2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(1355/2400, 694/1080, corner='topright', move_x=0, move_y=8) # Shape of Celestial
        await self.bot.movepi(1.66, 2500)
        await self.bot.attack() # +2TP
        await self.bot.restore_tp(n=1) # +2TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(854/2400, 689/1080, corner='topright', move_x=0, move_y=6, confirm=True) # Healer's Market
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(0.75, 6700)
        await self.bot.movepi(0.98, 6000)
        await self.bot.attack() # items
        await self.bot.movepi(1.2, 4000)
        await self.bot.movepi(1.1, 4500)
        await self.bot.attack_technique(5, wait=False) # -2TP
        await self.bot.movepi(1.6, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(866/2400, 517/1080, corner='topleft', move_x=0, move_y=5) # Elixir Research Terrace
        await self.bot.movepi(0.5, 10300)
        await self.bot.movepi(0.75, 2000)
        await self.bot.movepi(1.1, 2200)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.0, 600)
        await self.bot.movepi(1.5, 4400)
        await self.bot.movepi(1.0, 1300)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(3, wait=False)
        await self.bot.movepi(0.25, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(1003/2400, 595/1080, corner='topleft', move_x=0, move_y=3) # Aureate Elixir Furnace
        await self.bot.movepi(0.8, 700)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.1, 500)
        await self.bot.movepi(0.55, 2200)
        await self.bot.movepi(0.34, 2300)
        await self.bot.movepi(0.2, 1300)
        await self.bot.movepi(0.5, 1200)
        await self.bot.movepi(0.35, 2000)
        await self.bot.movepi(0.14, 2800)
        await self.bot.movepi(1.6, 900)
        await self.bot.attack_technique(1, wait=False) # -1TP
        for _ in range(2): # -1TP
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(2, wait=False)
        for _ in range(2):
            await self.bot.movepi(0.25, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.25, 1000)
        await self.bot.movepi(0.5, 1000)
        await self.bot.movepi(0.25, 2000)
        await self.bot.restore_tp(n=1) # +2TP
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.6, 1900)
        await self.bot.movepi(0.1, 2500)
        await self.bot.movepi(1.8, 2100)
        await self.bot.movepi(1.4, 800)
        await self.bot.attack_technique(1, wait=False) # -1TP
        for _ in range(2): # -1TP
            await self.bot.movepi(0.4, 300)
            await self.bot.attack_technique(2, wait=False)
        for _ in range(2):
            await self.bot.movepi(1.9, 300)
            await self.bot.attack_technique(3, wait=False)
        for _ in range(2):
            await self.bot.movepi(1.4, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(0.25, 5000)
        await self.bot.restore_tp(n=1) # +2TP
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.15, 3400)
        await self.bot.movepi(1.35, 3000)
        await self.bot.movepi(1.55, 5000)
        await self.bot.movepi(1.25, 3000)
        await self.bot.movepi(1.1, 2000)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(1.6, 300)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(0.6, 300)
        await self.bot.attack_technique(8)


class Scalegorge_Waterscape:
    def __init__(self, bot):
        self.bot = bot
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Scalegorge Waterscape')
        logger.info('---')
        await self.bot.switch_map(y_list=928/1080, world='the_xianzhou_luofu', scroll_down=True,
                                    x=966/2400, y=379/1080, corner='botright', move_x=0, move_y=0) # Dragonvista Rain Hall
        await self.bot.movepi(1.5, 4500)
        await self.bot.movepi(0.0, 2000)
        await self.bot.movepi(0.5, 3300)
        await self.bot.movepi(0.0, 3900)
        await self.bot.attack_technique(3, wait=False) # -1TP
        await self.bot.movepi(1.75, 300)
        await self.bot.attack_technique(3, wait=False) # -1TP
        await self.bot.movepi(1.0, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_x(self):
        logger_set_path(1)
        await self.bot.use_teleporter(357/2400, 354/1080, move_x=0, move_y=0) # Ancient Sea Palace Ruins
        await self.bot.movepi(0.75, 900)
        await self.bot.attack() # items
        await self.bot.movepi(1.75, 1200)
        await self.bot.movepi(1.5, 8000)
        await self.bot.movepi(0.0, 1000)
        await self.bot.attack() # +2TP
    async def path_x(self): # roamer
        logger_set_path(2)
        await self.bot.use_teleporter(357/2400, 354/1080, move_x=0, move_y=0) # Ancient Sea Palace Ruins
        await self.bot.movepi(1.0, 5600)
        await self.bot.movepi(1.5, 1300)
        await self.bot.movepi(1.0, 6400)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(0.75, 300)
        await self.bot.attack_technique(6, wait=False) # -1TP
        await self.bot.movepi(1.75, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_x(self):
        logger_set_path(3)
        await self.bot.use_teleporter(1433/2400, 659/1080, corner='topleft', move_x=0, move_y=0) # Palace Ruin Depths
        await self.bot.movepi(1.5, 6000)
        await self.bot.movepi(1.6, 300)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.5, 3900)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(1.5, 2900)
        await self.bot.movepi(1.13, 2800)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.75, 600)
        await self.bot.movepi(0.0, 2100)
        await self.bot.movepi(0.5, 2400)
        await self.bot.movepi(1.0, 6500)
        await self.bot.movepi(0.7, 1300)
        await self.bot.attack_technique(2, wait=False) # -1TP
        await self.bot.movepi(0.75, 1000)
        await self.bot.movepi(1.0, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.6, 1000)
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(1.0, 2100)
        await self.bot.movepi(1.5, 3000)
        for _ in range(3): # -1TP
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(3, wait=False)
        await self.bot.attack_technique(4)
        await self.bot.restore_tp(n=1) # +2TP
    async def path_x(self):
        logger_set_path(4)
        await self.bot.use_teleporter(1433/2400, 659/1080, corner='topleft', move_x=0, move_y=0) # Palace Ruin Depths
        await self.bot.movepi(1.5, 3000)
        await self.bot.movepi(0.0, 6500)
        await self.bot.attack_technique(2, wait=False) # -1TP
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_x(self):
        logger_set_path(5)
        await self.bot.use_teleporter(1433/2400, 659/1080, corner='topleft', move_x=0, move_y=0) # Palace Ruin Depths
        await self.bot.movepi(1.5, 3000)
        await self.bot.movepi(0.00, 3600)
        await self.bot.movepi(1.5, 6000)
        await self.bot.movepi(1.25, 500)
        for _ in range(3): # -1TP
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_x(self):
        logger_set_path(6)
        await self.bot.use_teleporter(1465/2400, 341/1080, corner='topleft', move_x=0, move_y=0) # Shape of Abomination
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(1.0, 1000)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.7, 1000)
        await self.bot.movepi(0.5, 1000)
        await self.bot.movepi(0.7, 5000)
        await self.bot.movepi(0.5, 500)
        await self.bot.movepi(0.75, 1000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.5, 1900)
        await self.bot.movepi(1.0, 4500)
        await self.bot.movepi(1.1, 900)
        await self.bot.attack_technique(2, wait=False) # -1TP
        await self.bot.movepi(1.6, 300)
        await self.bot.attack_technique(1, wait=False) # -1TP
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(4, wait=False)
        await self.bot.movepi(0.75, 5000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.75, 1000)
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(1.4, 1700)
        await self.bot.movepi(1.6, 1200)
        await self.bot.movepi(1.92, 500)
        await self.bot.attack() # +2TP
    async def path_x(self): # roamer
        logger_set_path(7)
        await self.bot.use_teleporter(909/2400, 690/1080, corner='topleft', move_x=0, move_y=0) # Divine Seed
        await self.bot.movepi(1.0, 2000)
        await self.bot.movepi(1.1, 2500)
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.0, 2000)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.0, 2100)
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(1.0, 8500)
        await self.bot.movepi(1.25, 2300)
        await self.bot.movepi(1.0, 1600)
        await self.bot.movepi(0.75, 3000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.75, 1000)
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.6, 2000)
        await self.bot.movepi(0.5, 4100)
        await self.bot.attack_technique(2, wait=False)
        await self.bot.movepi(0.75, 300)
        await self.bot.attack_technique(3, wait=False)
        await self.bot.movepi(0.9, 300)
        await self.bot.attack_technique(5, wait=False)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(5, wait=False)
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(5)
        exit()

