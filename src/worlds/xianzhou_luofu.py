from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.herta_space_station import Base_Zone, Supply_Zone
from worlds.jarilo_vi import Silvermane_Guard, Robot_Settlement


class Init:
    def __init__(self, device, mode='credits'):
        self.mode = mode
        self.central_starskiff_haven = Central_Starskiff_Haven(device)
        self.cloudford = Cloudford(device)
        self.stargazer_navalia = Stargazer_Navalia(device)
        self.divination_commission = Divination_Commission(device)
        self.artisanship_commission = Artisanship_Commission(device)
        self.fyxestroll_garden = Fyxestroll_Garden(device)
        self.alchemy_commission = Alchemy_Commission(device)
        self.scalegorge_waterscape = Scalegorge_Waterscape(device)
        self.the_shackling_prison = The_Shackling_Prison(device)
        self.base_zone = Base_Zone(device)
        self.supply_zone = Supply_Zone(device)
        self.silvermane_guard = Silvermane_Guard(device)
        self.robot_settlement = Robot_Settlement(device)
    async def stockup(self):
        if self.mode == 'credits':
            logger.info(f'Mode: {self.mode}. Nothing to buy.')
        else:
            await self.central_starskiff_haven.teleport()
            await self.central_starskiff_haven.shop_salesby()
    async def farm(self):
        '''
        Status  7/8 (new: shackling prison)
        TP      5 -> ???
        Items   R2: 2, R4: 3
        XP      42596/???
        Time    ???
        '''
        await self.fyxestroll_garden.farm()                         # TP:-4->1 XP:4644/4644 Time:???
        await self.base_zone.restore_tp(tp=4)                       # TP:+4->5 Time:???
        await self.artisanship_commission.farm()                    # TP:-4->1 R4:2 XP:9548/9548 Time:???
        await self.supply_zone.teleport(tp_restore=4)               # TP:+4->5 Time:65
        await self.scalegorge_waterscape.farm()                     # TP:-4->1 XP:4752/4752 Time:450
        await self.silvermane_guard.teleport(tp_restore=4.1)        # TP:+4->5 Time:85  
        await self.divination_commission.farm()                     # TP:-6->1 R2:1 XP:6000/6000 Time:540
        await self.silvermane_guard.teleport(tp_restore=4.2)        # TP:+4->5 Time:???
        await self.alchemy_commission.farm()                        # TP:-7->2 R4:1 XP:6912/6912 Time:???
        await self.cloudford.farm()                                 # TP:+1->3 XP:4644/4644 Time:395
        await self.the_shackling_prison.teleport(tp_restore=2.1)    # TP:+2->5 Time:???
        await self.stargazer_navalia.farm()                         # TP:-5->2 R2:1 XP:6264/6264 Time:425
        await self.the_shackling_prison.farm()                      # TP:+3->5 Time:???
    async def dev(self):
        # await self.the_shackling_prison.teleport()
        # await self.the_shackling_prison.path_1()
        # await self.the_shackling_prison.path_2()
        # await self.the_shackling_prison.path_3()
        raise SystemExit()


class Central_Starskiff_Haven:
    def __init__(self, device):
        self.bot = Bot(device)
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
        await self.bot.buy_item('virtual_particle', amount_percentage=30)
        await self.bot.shop_exit()


class Cloudford:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
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
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Cloudford')
        logger.info('---')
        await self.bot.switch_map(y_list=500/1080, world='the_xianzhou_luofu', scroll_down=False, # Trove of Verdure
                                    x=925/2400, y=663/1080, corner='topleft', move_x=0, move_y=5)
        await self.bot.movepi(0.4, 8000)
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.37, 2300)
        await self.bot.attack() # +2TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(925/2400, 663/1080, move_x=0, move_y=5, corner='topleft') # Trove of Verdure
        await self.bot.movepi(1.75, 2300)
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(1.75, 2400)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 10000)
        await self.bot.movepi(1.7, 4000)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(0.62, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_2(self): # roamer
        logger_set_path(2)
        await self.bot.use_teleporter(925/2400, 663/1080, move_x=0, move_y=5, corner='topleft') # Trove of Verdure
        await self.bot.movepi(1.75, 2300)
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(1.75, 2400)
        await self.bot.movepi(1.5, 8900)
        await self.bot.movepi(1.0, 1000)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 900)
        await self.bot.movepi(1.4, 1100)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(925/2400, 663/1080, move_x=0, move_y=5, corner='topleft') # Trove of Verdure
        await self.bot.movepi(0.75, 2100)
        await self.bot.movepi(1.0, 7500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.movepi(1.9, 2000)
        await self.bot.movepi(1.7, 1000)
        await self.bot.movepi(1.9, 1000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.movepi(0.75, 500)
        await self.bot.movepi(1.0, 1000)
        for _ in range(2): # -1TP, roamer
            await self.bot.movepi(1.0, 300)
            await self.bot.attack_technique(3)
        await self.bot.movepi(0.7, 300)
        await self.bot.attack_technique(3) # +2TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(973/2400, 532/1080, move_x=0, move_y=0, corner='botright') # Skiff Boarding Area
        await self.bot.movepi(0, 9900)
        await self.bot.movepi(1.5, 1900)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(0.5, 2500)
        await self.bot.movepi(0.75, 1900)
        await self.bot.movepi(1, 1500)
        await self.bot.attack_technique(7) # -1TP
        await self.bot.movepi(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.75, 900)
        await self.bot.movepi(0, 3500)
        await self.bot.movepi(1.75, 400)
        await self.bot.movepi(0, 2900)
        await self.bot.attack() # +2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(813/2400, 349/1080, move_x=0, move_y=0, corner='botright') # Bud of Memories
        await self.bot.movepi(1.65, 2900)
        await self.bot.movepi(1.8, 400)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(1.25, 500)
        await self.bot.attack_technique(3) # -1TP, roamer
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(2)
    async def path_6(self):
        logger_set_path(6)
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
        for _ in range(2): # -2TP, roamer
            await self.bot.movepi(0.25, 300)
            await self.bot.attack_technique(2)
        for _ in range(3):
            await self.bot.movepi(0.0, 300)
            await self.bot.attack_technique(2)
        await self.bot.movepi(1.1, 300)
        await self.bot.attack_technique(6)
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(1163/2400, 530/1080, move_x=0, move_y=0, corner='botright') # Shape of Icicle
        await self.bot.movepi(0.0, 1300)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.5, 1000)
        await self.bot.attack() # items
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(813/2400, 349/1080, move_x=0, move_y=0, corner='botright') # Bud of Memories
        await self.bot.movepi(1.65, 1700)
        await self.bot.movepi(0.14, 3100)
        await self.bot.movepi(1.5, 700)
        await self.bot.attack_technique(1) # items
        await self.bot.movepi(0.0, 400)
        await self.bot.attack_technique(3) # -1TP, roamer
        for _ in range(4): # -3TP, roamer
            await self.bot.movepi(0.7, 300)
            await self.bot.attack_technique(2)
        for _ in range(4):
            await self.bot.movepi(1.7, 300)
            await self.bot.attack_technique(3)
    async def path_9(self):
        logger_set_path(9)
        await self.bot.use_teleporter(930/2400, 259/1080, move_x=0, move_y=0, corner='botright') # Cavern of Corrosion
        await self.bot.movepi(1.25, 1000)
        await self.bot.attack() # +2TP
       
 
class Stargazer_Navalia:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.path_7()
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
        await self.bot.attack_technique(2) # -1TP
        await self.bot.movepi(0.25, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.3, 900)
        await self.bot.movepi(1.11, 5000)
        await self.bot.movepi(1.17, 2700)
        await self.bot.movepi(0.6, 2800)
        for _ in range(4): # -2TP, roamer
            await self.bot.movepi(0.2, 300)
            await self.bot.attack_technique(3)
        for _ in range(3):
            await self.bot.movepi(1.2, 300)
            await self.bot.attack_technique(3)
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
        await self.bot.attack_technique(2) # -1TP
        await self.bot.movepi(0.15, 1500)
        await self.bot.movepi(0.4, 1500)
        await self.bot.movepi(0.25, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.15, 4900)
        await self.bot.movepi(1.25, 300)
        await self.bot.attack_technique(2) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(768/2400, 696/1080, move_x=0, move_y=0, corner='topright') # Path of Conflagration
        await self.bot.movepi(1.7, 3300)
        await self.bot.movepi(1.9, 300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(0.4, 1800)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(855/2400, 405/1080, move_x=0, move_y=2, corner='botleft') # Ship Nursery - The Budding
        await self.bot.movepi(0.7, 800)
        await self.bot.movepi(0.5, 900)
        await self.bot.movepi(0.00, 2500)
        for _ in range(2): # -1TP, roamer
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.movepi(1.0, 300)
            await self.bot.attack_technique(2)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.movepi(0.0, 300)
            await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(2)
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(855/2400, 405/1080, move_x=0, move_y=2, corner='botleft') # Ship Nursery - The Budding
        await self.bot.movepi(0.7, 800)
        await self.bot.movepi(0.5, 900)
        await self.bot.movepi(0.0, 2000)
        await self.bot.movepi(0.2, 3000)
        await self.bot.movepi(0.3, 500)
        await self.bot.attack() # items
        await self.bot.movepi(1.1, 1200)
        await self.bot.movepi(1.0, 700)
        await self.bot.movepi(0.5, 3800)
        await self.bot.movepi(0.3, 1000)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.25, 1900)
        await self.bot.movepi(1.0, 5500)
        await self.bot.movepi(0.9, 1500)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.4, 1500)
        await self.bot.attack_technique(4) # -3TP
        await self.bot.movepi(0.3, 300)
        await self.bot.attack_technique(4)
        await self.bot.restore_tp(item='trick_snack') # +2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(855/2400, 184/1080, move_x=0, move_y=0, corner='botleft') # Ship Nursery - The Budding
        await self.bot.movepi(1.5, 700)
        await self.bot.movepi(0.0, 2300)
        await self.bot.movepi(0.5, 800)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.5, 800)
        await self.bot.movepi(1.9, 500)
        await self.bot.movepi(0.00, 8300)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.movepi(0.25, 1000)
        await self.bot.movepi(1.25, 1000)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(10) # -1TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(1106/2400, 610/1080, move_x=0, move_y=0, corner='botright') # Shape of Doom
        await self.bot.movepi(1.5, 700)
        await self.bot.attack() # +2TP
        await self.bot.posfix(1.5, 1000)
        await self.bot.movepi(0.3, 500)
        await self.bot.movepi(0.00, 5400)
        await self.bot.movepi(1.7, 600)
        await self.bot.movepi(0.0, 2550)
        for _ in range(3): # -1TP, roamer, +2TP
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.movepi(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(1.3, 1100)
        await self.bot.attack() # items
        await self.bot.movepi(0.3, 1600)
        await self.bot.movepi(0.0, 3100)
        await self.bot.movepi(1.7, 1300)
        await self.bot.attack() # items
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(958/2400, 364/1080, move_x=0, move_y=0, corner='botleft') # Ship Nursery - The Burgeoning
        await self.bot.movepi(0.95, 1700)
        await self.bot.movepi(0.65, 1900)
        await self.bot.movepi(1.0, 1900)
        await self.bot.movepi(0.5, 1100)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 3000)
        await self.bot.movepi(1.0, 800)
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.0, 1000)
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.0, 1000)
        for _ in range(9): # -2TP, roamer
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.movepi(1.0, 2000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.5, 3700)
        await self.bot.movepi(1.0, 4200)
        await self.bot.movepi(1.5, 1700)
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(3) # -1TP


class Divination_Commission:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
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
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Divination Commission')
        logger.info('---')
        await self.bot.switch_map(y_list=328/1080, world='the_xianzhou_luofu', scroll_down=True,
                                    x=848/2400, y=524/1080, corner='botright', move_x=0, move_y=0) # Bud of Aether
        await self.bot.movepi(1.25, 2600)
        await self.bot.attack_technique(6) # -1TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(445/2400, 720/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Fortuna Augurstead
        await self.bot.movepi(0.5, 4000)
        await self.bot.movepi(0.7, 1500)
        await self.bot.attack() # items
        await self.bot.movepi(1.1, 1600)
        await self.bot.movepi(0.75, 500)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.movepi(1.5, 500)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.restore_tp(item='trick_snack') # +2TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(445/2400, 720/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Fortuna Augurstead
        await self.bot.movepi(0.5, 4000)
        await self.bot.movepi(0.7, 1000)
        await self.bot.movepi(1.0, 2000)
        await self.bot.movepi(0.7, 1200)
        await self.bot.movepi(1.0, 10700)
        await self.bot.movepi(0.5, 800)
        await self.bot.movepi(0.4, 500)
        await self.bot.attack_technique(1) # -3TP, roamer
        await self.bot.movepi(0.7, 200)
        await self.bot.attack_technique(1)
        for _ in range(5):
            await self.bot.movepi(1.0, 300)
            await self.bot.attack_technique(1)
        for _ in range(4):
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(1)
        await self.bot.attack_technique(1)
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(445/2400, 720/1080, move_x=0, move_y=0, corner='botright', confirm=True) # Fortuna Augurstead
        await self.bot.movepi(0.5, 4000)
        await self.bot.movepi(0.7, 1000)
        await self.bot.movepi(1.0, 2000)
        await self.bot.movepi(0.7, 1200)
        await self.bot.movepi(1.0, 10700)
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.6, 500)
        await self.bot.attack() # +2TP
        await self.bot.posfix(1.75, 1000)
        await self.bot.movepi(0.75, 1000)
        await self.bot.movepi(1.0, 1500)
        await self.bot.movepi(1.5, 500)
        await self.bot.attack_technique(5)
        await self.bot.movepi(1.2, 1000)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(14) # -1TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(627/2400, 308/1080, corner='botright', move_x=0, move_y=3) # Matrix of Prescience Ultima
        await self.bot.movepi(0.75, 800)
        await self.bot.attack() # +2TP
    async def path_5(self): # roamer
        logger_set_path(5)
        await self.bot.use_teleporter(1089/2400, 284/1080, corner='botright', move_x=0, move_y=0) # Conclave Hall
        await self.bot.movepi(1.5, 22900)
        await self.bot.movepi(1.25, 2200)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(1.5, 3000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.1, 3000)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.75, 1000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.movepi(0.75, 5000)
        await self.bot.movepi(1.0, 3500)
        for _ in range(4): # -3TP
            await self.bot.movepi(1.3, 300)
            await self.bot.attack_technique(1)
        for _ in range(2):
            await self.bot.movepi(1.3, 300)
            await self.bot.attack_technique(2)
        for _ in range(9):
            await self.bot.movepi(0.4, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(1)
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(1089/2400, 284/1080, corner='botright', move_x=0, move_y=0) # Conclave Hall
        await self.bot.movepi(1.0, 1100)
        await self.bot.movepi(0.7, 2100)
        await self.bot.attack() # items
        await self.bot.movepi(1.7, 3500)
        await self.bot.movepi(1.5, 10000)
        await self.bot.movepi(0.78, 1500)
        await self.bot.attack() # items
        await self.bot.movepi(0.75, 1000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.75, 2600)
        await self.bot.movepi(1.5, 8500)
        await self.bot.movepi(0.0, 1500)
        await self.bot.attack() # items
        await self.bot.movepi(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.2, 2500)
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(0.0, 3000)
        await self.bot.movepi(1.75, 1700)
        await self.bot.movepi(0.0, 3500)
        await self.bot.movepi(0.5, 1900)
        await self.bot.movepi(0.0, 3700)
        await self.bot.movepi(1.75, 1000)
        await self.bot.movepi(0.0, 2500)
        await self.bot.movepi(1.42, 1100)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.4, 2500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.35, 3800)
        await self.bot.movepi(1.1, 1500)
        await self.bot.movepi(1.0, 4300)
        await self.bot.movepi(1.5, 3500)
        await self.bot.movepi(1.75, 2000)
        await self.bot.movepi(1.75, 300)
        await self.bot.attack_technique(2) # -1TP
    async def path_7(self): # roamer
        logger_set_path(7)
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
        await self.bot.attack_technique(4) # -2TP
        await self.bot.movepi(0.6, 500)
        await self.bot.attack_technique(6)    
    async def path_8(self): # roamer
        logger_set_path(8)
        await self.bot.use_teleporter(743/2400, 586/1080, corner='topleft', move_x=0, move_y=0) # Spatial Terminal
        await self.bot.movepi(1.5, 3700)
        await self.bot.movepi(1.75, 5800)
        await self.bot.movepi(0.0, 1500)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.0, 1900)
        await self.bot.movepi(1.25, 2800)
        await self.bot.movepi(0.75, 300)
        await self.bot.attack_technique(1) # -2TP
        for _ in range(4):
            await self.bot.movepi(1.2, 300)
            await self.bot.attack_technique(1)
        for _ in range(4):
            await self.bot.movepi(1.75, 300)
            await self.bot.attack_technique(1)
    async def path_9(self):
        logger_set_path(9)
        await self.bot.use_teleporter(743/2400, 586/1080, corner='topleft', move_x=0, move_y=0) # Spatial Terminal
        await self.bot.movepi(1.5, 3700)
        await self.bot.movepi(1.75, 11300)
        await self.bot.movepi(0.0, 2900)
        await self.bot.movepi(0.3, 1200)
        await self.bot.attack() # items
        await self.bot.movepi(0.0, 2500)
        await self.bot.movepi(0.5, 1500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.5, 2500)
        await self.bot.movepi(0.0, 4500)
        await self.bot.movepi(0.25, 3200)
        await self.bot.movepi(0.0, 1400)
        await self.bot.movepi(0.2, 300)
        await self.bot.attack_technique(3) # -1TP


class Artisanship_Commission:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.path_7()
        await self.path_8()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Artisanship Commission')
        logger.info('---')
        await self.bot.switch_map(y_list=446/1080, world='the_xianzhou_luofu', scroll_down=True,
                                    x=933/2400, y=530/1080, corner='topright', move_x=0, move_y=4) # Passage of the Finery Foundry
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(0.0, 6200)
        await self.bot.movepi(0.25, 700)
        await self.bot.movepi(0.1, 500)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(0.0, 500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.movepi(1.25, 700)
        await self.bot.attack_technique(3) # -1TP
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
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(5) # -1TP
    async def path_2(self):
        logger_set_path(2)
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
        await self.bot.attack_technique(5) # -1TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(854/2400, 418/1080, corner='botright', move_x=0, move_y=4) # Creation Furnace
        await self.bot.movepi(1.0, 1100)
        await self.bot.movepi(1.5, 900)
        await self.bot.movepi(0.0, 1900)
        await self.bot.movepi(0.5, 2800)
        await self.bot.movepi(0.2, 2100)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.5, 1600)
        await self.bot.movepi(0.0, 1400)
        await self.bot.movepi(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.3, 500)
        await self.bot.movepi(1.5, 4600)
        await self.bot.movepi(0.0, 500)
        await self.bot.attack_technique(2) # -3TP, roamer
        for _ in range(8):
            await self.bot.movepi(0.0, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.movepi(0.9, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.movepi(1.9, 300)
            await self.bot.attack_technique(1)
        await self.bot.restore_tp(item='punitive_energy') # +4TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(894/2400, 610/1080, corner='topleft', move_x=0, move_y=2) # Passage to the Sapientia Academe
        await self.bot.movepi(1.25, 3100)
        await self.bot.movepi(1.0, 8000)
        await self.bot.movepi(0.75, 200)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(1.5, 800)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.movepi(1.25, 2500)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.25, 500)
        await self.bot.movepi(0.5, 600)
        await self.bot.movepi(1.0, 4600)
        await self.bot.movepi(0.5, 8350)
        await self.bot.movepi(1.0, 3600)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.0, 500)
        await self.bot.movepi(1.4, 2000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.2, 500)
        await self.bot.movepi(1.5, 5200)
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(3) # -2TP
        for _ in range(3):
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.movepi(0.25, 300)
            await self.bot.attack_technique(1)
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(894/2400, 610/1080, corner='topleft', move_x=0, move_y=2) # Passage to the Sapientia Academe
        await self.bot.movepi(1.25, 3100)
        await self.bot.movepi(1.0, 8000)
        await self.bot.movepi(1.4, 1400)
        await self.bot.movepi(1.0, 4700)
        await self.bot.movepi(0.57, 3800)
        await self.bot.attack() # items
        await self.bot.movepi(1.4, 2100)
        await self.bot.movepi(1.0, 300)
        await self.bot.attack_technique(12)
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(1.2, 2000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.5, 400)
        await self.bot.movepi(0.8, 800)
        await self.bot.movepi(0.5, 200)
        await self.bot.attack() # items
        await self.bot.movepi(0.2, 1000)
        await self.bot.movepi(0.4, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.2, 1500)
        await self.bot.movepi(1.0, 3300)
        await self.bot.movepi(0.5, 2500)
        await self.bot.movepi(0.83, 900)
        await self.bot.attack() # items
        await self.bot.movepi(0.5, 900)
        await self.bot.movepi(1.0, 1500)
        await self.bot.movepi(0.4, 1500)
        await self.bot.movepi(0.25, 1000)
        await self.bot.restore_tp(item='punitive_energy') # +4TP
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.2, 3500)
        await self.bot.movepi(1.0, 600)
        await self.bot.attack_technique(3) # items
        for _ in range(4): # -3TP
            await self.bot.movepi(1.0, 300)
            await self.bot.attack_technique(2)
        for _ in range(3): # -1TP
            await self.bot.movepi(0.75, 300)
            await self.bot.attack_technique(2)
        for _ in range(3): # -1TP
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.movepi(1.2, 1000)
        await self.bot.movepi(1.4, 1500)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.2, 3100)
        await self.bot.attack() # +2TP
    async def path_6(self): # roamer
        logger_set_path(6)
        await self.bot.use_teleporter(854/2400, 418/1080, corner='botright', move_x=0, move_y=4) # Creation Furnace
        await self.bot.movepi(1.0, 1100)
        await self.bot.movepi(1.5, 900)
        await self.bot.movepi(0.00, 1800)
        await self.bot.movepi(0.5, 2500)
        await self.bot.movepi(0.00, 3300)
        await self.bot.movepi(1.5, 3000)
        await self.bot.movepi(1.75, 1000)
        await self.bot.movepi(0.25, 4500)
        await self.bot.movepi(0.5, 5700)
        await self.bot.movepi(1.05, 1000)
        await self.bot.movepi(1.25, 100)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.movepi(0.25, 700)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(804/2400, 487/1080, corner='topleft', move_x=0, move_y=5) # Shape of Puppetry
        await self.bot.movepi(1.22, 2100)
        await self.bot.attack() # +2TP
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(894/2400, 610/1080, corner='topleft', move_x=0, move_y=2) # Passage to the Sapientia Academe
        await self.bot.movepi(0.5, 4400)
        await self.bot.movepi(0.75, 1700)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.1, 1600)
        await self.bot.movepi(0.5, 1600)
        await self.bot.attack_technique(2) # items
        await self.bot.movepi(1.7, 500)
        for _ in range(6): # -2TP
            await self.bot.movepi(0.0, 300)
            await self.bot.attack_technique(2)
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(0.0, 1000)
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.75, 1000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.movepi(1.0, 1000)
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.0, 4100)
        await self.bot.movepi(1.5, 900)
        await self.bot.movepi(1.65, 2200)
        for _ in range(3): # -1TP
            await self.bot.movepi(0.0, 300)
            await self.bot.attack_technique(1)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(6)


class Fyxestroll_Garden:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.path_7()
        await self.path_8()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Fyxestroll Garden')
        logger.info('---')
        await self.bot.switch_map(y_list=568/1080, world='the_xianzhou_luofu', scroll_down=True, # Locufox Forest Backdoor
                                    x=578/2400, y=284/1080, move_x=0, move_y=1, corner='botleft', confirm=False)
        await self.bot.movepi(1.5, 4400)
        await self.bot.movepi(1.95, 600)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.movepi(1.0, 1000)
        await self.bot.movepi(1.2, 500)
        await self.bot.attack_technique(4) # -1TP
    async def path_1(self): # roamer
        logger_set_path(1)
        await self.bot.use_teleporter(697/2400, 153/1080, move_x=0, move_y=0) # Path of Darkness
        await self.bot.movepi(1.8, 1800)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.8, 800)
        await self.bot.movepi(0.1, 2100)
        await self.bot.movepi(1.75, 2600)
        await self.bot.movepi(0.25, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(697/2400, 153/1080, move_x=0, move_y=0) # Path of Darkness
        await self.bot.movepi(1.8, 2300)
        await self.bot.movepi(1.9, 800)
        await self.bot.movepi(0.1, 1800)
        await self.bot.movepi(1.75, 2600)
        await self.bot.movepi(0.25, 3000)
        await self.bot.movepi(0.1, 2100)
        await self.bot.attack() # items
        await self.bot.movepi(0.7, 1900)
        await self.bot.attack_technique(3) # -2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(510/2400, 423/1080, corner='botleft', move_x=0, move_y=0) # Shape of Perdition
        await self.bot.movepi(0.95, 2500)
        await self.bot.attack() # +2TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(412/2400, 603/1080, move_x=0, move_y=0) # Bud of Abundance
        await self.bot.movepi(1.49, 3900)
        await self.bot.attack_technique(2) # -1TP
    async def path_5(self):
        logger_set_path(5) # roamer
        await self.bot.use_teleporter(412/2400, 603/1080, move_x=0, move_y=0) # Bud of Abundance
        await self.bot.movepi(0.9, 4000)
        await self.bot.movepi(1.2, 3000)
        await self.bot.attack_technique(8) # -1TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(931/2400, 383/1080, corner='botright', move_x=0, move_y=0) # Verdant Terrace Entrance
        await self.bot.movepi(0.75, 3400)
        await self.bot.movepi(1.0, 1500)
        await self.bot.movepi(0.75, 3100)
        await self.bot.movepi(1.25, 5900)
        await self.bot.attack() # +2TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(577/2400, 285/1080, corner='botleft', move_x=0, move_y=1) # Locufox Forest Backdoor
        await self.bot.movepi(0.5, 2500)
        await self.bot.movepi(0.25, 2000)
        await self.bot.movepi(0.75, 2000)
        await self.bot.movepi(0.5, 2000)
        await self.bot.movepi(0.4, 1500)
        await self.bot.attack_technique(3) # -2TP
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(412/2400, 603/1080, move_x=0, move_y=0)  # Bud of Abundance
        await self.bot.movepi(1.47, 5000)
        await self.bot.movepi(1.2, 2000)
        await self.bot.movepi(0.9, 1500)
        await self.bot.movepi(1.12, 2300)
        await self.bot.attack() # +2TP
        await self.bot.sleep(0.5)
        await self.bot.movepi(1.2, 1500)
        await self.bot.movepi(0.7, 1000)
        await self.bot.attack_technique(4) # -2TP


class Alchemy_Commission:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
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
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Alchemy Comission')
        logger.info('---')
        await self.bot.switch_map(y_list=685/1080, world='the_xianzhou_luofu', scroll_down=True, # Healer's Market
                                    x=854/2400, y=689/1080, corner='topright', move_x=0, move_y=6, confirm=True)
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(0.75, 6700)
        await self.bot.movepi(0.98, 6000)
        await self.bot.attack() # items
        await self.bot.movepi(1.2, 4000)
        await self.bot.movepi(1.1, 4500)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.movepi(1.6, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(854/2400, 689/1080, corner='topright', move_x=0, move_y=6, confirm=True) # Healer's Market
        await self.bot.movepi(1.4, 4600)
        await self.bot.movepi(1.9, 2100)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.2, 1000)
        await self.bot.movepi(0.9, 2800)
        await self.bot.movepi(1.4, 7400)
        await self.bot.movepi(0.0, 1400)
        await self.bot.attack() # items
        await self.bot.movepi(1.65, 1000)
        await self.bot.posfix(1.65, 1000)
        await self.bot.movepi(1.0, 1000)
        await self.bot.movepi(1.5, 1500)
        await self.bot.movepi(1.8, 600)
        await self.bot.attack_technique(6) # -1TP
        await self.bot.movepi(1.7, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(659/2400, 363/1080, corner='botright', move_x=0, move_y=0) # Cavern of Corrosion
        await self.bot.movepi(1.5, 2800)
        await self.bot.movepi(1.2, 1600)
        await self.bot.attack() # +2TP
        await self.bot.movepi(1.75, 2000)
        for _ in range(3): # -1TP, roamer
            await self.bot.movepi(1.25, 300)
            await self.bot.attack_technique(2)
        await self.bot.movepi(0.25, 1000)
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.movepi(0.4, 2000)
        await self.bot.movepi(0.65, 1300)
        await self.bot.attack() # items
        await self.bot.movepi(1.6, 2300)
        await self.bot.movepi(1.25, 300)
        await self.bot.attack_technique(12) # -1TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(867/2400, 646/1080, corner='topleft', move_x=0, move_y=4) # Elixir Research Terrace
        await self.bot.movepi(0.5, 10300)
        await self.bot.movepi(0.75, 2000)
        await self.bot.movepi(1.1, 2200)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.0, 600)
        await self.bot.movepi(1.5, 4400)
        await self.bot.movepi(1.0, 1300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(3)
        await self.bot.movepi(0.25, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(867/2400, 646/1080, corner='topleft', move_x=0, move_y=4) # Elixir Research Terrace
        await self.bot.movepi(0.5, 6900)
        await self.bot.movepi(0.0, 3600)
        await self.bot.movepi(1.5, 3700)
        await self.bot.movepi(0.0, 4200)
        await self.bot.attack_technique(2) # -1TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(1003/2400, 595/1080, corner='topleft', move_x=0, move_y=3) # Aureate Elixir Furnace
        await self.bot.movepi(0.8, 700)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.1, 500)
        await self.bot.movepi(0.55, 2200)
        await self.bot.movepi(0.34, 2300)
        await self.bot.movepi(0.2, 1300)
        await self.bot.movepi(0.5, 1200)
        await self.bot.movepi(0.35, 2000)
        await self.bot.movepi(0.14, 2700)
        await self.bot.attack_technique(1) # -2TP
        for _ in range(2):
            await self.bot.movepi(1.64, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.movepi(0.14, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.movepi(0.64, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.movepi(1.14, 300)
            await self.bot.attack_technique(1)
        for _ in range(2):
            await self.bot.movepi(1.64, 300)
            await self.bot.attack_technique(1)
        await self.bot.restore_tp(item='punitive_energy') # +4TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(1003/2400, 595/1080, corner='topleft', move_x=0, move_y=3) # Aureate Elixir Furnace
        await self.bot.movepi(0.54, 3200)
        await self.bot.movepi(0.33, 2500)
        await self.bot.movepi(0.1, 1000)
        await self.bot.movepi(0.6, 1000)
        await self.bot.movepi(0.33, 2600)
        await self.bot.movepi(0.13, 3000)
        await self.bot.movepi(1.85, 1000)
        await self.bot.movepi(0.15, 1000)
        await self.bot.movepi(0.13, 3100)
        await self.bot.movepi(1.82, 1500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.movepi(1.32, 300)
        await self.bot.attack_technique(2) # -1TP
        for _ in range(3):
            await self.bot.movepi(1.82, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.movepi(0.32, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.movepi(0.82, 300)
            await self.bot.attack_technique(1)
        for _ in range(3):
            await self.bot.movepi(1.32, 300)
            await self.bot.attack_technique(1)
        for _ in range(2):
            await self.bot.movepi(1.82, 300)
            await self.bot.attack_technique(1)
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(583/2400, 241/1080, corner='botright', move_x=0, move_y=3) # Bud of Nihility
        await self.bot.movepi(1.0, 1500)
        await self.bot.movepi(0.5, 4200)
        await self.bot.movepi(0.7, 1800)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.movepi(0.8, 1500)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(0.0, 1000)
        await self.bot.movepi(0.28, 1300)
        await self.bot.attack() # items
        await self.bot.movepi(1.55, 1200)
        await self.bot.movepi(1.7, 1500)
        await self.bot.movepi(1.4, 1000)
        await self.bot.movepi(1.5, 6000)
        await self.bot.movepi(0.0, 4800)
        await self.bot.movepi(1.8, 600)
        await self.bot.attack() # +2TP
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(583/2400, 241/1080, corner='botright', move_x=0, move_y=3) # Bud of Nihility
        await self.bot.movepi(1.0, 2600)
        await self.bot.movepi(0.5, 3100)
        await self.bot.movepi(1.0, 3400)
        await self.bot.movepi(1.4, 1900)
        await self.bot.movepi(1.1, 300)
        await self.bot.attack() # items
        for _ in range(8): # -3TP
            await self.bot.movepi(1.15, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.movepi(0.35, 300)
            await self.bot.attack_technique(1)
        await self.bot.movepi(1.7, 800)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(16)
    async def path_9(self):
        logger_set_path(9)
        await self.bot.use_teleporter(1355/2400, 351/1080, corner='botright', move_x=0, move_y=5) # Shape of Celestial
        await self.bot.movepi(1.66, 2500)
        await self.bot.attack() # +2TP
    async def path_10(self):
        logger_set_path(10)
        await self.bot.use_teleporter(583/2400, 241/1080, corner='botright', move_x=0, move_y=3) # Bud of Nihility
        await self.bot.movepi(1.0, 2600)
        await self.bot.movepi(0.5, 3100)
        await self.bot.movepi(1.0, 3500)
        await self.bot.movepi(1.1, 4000)
        await self.bot.movepi(1.5, 3600)
        await self.bot.movepi(1.0, 3000)
        await self.bot.movepi(0.5, 500)
        await self.bot.attack_technique(13) # move
        await self.bot.movepi(1.0, 500)
        await self.bot.attack_technique(3) # +2TP
    async def path_11(self):
        logger_set_path(11)
        await self.bot.use_teleporter(1003/2400, 595/1080, corner='topleft', move_x=0, move_y=3) # Aureate Elixir Furnace
        await self.bot.movepi(0.54, 3200)
        await self.bot.movepi(0.33, 2500)
        await self.bot.movepi(0.1, 1000)
        await self.bot.movepi(0.6, 1000)
        await self.bot.movepi(0.33, 2600)
        await self.bot.movepi(0.13, 3000)
        await self.bot.movepi(1.85, 1000)
        await self.bot.movepi(0.15, 1000)
        await self.bot.movepi(0.13, 3100)
        await self.bot.movepi(1.82, 2500)
        await self.bot.movepi(1.55, 2000)
        await self.bot.movepi(1.35, 3000)
        await self.bot.movepi(1.55, 5000)
        await self.bot.movepi(1.25, 3000)
        await self.bot.movepi(1.1, 2200)
        await self.bot.attack_technique(3) # -3TP
        await self.bot.movepi(1.7, 300)
        await self.bot.attack_technique(1)
        await self.bot.movepi(0.6, 300)
        await self.bot.attack_technique(5)


class Scalegorge_Waterscape:
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.path_7()
        await self.path_8()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Scalegorge Waterscape')
        logger.info('---')
        await self.bot.switch_map(y_list=807/1080, world='the_xianzhou_luofu', scroll_down=True, # Dragonvista Rain Hall
                                    x=966/2400, y=379/1080, corner='botright', move_x=0, move_y=0)
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(1.7, 2900)
        await self.bot.attack() # items
        await self.bot.movepi(0.4, 4500)
        await self.bot.movepi(0.1, 2900)
        await self.bot.attack_technique(4) # -3TP
        await self.bot.movepi(1.3, 300)
        await self.bot.attack_technique(4)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(4)
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(357/2400, 354/1080, move_x=0, move_y=0) # Ancient Sea Palace Ruins
        await self.bot.movepi(0.75, 900)
        await self.bot.attack() # items
        await self.bot.movepi(1.75, 1200)
        await self.bot.movepi(1.5, 8000)
        await self.bot.movepi(0.0, 1000)
        await self.bot.attack() # +2TP
        await self.bot.posfix(1.70, 1300)
        await self.bot.attack() # items
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(357/2400, 354/1080, move_x=0, move_y=0) # Ancient Sea Palace Ruins
        await self.bot.movepi(1.0, 4900)
        await self.bot.movepi(1.3, 2100)
        await self.bot.attack() # items
        await self.bot.movepi(1.0, 1000)
        await self.bot.movepi(0.9, 2000)
        for _ in range(9): # -3TP, roamer
            await self.bot.movepi(1.0, 300)
            await self.bot.attack_technique(1)
        for _ in range(4):
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(1)
        await self.bot.movepi(1.7, 300)
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(1433/2400, 659/1080, corner='topleft', move_x=0, move_y=0) # Palace Ruin Depthsck
        await self.bot.movepi(1.3, 1200)
        await self.bot.attack() # items
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(1.5, 2900)
        await self.bot.movepi(1.13, 2000)
        await self.bot.attack() # +2TP
        await self.bot.movepi(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.75, 600)
        await self.bot.movepi(0.0, 2100)
        await self.bot.movepi(0.5, 2400)
        await self.bot.movepi(1.0, 6500)
        await self.bot.movepi(0.7, 1300)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.movepi(0.75, 1000)
        await self.bot.movepi(1.0, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(1.6, 1000)
        await self.bot.movepi(1.5, 1000)
        await self.bot.movepi(1.0, 1900)
        await self.bot.movepi(0.5, 1200)
        await self.bot.attack() # items
        await self.bot.movepi(0.25, 500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.2, 1000)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(21) # -1TP, roamer
    async def path_4(self):
        logger_set_path(4)
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
        await self.bot.attack_technique(2) # -1TP
        await self.bot.movepi(1.6, 300)
        await self.bot.attack_technique(1)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_5(self):
        logger_set_path(5)
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
        await self.bot.movepi(0.5, 3900)
        for _ in range(2): # -2TP, roamer
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(1)
        for _ in range(6):
            await self.bot.movepi(0.8, 300)
            await self.bot.attack_technique(1)
        for _ in range(4):
            await self.bot.movepi(0.0, 300)
            await self.bot.attack_technique(1)
        await self.bot.attack_technique(7)
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(1433/2400, 659/1080, corner='topleft', move_x=0, move_y=0) # Palace Ruin Depths
        await self.bot.movepi(1.5, 6000)
        await self.bot.movepi(1.6, 300)
        await self.bot.attack() # +2TP
        await self.bot.sleep(0.5)
        await self.bot.movepi(0.5, 3600)
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(12) # -1TP
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(1465/2400, 341/1080, corner='topleft', move_x=0, move_y=0) # Shape of Abomination
        await self.bot.movepi(1.0, 1600)
        await self.bot.movepi(0.75, 1600)
        await self.bot.movepi(1.0, 5000)
        await self.bot.movepi(1.1, 1000)
        await self.bot.movepi(1.0, 2000)
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(1.4, 1700)
        await self.bot.movepi(1.6, 1200)
        await self.bot.movepi(1.8, 800)
        await self.bot.attack() # +2TP
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(1433/2400, 659/1080, corner='topleft', move_x=0, move_y=0) # Palace Ruin Depths
        await self.bot.movepi(1.5, 3000)
        await self.bot.movepi(0.0, 3600)
        await self.bot.movepi(1.5, 6000)
        await self.bot.movepi(1.25, 500)
        for _ in range(3): # -2TP, roamer
            await self.bot.movepi(1.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.movepi(0.5, 300)
        await self.bot.attack_technique(3)
        await self.bot.movepi(0.25, 300)
        await self.bot.attack_technique(6) # items
    

class The_Shackling_Prison:
    def __init__(self, device):
        self.bot = Bot(device)
    async def restore_tp(self, tp):
        if tp == 2.1:
            self.teleport(tp_restore=tp)
        else:
            raise SystemExit(f'no {tp} TP restore available')
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
    async def teleport(self, tp_restore=None):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: The Shackling Prison')
        logger.info('---')
        if tp_restore == 2.1:
            await self.bot.switch_map(y_list=928/1080, world='the_xianzhou_luofu', scroll_down=True, # Plankway Front
                                        x=575/2400, y=615/1080, move_x=5, move_y=4, corner='topright')
            await self.bot.movepi(0.4, 2600)
            await self.bot.attack_technique(1) # items
            await self.bot.movepi(0.75, 500)
            await self.bot.attack_technique(12) # move
            await self.bot.movepi(0.6, 500)
            await self.bot.attack_technique(4) # items
            await self.bot.movepi(0.87, 500) # gradually increase this one
            await self.bot.attack_technique(8) # +2TP
            await self.bot.movepi(0.6, 1000)
            await self.bot.movepi(0.25, 1000)
            await self.bot.posfix(0.25, 1000)
            await self.bot.movepi(1.1, 500)
            await self.bot.attack_technique(7) # items
            await self.bot.movepi(1.0, 500)
            await self.bot.attack_technique(10) # items
        else:
            await self.bot.switch_map(y_list=928/1080, world='the_xianzhou_luofu', scroll_down=True, # Grimfrost Hold (II)
                                        x=551/2400, y=358/1080, move_x=4, move_y=3, corner='botright')
            await self.bot.movepi(0.35, 900)
            await self.bot.attack() # +2TP
            await self.bot.movepi(1.5, 2000)
            await self.bot.movepi(1.67, 3600)
            await self.bot.movepi(1.5, 500)
            await self.bot.attack_technique(10) # items
            await self.bot.movepi(0.35, 500)
            await self.bot.attack_technique(4) # move
            await self.bot.movepi(0.0, 500)
            await self.bot.attack_technique(3) # items
            await self.bot.movepi(0.4, 800)
            await self.bot.movepi(0.25, 1000)
            await self.bot.posfix(0.25, 1000)
            await self.bot.movepi(1.4, 800)
            await self.bot.movepi(1.8, 3900)
            await self.bot.interact(wait_for_ready=True)
            await self.bot.movepi(0.4, 1500)
            await self.bot.movepi(0.35, 1000)
            await self.bot.movepi(0.5, 500)
            await self.bot.attack_technique(2) # items
            await self.bot.movepi(0.25, 1500)
            await self.bot.posfix(0.25, 1000)
            await self.bot.movepi(0.9, 1700)
            await self.bot.movepi(1.2, 1700)
            await self.bot.movepi(1.45, 1800)
            await self.bot.movepi(1.1, 500)
            await self.bot.attack_technique(3) # items
            await self.bot.movepi(0.5, 1500)
            await self.bot.movepi(0.25, 1000)
            await self.bot.posfix(0.25, 1000)
            await self.bot.movepi(1.25, 500)
            await self.bot.attack_technique(4) # move
            await self.bot.movepi(1.65, 500)
            await self.bot.attack_technique(6) # move
            await self.bot.movepi(0.0, 500)
            await self.bot.attack_technique(8) # move
            await self.bot.movepi(0.25, 1000)
            await self.bot.posfix(0.25, 1000)
            await self.bot.movepi(1.4, 1800)
            await self.bot.movepi(1.65, 500)
            await self.bot.attack_technique(18) # items
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(x=551/2400, y=358/1080, corner='botright', move_x=4, move_y=3) # Grimfrost Hold (II)
        await self.bot.movepi(0.5, 500)
        await self.bot.attack_technique(9) # move
        await self.bot.movepi(0.9, 300)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.movepi(0.3, 500)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.movepi(0.0, 100)
        await self.bot.attack_technique(3) # items
        await self.bot.movepi(0.1, 1500)
        await self.bot.movepi(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.3, 2200)
        await self.bot.movepi(1.0, 500)
        await self.bot.attack_technique(12) # move
        await self.bot.movepi(1.3, 300)
        await self.bot.attack_technique(6) # -1TP, roamer
        await self.bot.movepi(1.8, 300)
        await self.bot.attack_technique(3)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(3)
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(x=1287/2400, y=411/1080, corner='botleft', move_x=3, move_y=3) # Grimfrost Hold (I)
        raise SystemExit('check,prision,path2')
        await self.bot.movepi(0.4, 500)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.movepi(0.9, 500)
        await self.bot.attack_technique(2) # items
        await self.bot.movepi(0.4, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.movepi(1.7, 500)
        await self.bot.movepi(0.1, 300)
        await self.bot.movepi(0.6, 500)
        await self.bot.attack_technique(6) # move
        for _ in range(11): # -1TP, roamer
            await self.bot.movepi(0.45, 300)
            await self.bot.attack_technique(2)
        await self.bot.movepi(0.6, 2000)
        await self.bot.movepi(0.75, 1000)
        await self.bot.posfix(0.75, 500)
        await self.bot.movepi(1.45, 3000)
        await self.bot.movepi(1.0, 300)
        await self.bot.attack_technique(6) # -1TP
        await self.bot.movepi(1.6, 800)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.movepi(1.6, 800)
        await self.bot.movepi(1.5, 300)
        await self.bot.attack_technique(4) # +2TP
        await self.bot.movepi(0.15, 300)
        await self.bot.attack_technique(10) # items
        await self.bot.movepi(0.25, 1000)
        await self.bot.posfix(0.25, 500)
        await self.bot.movepi(1.0, 1000)
        await self.bot.movepi(0.85, 300)
        await self.bot.attack_technique(8) # items
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(x=605/2400, y=289/1080, corner='botright', move_x=3, move_y=4) # Pyroscape Hold
        raise SystemExit('check,prision,path3')
        await self.bot.movepi(0.9, 500)
        await self.bot.attack_technique(6) # items
        await self.bot.movepi(0.8, 1000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.movepi(0.3, 500)
        await self.bot.movepi(0.5, 1100)
        await self.bot.movepi(0.75, 500)
        await self.bot.attack_technique(12) # +2TP
        await self.bot.movepi(0.6, 500)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.movepi(1.5, 500)
        await self.bot.movepi(1.1, 300)
        await self.bot.attack_technique(5) # -1TP, roamer
        await self.bot.movepi(0.0, 300)
        await self.bot.attack_technique(5)
        await self.bot.use_teleporter(x=605/2400, y=289/1080, corner='botright', move_x=3, move_y=4) # Pyroscape Hold
        await self.bot.movepi(0.65, 500)
        await self.bot.attack_technique(4) # move
        await self.bot.movepi(0.7, 600)
        await self.bot.interact(wait_for_ready=True) # move bridge to TP object
        await self.bot.movepi(0.5, 600)
        await self.bot.movepi(0.9, 1200)
        await self.bot.movepi(0.4, 500)
        await self.bot.attack_technique(10) # move
        await self.bot.movepi(0.6, 300)
        await self.bot.attack_technique(3) # +2TP
        await self.bot.movepi(1.71, 300)
        await self.bot.attack_technique(12) # items
        await self.bot.use_teleporter(x=605/2400, y=289/1080, corner='botright', move_x=3, move_y=4) # Pyroscape Hold
        await self.bot.movepi(0.65, 500)
        await self.bot.attack_technique(4) # move
        await self.bot.movepi(0.7, 600)
        await self.bot.interact(wait_for_ready=True) # move bridge to TP object