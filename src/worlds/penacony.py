from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.universal import Init as Universal
from worlds.jarilo_vi import Silvermane_Guard

class Init:
    '''
    Status: 7/9
    '''
    def __init__(self, device, mode='credits'):
        self.mode = mode
        self.golden_hour = Golden_Hour(device)
        self.dreams_edge = Dreams_Edge(device)
        self.childs_dream = Childs_Dream(device)
        self.the_reverie_dreamscape = The_Reverie_Dreamscape(device)
        self.dewlight_pavilion = Dewlight_Pavilion(device)
        self.clock_studios_theme_park = Clock_Studios_Theme_Park(device)
        self.penacony_grand_theater = Penacony_Grand_Theater(device)
        self.the_soaring_clock_hand = The_Soaring_Clock_Hand(device)
        self.universal = Universal(device)
        self.silvermane_guard = Silvermane_Guard(device)
    async def farm(self):
        '''
        ### Mode: credits (default)
        XP:???
        Time:???
        TP:???
        
        ### Mode: XP
        XP:???
        Time:???
        TP: 5 -> ???
        R2: 10 (credits) 15 (xp)
        R4: 0
        '''
        # await self.dreams_edge.farm()                       # TP:-4->1 XP:7668/9612 Time:431    
        # await self.silvermane_guard.restore_tp(tp=4.1)      # TP:+4->5 Time:85
        # await self.clock_studios_theme_park.farm()          # TP:-10->1 R2:3 XP:7648/7648 Time:???
        # await self.silvermane_guard.restore_tp(tp=4.2)      # TP:+4->5 Time:???         
        # await self.the_reverie_dreamscape.farm()            # TP:-???->1 R2:5(credits)8(xp) XP:14580/15552 Time:?
        # await self.golden_hour.restore_tp(tp=4.1)           # TP:+4->5 Time:???
        # await self.dewlight_pavilion.farm()                 # TP:-22->1 R2:5(credits)7(xp) XP:11448/11448 Time:
        # await self.golden_hour.restore_tp(tp=4.2)           # TP:+4->5 Time:80
        await self.childs_dream.farm()                      # TP:-9->2 R2:4 XP:5832/5832 Time:???
        await self.the_soaring_clock_hand.restore_tp(tp=4)  # TP:+4->5 Time:???
        await self.penacony_grand_theater.farm()            # XP:?/? Time: TP:1->? R4:0 R2:?
    async def dev(self):
        raise SystemExit()


class Golden_Hour:
    def __init__(self, device):
        self.bot = Bot(device)
    async def restore_tp(self, tp):
        logger_set_path('Teleport: TP Restore')
        logger.info('---')
        logger.info('--- Map: Golden Hour')
        logger.info('---')
        if tp == 4.1:
            await self.bot.switch_map(y_list=650/1080, world='penacony',
                                        x=588/2400, y=356/1080, move_x=4, move_y=3,) # Sweet Corner
            await self.bot.move(1.5, 3300)
            await self.bot.attack() # items
            await self.bot.move(1.6, 1000)
            await self.bot.move(1.4, 2800)
            await self.bot.attack() # +2TP
            await self.bot.use_teleporter(815/2400, 245/1080, move_x=0, move_y=2) # Oti Mall
            await self.bot.move(0.7, 2000)
            await self.bot.move(0.9, 4400)
            await self.bot.attack() # +2TP
        elif tp == 4.2:
            await self.bot.switch_map(y_list=650/1080, world='penacony',
                                        x=330/2400, y=498/1080, corner='botright', move_x=0, move_y=0) # The Reverie Hotel Entrance
            await self.bot.move(0.35, 9000)
            await self.bot.move(0.8, 1000)
            await self.bot.attack_technique(3) # +2TP
            await self.bot.use_teleporter(1219/2400, 630/1080, corner='topleft', move_x=0, move_y=0) # Aideen Park
            await self.bot.move(1.5, 3000)
            await self.bot.move(1.6, 3100)
            await self.bot.attack() # items
            await self.bot.move(0.82, 2900)
            await self.bot.attack() # items
            await self.bot.move(1.4, 4000)
            await self.bot.move(1.3, 2400)
            await self.bot.move(0.8, 500)
            await self.bot.attack() # +2TP
        else:
            raise SystemExit(f'no {tp} TP restore available')


class Dreams_Edge:
    '''
    TP: -12
    R4: 2 
    '''
    def __init__(self, device):
        self.bot = Bot(device)
        self.universal = Universal(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.universal.restore_tp(tp=4)
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.universal.restore_tp(tp=4)
        await self.path_7()
        await self.path_8()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Dream's Edge")
        logger.info('---')
        await self.bot.switch_map(y_list=771/1080, world='penacony', scroll_down=False, # Bud of Memories
                                    x=658/2400, y=738/1080, move_x=0, move_y=7, corner='botleft')
        await self.bot.move(1.65, 2300)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(1.2, 2000)
        await self.bot.move(1.7, 2000)
        await self.bot.posfix(1.65, 1000)
        await self.bot.move(0.8, 5700)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1.8, 1400)
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(8) # -1TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
        await self.bot.move(0.9, 1000)
        await self.bot.attack() # +2TP
        await self.bot.move(1.0, 1600)
        await self.bot.move(0.5, 2400)
        await self.bot.move(0.9, 900)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.05, 400)
        await self.bot.attack_technique(8) # -2TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.switch_map(y_list=771/1080, world='penacony', scroll_down=False, # Rooftop Garden
                                    x=764/2400, y=253/1080, corner='botright', move_x=2, move_y=3)
        await self.bot.move(0.5, 3500)
        await self.bot.move(0.00, 2500)
        await self.bot.move(1.90, 1400)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(0.9, 1100)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(543/2400, 503/1080, move_x=3, move_y=1, corner='topright', confirm=True) # The Family's Construction Authority
        await self.bot.move(0.25, 3000)
        await self.bot.move(0.5, 8500)
        await self.bot.attack() # +2TP
        await self.bot.move(1.05, 5000)
        await self.bot.attack_technique(11) # -2TP
        await self.bot.move(1.25, 2500)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.9, 2000)
        await self.bot.move(0.67, 1800)
        await self.bot.move(1.0, 500)
        await self.bot.interact()
        await self.bot.move(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.4, 900)
        await self.bot.move(0.9, 1700)
        await self.bot.move(0.4, 2500)
        await self.bot.move(0.2, 500)
        await self.bot.move(0.0, 300)
        await self.bot.sleep(0.5)
        await self.bot.interact()
        await self.bot.move(0.25, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.0, 1300)
        await self.bot.move(0.45, 2600)
        await self.bot.move(1.95, 2900)
        await self.bot.move(0.45, 2000)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.0, 3000)
        await self.bot.move(0.6, 1500)
        await self.bot.attack_technique(1) # items
        await self.bot.move(0.2, 700)
        await self.bot.attack_technique(2) # items
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
        await self.bot.move(0.5, 5000)
        await self.bot.move(0.75, 1500)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.38, 1800)
        await self.bot.attack() # items
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(8) # -1TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(933/2400, 535/1080, move_x=0, move_y=5, corner='topright') # Dreamweaver Plaza
        await self.bot.move(1.97, 2000)
        await self.bot.attack_technique(8) # -1TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(933/2400, 535/1080, move_x=0, move_y=5, corner='topright') # Dreamweaver Plaza
        await self.bot.move(0.25, 1500)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(7) # move
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(5) # move
        await self.bot.move(0.0, 1300)
        await self.bot.attack_technique(1) # items
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(5) # -1TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.switch_map(y_list=771/1080, world='penacony', scroll_down=False, # Dreamweaver Plaza
                                    x=933/2400, y=535/1080, corner='topright', move_x=0, move_y=5)
        await self.bot.move(0.25, 1500)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(7) # move
        await self.bot.move(0.0, 500)
        await self.bot.attack_technique(6) # move
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(15) # move
        await self.bot.attack_technique(6) # -3TP, roamer
        await self.bot.move(1.2, 300)
        await self.bot.attack_technique(4) # stability
        await self.bot.move(0.2, 300)
        await self.bot.attack_technique(8) # items
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(909/2400, 345/1080, move_x=0, move_y=7, corner='botleft') # Shape of Roast
        await self.bot.move(1.5, 3000)
        await self.bot.move(0.05, 1300)
        await self.bot.attack() # +2TP
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(5) # -3TP, roamer
        await self.bot.move(0.75, 300)
        await self.bot.attack_technique(6)
        await self.bot.move(1.75, 300)
        await self.bot.attack_technique(6)


class Childs_Dream:
    '''
    data here
    '''
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Childs's Dream")
        logger.info('---')
        await self.bot.switch_map(y_list=893/1080, world='penacony', scroll_down=False, # Corridor of Memories
                                    x=1010/2400, y=304/1080, move_x=0, move_y=4, corner='botright')
        await self.bot.move(0.25, 2000)
        await self.bot.move(0.0, 1900)
        await self.bot.move(0.5, 3300)
        await self.bot.attack() # items
        await self.bot.move(1.8, 300)
        await self.bot.attack_technique(8) # -2TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(962/2400, 356/1080, move_x=0, move_y=0, corner='botright') # Eddying Dreamscape
        await self.bot.move(1.9, 1600)
        await self.bot.attack() # +2TP
        await self.bot.move(1.1, 1700)
        await self.bot.move(1.5, 2900)
        await self.bot.move(1.9, 700)
        await self.bot.attack_technique(3) # -2TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(962/2400, 519/1080, move_x=0, move_y=0, corner='botright') # Bud of Aether
        await self.bot.move(1.45, 2200)
        await self.bot.move(1.88, 9400)
        await self.bot.interact()
        await self.bot.move(1.95, 2900)
        await self.bot.action_button()
        await self.bot.move(0.00, 3000)
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.25, 500)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.restore_tp(item='trick_snack') # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(1010/2400, 304/1080, move_x=0, move_y=4, corner='botright') # Corridor of Memories
        await self.bot.move(1.5, 9300)
        await self.bot.move(1.0, 7000)
        await self.bot.attack() # items
        await self.bot.move(1.5, 500)
        await self.bot.attack_technique(6) # -3TP
        await self.bot.restore_tp(item='trick_snack', n=2) # +4TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(962/2400, 356/1080, move_x=0, move_y=0, corner='botright') # Eddying Dreamscape
        await self.bot.move(0.5, 9000)
        await self.bot.move(1.0, 3200)
        await self.bot.move(0.6, 300)
        await self.bot.move(0.5, 500)
        await self.bot.attack() # items
        await self.bot.move(1.5, 800)
        await self.bot.move(1.0, 3000)
        for _ in range(2): # -3TP
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.7, 2200)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.0, 1500)
        await self.bot.interact()
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.25, 2500)
        await self.bot.action_button()
        await self.bot.move(1.0, 2600)
        await self.bot.move(0.5, 2300)
        await self.bot.attack() # items
        await self.bot.move(1.0, 1300)
        await self.bot.move(0.5, 2200)
        await self.bot.action_button()
        await self.bot.move(0.5, 2200)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(8) # +2TP
        await self.bot.move(1.9, 3000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.95, 4800)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.0, 1400)
        await self.bot.action_button()
        await self.bot.move(0.0, 3000)
        await self.bot.move(0.5, 5000)
        await self.bot.move(1.0, 1300)
        await self.bot.move(0.5, 3800)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(0.35, 2000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.4, 2500)
        await self.bot.move(1.0, 700)
        await self.bot.interact()
        await self.bot.move(1.2, 1100)
        await self.bot.action_button()
        await self.bot.move(1.0, 2700)
        await self.bot.move(0.5, 3000)
        await self.bot.action_button()
        await self.bot.move(0.5, 2000)
        await self.bot.move(1.0, 1600)
        await self.bot.move(1.5, 3000)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.restore_tp(item='trick_snack') # +2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(1122/2400, 617/1080, move_x=0, move_y=0, corner='botright') # Clock Factory
        await self.bot.move(0.5, 5000)
        await self.bot.move(1.0, 600)
        await self.bot.attack() # items
        await self.bot.move(1.3, 800)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(5) # -1TP


class The_Reverie_Dreamscape:
    '''
    TODO: there is one more 3D room
    37/??? fights
    R2: 5 (credits), 8 (xp)
    # TP:-22->1 XP:14580/15552 Time:?
    '''
    def __init__(self, device):
        self.bot = Bot(device)
    async def farm(self, mode='credits'):
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
        await self.rest_tp4()
        await self.path_16()
        await self.rest_tp4()
        await self.path_17()
    async def teleport(self):
        logger_set_path('Teleport')
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
    async def rest_tp2(self):
        await self.bot.restore_tp(item='trick_snack', n=1) # +2TP
    async def rest_tp4(self):
        await self.bot.restore_tp(item='trick_snack', n=2) # +4TP
    async def path_1(self):
        logger_set_path(1)
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
        logger_set_path(2)
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
        logger_set_path(3)
        await self.bot.use_teleporter(1132/2400, 660/1080, move_x=0, move_y=8, corner='botleft') # Bud of Harmony
        await self.bot.move(1.0, 2500)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(12) # -2TP, roamer
    async def path_4(self):
        logger_set_path(4)
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
        logger_set_path(5)
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
        logger_set_path(6)
        await self.bot.use_teleporter(935/2400, 587/1080, move_x=0, move_y=5, corner='topleft') # VIP Lounge Corridor
        await self.bot.move(1.25, 1200)
        await self.bot.move(1.0, 5100)
        await self.bot.move(0.5, 4800)
        await self.bot.move(1.0, 500)
        await self.bot.attack_technique(10) # -1TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(935/2400, 587/1080, move_x=0, move_y=5, corner='topleft') # VIP Lounge Corridor
        await self.bot.move(0.5, 1600)
        await self.bot.move(1.0, 2300)
        await self.bot.move(0.6, 1600)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.45, 2600)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(10) # -1TP
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(574/2400, 482/1080, move_x=0, move_y=6, corner='topleft') # Shape of Nectar
        await self.bot.move(1.5, 2600)
        await self.bot.attack() # +2TP
    async def path_9(self):
        logger_set_path(9)
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
        logger_set_path(10)
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
        logger_set_path(11)
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
        logger_set_path(12)
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
        logger_set_path(13)
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
        await self.bot.restore_tp(item='trick_snack', n=2) # +4TP
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
        raise SystemExit('check,path13,reverie')
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
        logger_set_path(14)
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
        logger_set_path(15)
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
        await self.bot.restore_tp(item='trick_snack', n=2) # +4TP
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
        logger_set_path(16)
        await self.bot.use_teleporter(1241/2400, 520/1080, move_x=0, move_y=5, corner='topright', confirm=True) # Platinum Guest Room
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
        logger_set_path(17)
        await self.bot.use_teleporter(748/2400, 533/1080, move_x=0, move_y=3, corner='topleft') # Monitoring Room
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
        logger_set_path(18)
        # TODO: one more room


class Dewlight_Pavilion:
    '''
    R2: 5 (credits), 7 (xp)
    '''
    def __init__(self, device):
        self.bot = Bot(device)
        self.universal = Universal(device)
    async def farm(self, mode='credits'):
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.universal.restore_tp(tp=4)
        await self.path_5()
        await self.path_6()
        await self.path_7()
        await self.path_8()
        await self.path_9()
        await self.path_10()
        await self.universal.restore_tp(tp=4)
        await self.path_11()
    async def teleport(self):
        logger_set_path('Teleport')
        logger.info('---')
        logger.info("--- Map: Dewlight Pavilion")
        logger.info('---')
        await self.bot.switch_map(y_list=328/1080, world='penacony', scroll_down=True, # Reception Counter
                                    x=981/2400, y=718/1080, corner='botright', move_x=0, move_y=0)
        await self.bot.move(0.67, 3900)
        await self.bot.attack() # items
        await self.bot.move(0.1, 2100)
        await self.bot.move(0.5, 1800)
        await self.bot.move(1.09, 1900)
        await self.bot.attack() # items
        await self.bot.move(0.09, 2200)
        await self.bot.move(1.89, 1700)
        await self.bot.attack() # items
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(981/2400, 718/1080, move_x=0, move_y=0, corner='botright') # Reception Counter
        await self.bot.move(0.5, 10350)
        await self.bot.move(0.0, 7000)
        await self.bot.move(1.5, 7000)
        await self.bot.move(1.7, 2100)
        await self.bot.move(1.3, 1900)
        await self.bot.interact()
        await self.bot.move(0.75, 2000)
        await self.bot.move(0.6, 1800)
        await self.bot.action_button()
        await self.bot.move(1.0, 2300)
        await self.bot.attack() # items
        await self.bot.move(1.5, 1000)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.8, 1200)
        await self.bot.move(0.5, 800)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(1.25, 3000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(1.6, 2800)
        await self.bot.action_button()
        await self.bot.move(1.5, 1700)
        await self.bot.move(1.7, 500)
        await self.bot.attack_technique(3) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(981/2400, 718/1080, move_x=0, move_y=0, corner='botright') # Reception Counter
        await self.bot.move(0.5, 10350)
        await self.bot.move(0.0, 7000)
        await self.bot.move(1.5, 7000)
        await self.bot.move(1.7, 2100)
        await self.bot.move(1.3, 1900)
        await self.bot.interact()
        await self.bot.move(0.3, 2000)
        await self.bot.move(0.4, 1600)
        await self.bot.action_button()
        await self.bot.move(0.0, 1900)
        await self.bot.move(1.9, 400)
        await self.bot.attack() # +2TP
        await self.bot.move(1.5, 1300)
        await self.bot.move(0.1, 900)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(2) # items
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(912/2400, 485/1080, move_x=0, move_y=2, corner='topleft') # Dreammaster Hall
        await self.bot.move(0.8, 2300)
        await self.bot.move(0.5, 4600)
        await self.bot.move(1.0, 1600)
        await self.bot.attack() # items
        await self.bot.move(0.1, 1000)
        await self.bot.move(0.5, 3400)
        await self.bot.move(1.0, 800)
        await self.bot.move(1.5, 6000)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.5, 3000)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(2) # -1TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(912/2400, 485/1080, move_x=0, move_y=2, corner='topleft') # Dreammaster Hall
        await self.bot.move(1.1, 1000)
        await self.bot.attack() # +2TP
        await self.bot.move(0.7, 1000)
        await self.bot.move(0.5, 5900)
        await self.bot.attack() # items
        await self.bot.move(0.0, 3100)
        await self.bot.attack() # items
        await self.bot.move(1.5, 1200)
        await self.bot.move(0.0, 800)
        await self.bot.move(0.5, 3800)
        await self.bot.move(0.0, 800)
        await self.bot.move(1.6, 3000)
        await self.bot.attack() # items
        await self.bot.move(1.4, 3300)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.1, 1000)
        await self.bot.move(1.5, 3500)
        await self.bot.attack_technique(2) # items
        await self.bot.move(1.7, 1000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.8, 500)
        await self.bot.move(0.5, 2400)
        await self.bot.move(0.0, 10400)
        await self.bot.move(0.5, 3600)
        await self.bot.move(0.0, 2600)
        await self.bot.move(0.5, 300)
        await self.bot.move(0.7, 2500)
        await self.bot.interact()
        await self.bot.move(0.75, 1500)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.9, 2000)
        await self.bot.move(1.6, 4000)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.0, 3200)
        await self.bot.attack() # items
        await self.bot.move(1.75, 1000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.6, 2800)
        await self.bot.move(0.1, 200)
        await self.bot.action_button()
        await self.bot.move(0.0, 2000)
        await self.bot.attack_technique(6) # -3TP
        await self.bot.posfix(0.25, 5000)
        await self.bot.restore_tp(item='trick_snack', n=2) # +4TP
        await self.bot.move(1.04, 4200)
        await self.bot.attack() # items
        await self.bot.move(0.29, 1300)
        await self.bot.attack() # items
        await self.bot.move(0.95, 1200)
        await self.bot.attack() # items
        await self.bot.move(1.1, 1400)
        await self.bot.interact()
        await self.bot.move(0.0, 2000)
        await self.bot.move(1.5, 3300)
        await self.bot.action_button()
        await self.bot.move(1.0, 1500)
        await self.bot.move(1.6, 2500)
        await self.bot.posfix(1.75, 1500)
        await self.bot.move(1.0, 3300)
        await self.bot.move(0.5, 2550)
        await self.bot.action_button()
        await self.bot.move(0.0, 2000)
        await self.bot.move(1.5, 2100)
        await self.bot.posfix(1.25, 1500)
        await self.bot.move(0.0, 2900)
        await self.bot.move(0.5, 6200)
        await self.bot.action_button()
        await self.bot.move(0.49, 5500)
        await self.bot.attack() # items
        await self.bot.posfix(0.25, 1500)
        await self.bot.move(1.1, 1250)
        await self.bot.move(1.0, 5500)
        await self.bot.attack() # items
        await self.bot.posfix(0.75, 1500)
        await self.bot.move(1.5, 1700)
        await self.bot.move(0.0, 1000)
        await self.bot.move(0.1, 600)
        await self.bot.move(0.25, 600)
        await self.bot.move(1.5, 600)
        await self.bot.move(1.4, 200)
        await self.bot.attack_technique(6) # -2TP
        await self.bot.move(1.75, 2000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.7, 1000)
        await self.bot.move(0.4, 2500)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.2, 2000)
        await self.bot.move(1.5, 3000)
        await self.bot.move(0.0, 1000)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.33, 3000)
        await self.bot.attack() # items
        await self.bot.move(1.9, 2500)
        await self.bot.move(0.25, 1500)
        await self.bot.attack() # items
        await self.bot.move(0.1, 1000)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(3) # -1TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.switch_map(y_list=328/1080, world='penacony', scroll_down=True, # Dreammaster Hall
                                    x=912/2400, y=485/1080, corner='topleft', move_x=0, move_y=2)
        await self.bot.move(0.8, 2300)
        await self.bot.move(0.5, 4600)
        await self.bot.move(1.0, 900)
        await self.bot.move(0.5, 3400)
        await self.bot.move(1.0, 1200)
        await self.bot.move(1.5, 7700)
        await self.bot.move(1.0, 10100)
        await self.bot.move(0.49, 2700)
        await self.bot.attack() # items
        await self.bot.move(1.51, 4800)
        await self.bot.interact()
        await self.bot.move(1.5, 600)
        await self.bot.move(1.1, 1100)
        await self.bot.attack() # items
        await self.bot.move(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.1, 1200)
        await self.bot.move(0.0, 550)
        await self.bot.action_button()
        await self.bot.move(1.5, 900)
        await self.bot.move(1.4, 2500)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.8, 5000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.95, 1600)
        await self.bot.attack() # items
        await self.bot.move(0.95, 3300)
        await self.bot.move(0.6, 1200)
        await self.bot.attack_technique(2) # -2TP
        await self.bot.move(0.45, 1900)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.4, 2900)
        await self.bot.move(1.5, 2300)
        await self.bot.move(0.0, 2000)
        await self.bot.move(0.3, 2600)
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.6, 400)
        await self.bot.interact()
        await self.bot.move(0.5, 3000)
        await self.bot.move(0.25, 2500)
        await self.bot.restore_tp(item='trick_snack', n=1) # +2TP
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.2, 2000)
        await self.bot.move(1.0, 6000)
        await self.bot.move(0.6, 900)
        await self.bot.action_button()
        await self.bot.move(0.5, 1900)
        await self.bot.move(0.0, 2000)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.55, 2800)
        await self.bot.attack() # items
        await self.bot.posfix(0.9, 5000)
        await self.bot.move(1.78, 5800)
        await self.bot.move(1.5, 100)
        await self.bot.attack() # items
        await self.bot.move(0.32, 1700)
        await self.bot.move(0.48, 700)
        await self.bot.attack() # +2TP
        await self.bot.move(1.7, 1700)
        await self.bot.attack_technique(3) # -2TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(912/2400, 485/1080, move_x=0, move_y=2, corner='topleft') # Dreammaster Hall
        await self.bot.move(0.5, 1000)
        await self.bot.interact()
        await self.bot.wait_for_onmap(min_duration=3)
        await self.bot.move(0.51, 2800)
        await self.bot.attack() # items
        await self.bot.move(0.69, 1500)
        await self.bot.attack() # items
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(1093/2400, 629/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # Shape of Ire
        await self.bot.move(1.2, 1600)
        await self.bot.attack() # items
        await self.bot.move(1.5, 3300)
        await self.bot.move(0.0, 600)
        await self.bot.attack() # +2TP
    async def path_8(self):
        logger_set_path(8)
        # await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.move(0.35, 500)
        await self.bot.attack_technique(14) # move
        await self.bot.move(0.3, 500)
        await self.bot.attack_technique(8) # items
        raise SystemExit('improve get into corner')
        await self.bot.move(0.25, 500)
        await self.bot.attack_technique(2) # move
        await self.bot.move(1.85, 500)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.9, 2000)   
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.75, 500)
        await self.bot.attack_technique(8) # move
        await self.bot.move(1.15, 300)
        await self.bot.attack_technique(2) # -1TP
        for _ in range(3): # -2TP, roamer
            await self.bot.move(1.6, 300)
            await self.bot.attack_technique(2)
        for _ in range(2):
            await self.bot.move(0.95, 300)
            await self.bot.attack_technique(2)
        for _ in range(4):
            await self.bot.move(0.25, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.4, 300)
        await self.bot.attack_technique(2)
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(8)
        await self.bot.restore_tp('punitive_energy', n=1) # +4TP
    async def path_9(self):
        logger_set_path(9)
        await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.move(0.5, 11500)
        await self.bot.interact(wait_for_ready=False)
        await self.bot.action_tap(1535, 960)
        await self.bot.wait_for_onmap(min_duration=5)
        await self.bot.move(0.51, 5500)
        await self.bot.interact(wait_for_ready=False)
        await self.bot.action_tap(1535, 960)
        await self.bot.wait_for_onmap(min_duration=5)
        await self.bot.move(0.47, 2200)
        await self.bot.attack() # items
        await self.bot.move(0.65, 2200)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.1, 1600)
        await self.bot.attack_technique(2) # -1TP
    async def path_10(self):
        logger_set_path(10)
        await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.move(0.3, 2500)
        await self.bot.move(1.83, 6300)
        await self.bot.move(0.45, 700)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.8, 300)
        await self.bot.attack_technique(5) # -1TP, roamer
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(5)
        await self.bot.move(1.7, 300)
        await self.bot.attack_technique(5) # items
    async def path_11(self):
        logger_set_path(11)
        await self.bot.switch_map(y_list=328/1080, world='penacony', scroll_down=True, # Dreammaster Hall
                                    x=912/2400, y=485/1080, corner='topleft', move_x=0, move_y=2)
        await self.bot.move(0.2, 2300)
        await self.bot.move(0.5, 4300)
        await self.bot.move(0.0, 8000)
        await self.bot.attack() # items
        await self.bot.posfix(0.2, 1200)
        await self.bot.move(1.45, 3000)
        await self.bot.move(1.5, 2900)
        await self.bot.move(0.2, 300)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(1.4, 400)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(8) # -2TP
    # disabled: choose monsters over extra tp
    async def path_extra(self):
        logger_set_path('extra')
        await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.move(0.5, 11500)
        await self.bot.interact(wait_for_ready=False)
        await self.bot.action_tap(1535, 960)
        await self.bot.wait_for_onmap(min_duration=5)
        await self.bot.move(0.51, 5500)
        await self.bot.interact(wait_for_ready=False)
        await self.bot.action_tap(1535, 960)
        await self.bot.wait_for_onmap(min_duration=5)
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(2) # +2TP


class Clock_Studios_Theme_Park:
    '''
    TP:-10->1
    R2:3
    XP:7648/7648
    Time:???
    '''
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
        logger.info('--- Map: Clock Studios Theme Park')
        logger.info('---')
        await self.bot.switch_map(y_list=446/1080, world='penacony', scroll_down=True, # Theme Park Entrance
                                    x=1216/2400, y=299/1080, corner='botright', move_x=1, move_y=6, confirm=True)
        await self.bot.move(0.45, 6300)
        await self.bot.attack(2) # items
        await self.bot.move(1.0, 2500)
        await self.bot.attack(2) # items
        await self.bot.move(0.3, 6000)
        await self.bot.attack(3) # items
        await self.bot.move(1.0, 5800)
        await self.bot.attack(3) # items
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(1209/2400, 276/1080, move_x=1, move_y=6, confirm=True) # Theme Park Entrance
        await self.bot.move(0.36, 6000)
        await self.bot.move(0.2, 2600)
        await self.bot.move(0.5, 12900)
        await self.bot.move(0.25, 3000)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.2, 1000)
        await self.bot.move(0.5, 2700)
        await self.bot.move(0.9, 4000)
        await self.bot.move(0.6, 2000)
        await self.bot.move(0.8, 3000)
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.7, 2000)
        await self.bot.move(1.6, 900)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.25, 2500)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.3, 2500)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.7, 1300)
        await self.bot.move(1.0, 1500)
        await self.bot.move(1.2, 1500)
        await self.bot.move(1.5, 2000)
        await self.bot.move(1.6, 1800)
        await self.bot.move(1.2, 1000)
        await self.bot.move(0.7, 3200)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.4, 500)
        await self.bot.attack_technique(3) # -1TP
    async def path_2(self):
        logger_set_path(2)
        await self.bot.use_teleporter(731/2400, 494/1080, corner='botright', move_x=1, move_y=6) # Shape of Duty
        await self.bot.move(1.3, 700)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
        await self.bot.move(0.8, 3300)
        for _ in range(4): # -1TP, roamer
            await self.bot.move(0.6, 300)
            await self.bot.attack_technique(1)
        for _ in range(6): # items
            await self.bot.move(1.5, 300)
            await self.bot.attack_technique(1)
        await self.bot.move(1.75, 2000)
        await self.bot.posfix(1.75, 1000)
        await self.bot.move(0.6, 3500)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.8, 1500)
        await self.bot.attack_technique(3) # -1TP
        await self.bot.move(1.45, 300)
        await self.bot.attack_technique(5) # -1TP
        await self.bot.move(1.1, 1000)
        await self.bot.move(1.4, 2000)
        await self.bot.move(1.25, 1000)
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.5, 5100)
        await self.bot.move(1.0, 900)
        await self.bot.attack() # +2TP
    async def path_4(self):
        logger_set_path(4)
        await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1, confirm=True) # Hanu Gang Place
        await self.bot.move(0.49, 7000)
        await self.bot.move(0.01, 5500)
        await self.bot.move(0.5, 500)
        await self.bot.attack() # items
        await self.bot.move(0.52, 4500)
        await self.bot.attack_technique(3) # -2TP
    async def path_5(self):
        logger_set_path(5)
        await self.bot.use_teleporter(929/2400, 549/1080, corner='topleft', move_x=0, move_y=7) # Screening Area Entrance
        await self.bot.move(0.6, 2500)
        await self.bot.attack() # +2TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(1100/2400, 423/1080, corner='botright', move_x=3, move_y=3) # Bud of Preservation
        await self.bot.move(1.69, 2500)
        await self.bot.attack() # +2TP
        await self.bot.move(1.2, 4100)
        await self.bot.move(1.1, 1600)
        await self.bot.attack() # items
        await self.bot.move(0.6, 2200)
        await self.bot.move(0.75, 1000)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(3) # -1TP
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright', confirm=True) # Hamster Ball Park
        await self.bot.move(1.58, 7000)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.0, 1500)
        await self.bot.move(1.3, 3000)
        await self.bot.restore_tp(item='trick_snack', n=1) # +2TP
        await self.bot.posfix(1.25, 1000)
        await self.bot.move(0.4, 1000)
        await self.bot.move(0.7, 2800)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(8) # -1TP
        await self.bot.move(1.9, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright', confirm=True) # Hamster Ball Park
        await self.bot.move(0.2, 3000)
        await self.bot.move(1.98, 4500)
        await self.bot.attack() # +2TP
        await self.bot.move(0.4, 300)
        await self.bot.move(0.2, 700)
        await self.bot.move(0.1, 2800)
        await self.bot.attack() # items
        await self.bot.move(1.55, 6000)
        await self.bot.move(1.9, 700)
        await self.bot.attack() # +2TP
    async def path_9(self):
        logger_set_path(9)
        await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright', confirm=True) # Hamster Ball Park
        await self.bot.move(0.2, 3000)
        await self.bot.move(0.0, 4700)
        await self.bot.move(0.4, 800)
        await self.bot.move(0.6, 500)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(0.1, 1000)
        await self.bot.move(0.5, 7000)
        await self.bot.move(0.25, 1000)
        await self.bot.restore_tp(item='trick_snack', n=1) # +2TP
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.5, 1800)
        await self.bot.move(1.3, 1500)
        await self.bot.move(1.1, 300)
        await self.bot.attack_technique(1) # -1TP
        for _ in range(4): # -1TP
            await self.bot.move(0.9, 300)
            await self.bot.attack_technique(1)
        for _ in range(4): # -1TP
            await self.bot.move(1.1, 300)
            await self.bot.attack_technique(1)
        await self.bot.move(0.6, 1000)
        await self.bot.move(1.0, 3000)
        await self.bot.move(0.6, 2000)
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.6, 2500)
        for _ in range(4): # -1TP
            await self.bot.move(0.0, 300)
            await self.bot.attack_technique(2)


# Soulgrad: y=686
# class Penacony_Grand_Theater:
#     def __init__(self, device):
#         self.bot = Bot(device)
#     async def teleport(self): # 1->3
#         logger_set_path('Teleport')
#         logger.info('---')
#         logger.info('--- Map: Penacony Grand Theater')
#         logger.info('---')
#         await self.bot.switch_map(y_list=807/1080, world='penacony', scroll_down=True,
#                                     x=787/2400, y=717/1080, corner='topleft', move_x=3, move_y=7)

        
class Penacony_Grand_Theater:
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
        await self.path_x()
    async def teleport(self): # 1->3
        logger_set_path('Teleport')
        logger.info('---')
        logger.info('--- Map: Penacony Grand Theater')
        logger.info('---')
        await self.bot.switch_map(y_list=807/1080, world='penacony', scroll_down=True, # Echo of War
                                    x=787/2400, y=717/1080, corner='topleft', move_x=3, move_y=7)
        await self.bot.move(0.12, 1800)
        await self.bot.attack() # +2TP
    async def path_1(self):
        logger_set_path(1)
        await self.bot.use_teleporter(966/2400, 763/1080, move_x=1, move_y=6, swipe=2, corner='topleft') # Hall of Chords
        await self.bot.move(0.31, 2200)
        await self.bot.attack() # +2TP
        await self.bot.move(1.6, 1000)
        await self.bot.move(0.1, 2500)
        await self.bot.attack() # items
        await self.bot.move(1.6, 500)
        await self.bot.move(0.1, 4000)
        await self.bot.move(0.25, 2500)
        await self.bot.move(0.4, 500)
        await self.bot.attack() # items
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(0.6, 1500)
        await self.bot.posfix(0.6, 1000)
        await self.bot.move(1.7, 1000)
        await self.bot.move(0.35, 5000)
        await self.bot.move(0.5, 1500)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.8, 300)
        await self.bot.attack_technique(4) # -1TP
    async def path_2(self): # 1->3
        logger_set_path(2)
        await self.bot.use_teleporter(1251/2400, 469/1080, move_x=0, move_y=8, swipe=2, corner='botright') # Communing Hall
        await self.bot.move(1.4, 3000)
        await self.bot.move(1.5, 1000)
        await self.bot.attack() # items
        await self.bot.move(1.6, 4500)
        await self.bot.move(0.1, 1600)
        await self.bot.attack() # +2TP
    async def path_3(self):
        logger_set_path(3)
        await self.bot.use_teleporter(1251/2400, 469/1080, move_x=0, move_y=8, swipe=2, corner='botright') # Communing Hall
        await self.bot.move(0.62, 2400)
        await self.bot.attack(2) # items
        await self.bot.move(0.0, 2100)
        await self.bot.attack() # items
        await self.bot.move(0.7, 5000)
        await self.bot.move(0.5, 700)
        await self.bot.attack(2) # items
    async def path_4(self): # 3->3
        logger_set_path(4)
        await self.bot.use_teleporter(1251/2400, 469/1080, move_x=0, move_y=8, swipe=2, corner='botright') # Communing Hall
        await self.bot.move(0.5, 6000)
        await self.bot.move(0.4, 8000)
        for _ in range(3): # -1TP
            await self.bot.move(0.3, 300)
            await self.bot.attack_technique(2)
        for _ in range(2): # +2TP
            await self.bot.move(1.9, 300)
            await self.bot.attack_technique(2)
        for _ in range(2): # -1TP
            await self.bot.move(0.9, 300)
            await self.bot.attack_technique(4)
    async def path_5(self): # 3 -> 
        logger_set_path(5)
        await self.bot.use_teleporter(635/2400, 388/1080, move_x=0, move_y=9, swipe=1, corner='botright') # Ascension Hallway
        await self.bot.move(0.3, 900)
        await self.bot.move(0.0, 4200)
        await self.bot.move(1.9, 900)
        await self.bot.move(0.0, 500)
        await self.bot.attack() # +2TP
        await self.bot.move(0.3, 500)
        for _ in range(2):
            await self.bot.move(0.1, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(4) # -1TP
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6)
        await self.bot.move(1.7, 300)
        await self.bot.attack_technique(6) # -1TP
    async def path_6(self):
        logger_set_path(6)
        await self.bot.use_teleporter(635/2400, 388/1080, move_x=0, move_y=9, swipe=1, corner='botright') # Ascension Hallway
        await self.bot.move(0.62, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.3, 500)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(1.0, 1000)
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(7) # items
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.69, 300)
        await self.bot.attack_technique(6) # items
        await self.bot.move(0.33, 300)
        await self.bot.attack_technique(6) # items
    async def path_7(self):
        logger_set_path(7)
        await self.bot.use_teleporter(900/2400, 184/1080, move_x=0, move_y=9, swipe=2, corner='botright') # Bud of Erdutition
        await self.bot.move(1.5, 1200)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1, 1500)
        await self.bot.move(0.83, 2500)
        await self.bot.attack_technique(1) # items
        await self.bot.move(1.3, 300)
        await self.bot.attack_technique(9) # -1TP
    async def path_8(self):
        logger_set_path(8)
        await self.bot.use_teleporter(900/2400, 184/1080, move_x=0, move_y=9, swipe=2, corner='botright') # Bud of Erdutition
        await self.bot.move(1.37, 500)
        await self.bot.attack_technique(19) # -1TP
    async def path_9(self):
        logger_set_path(9)
        await self.bot.use_teleporter(1000/2400, 274/1080, move_x=1, move_y=7, swipe=2, corner='botright') # Hall of Chords
        await self.bot.move(0.9, 3500)
        await self.bot.move(0.7, 1000)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(1.0, 2000)
        await self.bot.move(0.9, 1000)
        await self.bot.move(0.7, 1600)
        await self.bot.attack_technique(2) # +2TP
        await self.bot.move(0.75, 2000)
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(1.4, 2000)
        await self.bot.move(0.9, 2000)
        await self.bot.move(0.7, 1000)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(3) # items
    async def path_10(self):
        logger_set_path(10)
        await self.bot.use_teleporter(599/2400, 322/1080, move_x=0, move_y=8, swipe=2, corner='botleft') # Cavern of Corrosion
        await self.bot.move(1.3, 1400)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(0.1, 500)
        await self.bot.attack_technique(6) # items
        await self.bot.move(0.25, 1000)
        await self.bot.posfix(0.25, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.8, 7000)
        await self.bot.posfix(1.8, 1000)
        await self.bot.move(1.5, 1000)
        await self.bot.move(1.85, 1500)
        await self.bot.attack_technique(2) # items
        # END: 5TP
    async def path_x(self):
        logger_set_path(11)
        await self.bot.use_teleporter(787/2400, 717/1080, corner='topleft', move_x=3, move_y=7) # Echo of War
        # TODO: 4 to the left
    async def path_z(self):
        logger_set_path(11)
        await self.bot.use_teleporter(671/2400, 526/1080, move_x=0, move_y=8, swipe=2, corner='botleft') # Saloon of Gospels
        # TODO: +2TP bot, teleport back, go into dream (1), -2TP


class The_Soaring_Clock_Hand:
    def __init__(self, device):
        self.bot = Bot(device)
    async def restore_tp(self, tp):
        logger_set_path('Teleport: Restore TP')
        logger.info('---')
        logger.info('--- Map: The Soaring Clock Hand')
        logger.info('---')
        if tp == 4:
            await self.bot.switch_map(y_list=927/1080, world='penacony', scroll_down=True,
                                        x=974/2400, y=417/1080, corner='topright', move_x=0, move_y=0, confirm=True)
            await self.bot.move(0.35, 3000)
            await self.bot.move(0.5, 2000)
            await self.bot.move(0.86, 2000)
            await self.bot.attack_technique(2) # +2TP
            await self.bot.use_teleporter(917/2400, 648/1080, move_x=0, move_y=0, swipe=0, corner='botright') # Aft Pool
            await self.bot.move(0.75, 3200)
            await self.bot.move(0.5, 3200)
            await self.bot.move(1.0, 300)
            await self.bot.attack_technique(2) # items
            await self.bot.move(1.1, 2000)
            await self.bot.posfix(1.25, 1000)
            await self.bot.move(0.0, 2000)
            await self.bot.move(1.7, 500)
            await self.bot.attack_technique(2) # items
            await self.bot.move(1.25, 2000)
            await self.bot.posfix(1.25, 1000)
            await self.bot.move(0.55, 3000)
            await self.bot.move(1.0, 900)
            await self.bot.attack_technique(6) # items
            await self.bot.move(1.25, 2000)
            await self.bot.posfix(1.25, 1000)
            await self.bot.move(0.3, 3000)
            await self.bot.move(0.2, 1000)
            await self.bot.move(0.5, 300)
            await self.bot.attack_technique(4) # +2TP
        else:
            raise SystemExit(f'no {tp} TP restore available')


