import asyncio as aio
from logger import logger
from automation.bot import Bot
from datetime import datetime as dt
from sys import exit

class World:
    def __init__(self, bot):
        self.bot = bot


    async def farm_dewlight_pavilion(self):
        x = self.Dewlight_Pavilion(bot=self.bot)
        # await x.teleport()
        # await x.path_1()
        # await x.path_2()
        # await x.path_3()
        # await x.path_4()
        # await x.path_5()
        # await x.path_6()
        # await x.path_7()
        # await x.path_8()
        await x.path_99()
    class Dewlight_Pavilion:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Dewlight Pavilion")
            logger.info('---')
            # await self.bot.switch_map(y=808/1080, world='penacony', scroll_down=True)
            # await self.bot.use_teleporter(801/2400, 569/1080, move_x=0, move_y=0, corner='botright', open_map=False) # Reception Counter
            await self.bot.movepi(0.67, 3600)
            await self.bot.attack()
        async def path_99(self):
            logger.info('### Path 1 ###')
            await self.bot.use_teleporter(801/2400, 569/1080, move_x=0, move_y=0, corner='botright') # Reception Counter
            # await self.bot.attack_technique(4)
            # await self.bot.restore_tp(n=1) # +2 TP

    async def farm_clock_studios_theme_park(self):
        x = self.Clock_Studios_Theme_Park(bot=self.bot)
        # await x.teleport()
        # await x.path_0()
        # await x.path_1()
        # await x.path_2()
        # await x.path_3()
        # await x.path_4()
        # await x.path_5()
        # await x.path_6()
        # await x.path_7()
        # await x.path_8()
        # await x.path_9()
        # await x.path_10()
        # await x.path_11()
        # await x.path_12()
        # await x.path_13()
        await x.path_14()
    class Clock_Studios_Theme_Park:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info('--- Map: Clock Studios Theme Park')
            logger.info('---')
            await self.bot.switch_map(y_list=925/1080, world='penacony', scroll_down=True,
                                      x=1100/2400, y=423/1080, move_x=3, move_y=3) # Bud of Preservation
            await self.bot.movepi(1.7, 2500)
            await self.bot.attack() # +2 TP
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
            logger.info('### Path 1 ###')
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
            logger.info('### Path 2 ###')
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
            logger.info('### Path 3 ###')
            await self.bot.use_teleporter(1209/2400, 276/1080, move_x=1, move_y=6, confirm=True) # Theme Park Entrance
            await self.bot.movepi(0.7, 8300)
            await self.bot.movepi(0.5, 12800)
            await self.bot.movepi(0.8, 1800)
            await self.bot.attack() # +2 TP
            await self.bot.movepi(0.7, 800)
            await self.bot.attack_technique(4)
        async def path_4(self):
            logger.info('### Path 4 ###') # roamer
            await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
            await self.bot.movepi(0.7, 4400)
            await self.bot.movepi(1.0, 800)
            await self.bot.attack_technique(5)
        async def path_5(self):
            logger.info('### Path 5 ###')
            await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
            await self.bot.movepi(0.75, 4500)
            await self.bot.movepi(0.99, 1800)
            await self.bot.movepi(0.5, 300)
            await self.bot.attack_technique(8)
        async def path_6(self):
            logger.info('### Path 6 ###')
            await self.bot.use_teleporter(929/2400, 549/1080, corner='topleft', move_x=0, move_y=7) # Screening Area Entrance
            await self.bot.movepi(0.6, 2500)
            await self.bot.attack() # +2 TP
        async def path_7(self):
            logger.info('### Path 7 ###')
            await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
            await self.bot.movepi(0.75, 4500)
            await self.bot.movepi(0.99, 2000)
            await self.bot.movepi(0.7, 2000)
            await self.bot.attack_technique(2, wait=False)
            await self.bot.movepi(1.45, 1000)
            await self.bot.attack_technique(4)
            await self.bot.restore_tp(n=2) # +4 TP
        async def path_8(self):
            logger.info('### Path 8 ###')
            await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
            await self.bot.movepi(0.49, 7000)
            await self.bot.movepi(0.01, 5500)
            await self.bot.movepi(0.5, 500)
            await self.bot.attack() # items
            await self.bot.movepi(0.52, 4500)
            await self.bot.attack_technique(4)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_9(self):
            logger.info('### Path 9 ###')
            await self.bot.use_teleporter(539/2400, 455/1080, move_x=1, move_y=1) # Hanu Gang Place
            await self.bot.movepi(0.00, 5000)
            await self.bot.movepi(1.47, 4000)
            await self.bot.attack_technique(3)
        async def path_10(self):
            logger.info('### Path 10 ###') # roamer
            await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
            await self.bot.movepi(1.55, 3500)
            await self.bot.movepi(1.35, 1500)
            await self.bot.movepi(1.2, 1000)
            await self.bot.attack_technique(8)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_11(self):
            logger.info('### Path 11 ###')
            await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
            await self.bot.movepi(1.58, 7000)
            await self.bot.attack_technique(2)
        async def path_12(self):
            logger.info('### Path 12 ###')
            await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
            await self.bot.movepi(0.2, 3000)
            await self.bot.movepi(1.98, 4500)
            await self.bot.attack()
            await self.bot.movepi(0.4, 1000)
            await self.bot.movepi(0.55, 1500)
            await self.bot.attack_technique(2, wait=False)
            await self.bot.movepi(0.5, 2000)
            await self.bot.attack_technique(2)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_13(self):
            logger.info('### Path 13 ###') # roamer
            await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
            await self.bot.movepi(0.51, 3000)
            await self.bot.movepi(0.6, 3100)
            await self.bot.movepi(0.57, 2100)
            await self.bot.attack()
            await self.bot.movepi(0.05, 2300)
            await self.bot.attack_technique(4, wait=False)
            await self.bot.movepi(0.0, 1000)
            await self.bot.attack_technique(4, wait=False)
            await self.bot.movepi(1.8, 2000)
        async def path_14(self):
            logger.info('### Path 14 ###') # TP regeneration
            await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
            await self.bot.movepi(0.25, 2000)
            await self.bot.movepi(0.05, 9000)
            await self.bot.attack()
            await self.bot.movepi(1.55, 6000)
            await self.bot.movepi(0.05, 600)
            await self.bot.attack() # +2 TP
        async def path_15(self):
            logger.info('### Path 14 ###') # roamer
            await self.bot.use_teleporter(490/2400, 633/1080, move_x=1, move_y=1, corner='topright') # Hamster Ball Park
            await self.bot.movepi(0.51, 3000)
            await self.bot.movepi(0.6, 3100)
            await self.bot.movepi(0.57, 3100)
            await self.bot.movepi(0.1, 2000)
            await self.bot.attack_technique(2, wait=False)
            await self.bot.movepi(1.95, 500)
            await self.bot.attack_technique(6, wait=False)
            await self.bot.restore_tp(n=1) # +2 TP


    async def farm_dreams_edge(self):
        x = self.Dreams_Edge(bot=self.bot)
        # await x.teleport()
        # await x.path_1()
        # await x.path_2()
        # await x.path_3()
        # await x.path_4()
        # await x.path_5() # TODO: can be better
        # await x.path_6() # TODO: can be better
        # await x.path_7()
        # await x.path_8()
        # await x.path_9()
        # await x.path_10()
        await x.path_11()
    class Dreams_Edge:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Dream's Edge")
            logger.info('---')
            await self.bot.switch_map(y_list=771/1080, world='penacony', scroll_down=False,
                                      x=543/2400, y=503/1080, move_x=3, move_y=1, corner='topright', confirm=True) # The Family's Construction Authority
        async def path_1(self):
            logger.info('### Path 1 ###')
            await self.bot.use_teleporter(543/2400, 503/1080, move_x=3, move_y=1, corner='topright', confirm=True) # The Family's Construction Authority
            await self.bot.movepi(0.25, 3000)
            await self.bot.movepi(0.5, 8500)
            await self.bot.attack() # +2 TP
            await self.bot.movepi(1.05, 5800)
            await self.bot.attack_technique(5)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_2(self):
            logger.info('### Path 2 ###')
            await self.bot.use_teleporter(933/2400, 535/1080, move_x=0, move_y=5, corner='topright') # Dreamweaver Plaza
            await self.bot.movepi(1.97, 4000)
            await self.bot.attack_technique(2)
        async def path_3(self):
            logger.info('### Path 3 ###')
            await self.bot.use_teleporter(933/2400, 535/1080, move_x=0, move_y=5, corner='topright') # Dreamweaver Plaza
            await self.bot.movepi(0.25, 1500)
            await self.bot.movepi(0.5, 4500)
            await self.bot.movepi(0.00, 3700)
            await self.bot.movepi(0.49, 5500)
            await self.bot.attack_technique(4)
            await self.bot.restore_tp(n=2) # +4 TP
        async def path_4(self):
            logger.info('### Path 4 ###')
            await self.bot.use_teleporter(933/2400, 535/1080, move_x=0, move_y=5, corner='topright') # Dreamweaver Plaza
            await self.bot.movepi(0.25, 1500)
            await self.bot.movepi(0.5, 4500)
            await self.bot.movepi(0.00, 3700)
            await self.bot.movepi(0.5, 11000)
            await self.bot.attack_technique(8)
        async def path_5(self):
            logger.info('### Path 5 ###')
            await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
            await self.bot.movepi(0.9, 1000)
            await self.bot.attack() # +2 TP
            await self.bot.movepi(1.0, 1600)
            await self.bot.movepi(0.5, 2400)
            await self.bot.movepi(0.9, 900)
            await self.bot.attack_technique(1, wait=False)
            await self.bot.movepi(0.05, 400)
            await self.bot.attack_technique(10)
            await self.bot.restore_tp(n=2) # +2 TP
        async def path_6(self):
            logger.info('### Path 6 ###')
            await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
            await self.bot.movepi(0.5, 3500)
            await self.bot.movepi(0.00, 2500)
            await self.bot.movepi(1.90, 1800)
            await self.bot.movepi(0.4, 100)
            await self.bot.attack_technique(3)
        async def path_7(self):
            logger.info('### Path 7 ###')
            await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
            await self.bot.movepi(0.5, 3500)
            await self.bot.movepi(0.00, 2800)
            await self.bot.movepi(0.5, 1000)
            await self.bot.attack_technique(5)
        async def path_8(self):
            logger.info('### Path 8 ###')
            await self.bot.use_teleporter(764/2400, 253/1080, move_x=2, move_y=3, corner='botright') # Rooftop Garden
            await self.bot.movepi(0.5, 5000)
            await self.bot.movepi(0.75, 1500)
            await self.bot.movepi(0.5, 3000)
            await self.bot.movepi(0.95, 2200)
            await self.bot.attack_technique(5)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_9(self):
            logger.info('### Path 9 ###')
            await self.bot.use_teleporter(658/2400, 738/1080, move_x=0, move_y=7, corner='botleft') # Bud of Memories
            await self.bot.movepi(1.5, 1500)
            await self.bot.attack_technique(4)
        async def path_10(self):
            logger.info('### Path 10 ###')
            await self.bot.use_teleporter(658/2400, 738/1080, move_x=0, move_y=7, corner='botleft') # Bud of Memories
            await self.bot.movepi(1.25, 2750)
            await self.bot.movepi(0.75, 1500)
            await self.bot.movepi(1.0, 1500)
            await self.bot.attack_technique(4)
        async def path_11(self):
            logger.info('### Path 11 ###')
            # await self.bot.use_teleporter(655/2400, 293/1080, move_x=0, move_y=7, corner='botleft') # Front Observation Deck
            await self.bot.use_teleporter(909/2400, 345/1080, move_x=0, move_y=7, corner='botleft') # Shape of Roast
            await self.bot.movepi(1.5, 3000)
            await self.bot.movepi(0.05, 1300)
            await self.bot.attack() # +2 TP
            await self.bot.movepi(1.3, 500)
            await self.bot.attack_technique(8)


    async def farm_childs_dream(self):
        x = self.Childs_Dream(bot=self.bot)
        await x.teleport()
        await x.path_1()
        await x.path_2()
        await x.path_3()
        await x.path_4()
        await x.path_5()
        await x.path_6()
        await x.path_7()
        await x.path_8()
    class Childs_Dream:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Childs's Dream")
            logger.info('---')
            await self.bot.switch_map(y_list=893/1080, world='penacony', scroll_down=False,
                                      x=962/2400, y=356/1080, move_x=0, move_y=0, corner='botright', confirm=False) # Eddying Dreamscape
            await self.bot.movepi(1.9, 1600)
            await self.bot.attack() # +2 TP
        async def path_1(self):
            logger.info('### Path 1 ###')
            await self.bot.use_teleporter(1010/2400, 304/1080, move_x=0, move_y=4, corner='botright') # Corridor of Memories
            await self.bot.movepi(0.25, 2000)
            await self.bot.movepi(0.00, 2000)
            await self.bot.movepi(0.5, 1000)
            await self.bot.movepi(0.25, 1100)
            await self.bot.movepi(0.00, 250)
            await self.bot.attack_technique(6)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_2(self):
            logger.info('### Path 2 ###')
            await self.bot.use_teleporter(1010/2400, 304/1080, move_x=0, move_y=4, corner='botright') # Corridor of Memories
            await self.bot.movepi(1.5, 9300)
            await self.bot.movepi(1.0, 7000)
            await self.bot.attack()
            await self.bot.movepi(1.5, 500)
            await self.bot.attack_technique(6)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_3(self):
            logger.info('### Path 3 ###')
            await self.bot.use_teleporter(1010/2400, 304/1080, move_x=0, move_y=4, corner='botright', penacony=True) # Corridor of Memories
            await self.bot.movepi(1.5, 9300)
            await self.bot.movepi(1.0, 5500)
            await self.bot.movepi(1.2, 1100)
            await self.bot.movepi(1.5, 6300)
            await self.bot.attack_technique(8)
            await self.bot.restore_tp(n=2) # +4 TP
        async def path_4(self):
            logger.info('### Path 4 ###')
            await self.bot.use_teleporter(1010/2400, 304/1080, move_x=0, move_y=4, corner='botright', penacony=True) # Corridor of Memories
            await self.bot.movepi(1.5, 9300)
            await self.bot.movepi(1.0, 5500)
            await self.bot.movepi(1.2, 1300)
            await self.bot.movepi(1.5, 7200)
            await self.bot.interact()
            await self.bot.movepi(1.5, 1700)
            await self.bot.movepi(1.0, 2000)
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
            await self.bot.attack_technique(5)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_5(self):
            logger.info('### Path 5 ###')
            await self.bot.use_teleporter(1010/2400, 304/1080, move_x=0, move_y=4, corner='botright', penacony=True) # Corridor of Memories
            await self.bot.movepi(1.5, 9300)
            await self.bot.movepi(1.0, 5500)
            await self.bot.movepi(1.2, 1300)
            await self.bot.movepi(1.5, 7200)
            await self.bot.interact()
            await self.bot.movepi(1.5, 1700)
            await self.bot.movepi(1.0, 2000)
            await self.bot.action_button()
            await self.bot.movepi(1.0, 2600)
            await self.bot.movepi(0.5, 2300)
            await self.bot.movepi(1.0, 1400)
            await self.bot.movepi(0.5, 2200)
            await self.bot.action_button()
            await self.bot.movepi(0.46, 4700)
            await self.bot.movepi(0.0, 1600)
            await self.bot.action_button()
            await self.bot.movepi(0.0, 3000)
            await self.bot.movepi(0.5, 5000)
            await self.bot.movepi(1.0, 1300)
            await self.bot.movepi(0.5, 3000)
            await self.bot.movepi(0.8, 1200)
            await self.bot.interact()
            await self.bot.movepi(1.2, 1100)
            await self.bot.action_button()
            await self.bot.movepi(1.0, 2900)
            await self.bot.movepi(0.5, 3000)
            await self.bot.action_button()
            await self.bot.movepi(0.5, 2000)
            await self.bot.movepi(1.0, 1600)
            await self.bot.movepi(1.5, 3000)
            await self.bot.attack_technique(6)
        async def path_6(self):
            logger.info('### Path 6 ###')
            await self.bot.use_teleporter(962/2400, 356/1080, move_x=0, move_y=0, corner='botright', penacony=True) # Eddying Dreamscape
            await self.bot.movepi(1.5, 4000)
            await self.bot.movepi(1.8, 800)
            await self.bot.attack_technique(4)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_7(self):
            logger.info('### Path 7 ###')
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
        async def path_8(self):
            logger.info('### Path 8 ###')
            await self.bot.use_teleporter(1122/2400, 617/1080, move_x=0, move_y=0, corner='botright', penacony=True) # Clock Factory
            await self.bot.movepi(0.5, 5000)
            await self.bot.movepi(1.0, 600)
            await self.bot.attack()
            await self.bot.movepi(1.3, 800)
            await self.bot.movepi(1.0, 1500)
            await self.bot.attack_technique(3)
        

    async def farm_the_reverie_dreamscape(self):
        x = self.The_Reverie_Dreamscape(bot=self.bot)
        # await x.teleport()
        # await x.path_1()
        # await x.path_2()
        # await x.path_3()
        # await x.path_4()
        # await x.path_5()
        # await x.path_6()
        # await x.path_7()
        # await x.path_8()
        await x.path_99()
    class The_Reverie_Dreamscape:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: The Reverie (Dreamscape)")
            logger.info('---')
            await self.bot.switch_map(y=681/1080, world='penacony', scroll_down=True)
            await self.bot.use_teleporter(1165/2400, 429/1080, move_x=0, move_y=5, corner='botright', open_map=False) # Path of Dreamdive
            await self.bot.movepi(1.6, 800) # +2 TP
            await self.bot.attack()
        async def path_1(self):
            logger.info('### Path 1 ###')
            await self.bot.use_teleporter(1133/2400, 634/1080, move_x=0, move_y=7, corner='topright', confirm=True) # Platinum Guest Room
            await self.bot.movepi(0.5, 2800)
            await self.bot.movepi(1.0, 1200)
            await self.bot.attack()
            await self.bot.movepi(1.0, 12000)
            await self.bot.movepi(0.5, 2900)
            await self.bot.movepi(0.7, 3800)
            await self.bot.attack_technique(20)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_2(self):
            logger.info('### Path 2 ###')
            await self.bot.use_teleporter(1133/2400, 634/1080, move_x=0, move_y=7, corner='topright', confirm=True) # Platinum Guest Room
            await self.bot.movepi(0.5, 2600)
            await self.bot.movepi(1.0, 5900)
            await self.bot.attack()
            await self.bot.movepi(0.9, 700)
            await self.bot.movepi(1.0, 6100)
            await self.bot.movepi(0.5, 3000)
            await self.bot.movepi(0.25, 1500)
            await self.bot.movepi(0.56, 6500)
            await self.bot.attack_technique(5)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_3(self):
            logger.info('### Path 3 ###')
            await self.bot.use_teleporter(864/2400, 506/1080, move_x=0, move_y=5, corner='botright') # Bud of Treasures
            await self.bot.movepi(1.5, 500)
            await self.bot.movepi(1.9, 1900)
            await self.bot.movepi(0.0, 1800)
            await self.bot.movepi(1.5, 1200)
            await self.bot.attack()
            await self.bot.movepi(0.48, 6400)
            await self.bot.attack()
        async def path_4(self):
            logger.info('### Path 4 ###')
            await self.bot.use_teleporter(1133/2400, 634/1080, move_x=0, move_y=7, corner='topright', confirm=True) # Platinum Guest Room
            await self.bot.movepi(0.5, 2800)
            await self.bot.movepi(1.0, 28000)
            await self.bot.movepi(1.25, 1200)
            await self.bot.movepi(1.5, 1000)
            await self.bot.attack_technique(3)
            await self.bot.movepi(0.6, 1800)
            await self.bot.attack_technique(5)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_5(self):
            logger.info('### Path 5 ###')
            await self.bot.use_teleporter(1133/2400, 634/1080, move_x=0, move_y=7, corner='topright', penacony=True, confirm=True) # Platinum Guest Room
            await self.bot.movepi(0.5, 2800)
            await self.bot.movepi(1.0, 28000)
            await self.bot.movepi(0.69, 2600)
            await self.bot.attack_technique(8)
        async def path_6(self):
            logger.info('### Path 6 ###')
            await self.bot.use_teleporter(1133/2400, 634/1080, move_x=0, move_y=7, corner='topright', penacony=True, confirm=True) # Platinum Guest Room
            await self.bot.movepi(0.5, 2800)
            await self.bot.movepi(1.0, 28000)
            await self.bot.movepi(1.1, 700)
            await self.bot.interact()
            await self.bot.movepi(1.5, 2000)
            await self.bot.movepi(1.3, 1800)
            await self.bot.action_button()
            await self.bot.movepi(1.5, 2000)
            await self.bot.movepi(0.0, 2000)
            await self.bot.attack_technique(8)
            await self.bot.restore_tp(n=1) # +2 TP
        async def path_7(self):
            logger.info('### Path 7 ###')
            await self.bot.use_teleporter(1133/2400, 634/1080, move_x=0, move_y=7, corner='topright', penacony=True, confirm=True) # Platinum Guest Room
            await self.bot.movepi(0.5, 2800)
            await self.bot.movepi(1.0, 28000)
            await self.bot.movepi(1.1, 700)
            await self.bot.interact()
            await self.bot.movepi(1.5, 2000)
            await self.bot.movepi(1.3, 1800)
            await self.bot.action_button()
            await self.bot.movepi(1.5, 2000)
            await self.bot.movepi(0.0, 3500)
            await self.bot.action_button()
            await self.bot.movepi(1.5, 2100)
            await self.bot.movepi(1.05, 2900)
            await self.bot.attack_technique(4)
        async def path_99(self):
            logger.info('### Path 8 ###')
            # await self.bot.use_teleporter(1133/2400, 634/1080, move_x=0, move_y=7, corner='topright', penacony=True, confirm=True) # Platinum Guest Room
            # await self.bot.attack_technique(4)
            # await self.bot.restore_tp(n=1) # +2 TP
            

    async def farm_reverie_dreamscape(self):
        logger.info('### group 6 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1620/2400, 352/1080, move_x=-0.1, move_y=0.2, open_map=False) # Platinum Guest Room
        await self.bot.movepi(0.5, 2800)
        await self.bot.movepi(1.0, 13000)
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.25, 1500)
        await self.bot.movepi(0.56, 6000)
        await self.bot.movepi(0.5, 3300)
        await self.bot.movepi(0.9, 2300)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 6, part 2 ###') # roamer
        await self.bot.movepi(0.9, 1000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 7 ###')
        await self.bot.use_teleporter(687/2400, 666/1080, move_x=0.2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 4800)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 7, part 2 ###') # roamer
        await self.bot.attack()
        await self.bot.wait_for_onmap(min_duration=3)
        logger.info('### group 8 ###')
        await self.bot.use_teleporter(754/2400, 160/1080)
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 8200)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 9 ###')
        await self.bot.use_teleporter(990/2400, 250/1080)
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 5500)
        await self.bot.movepi(0.92, 4400)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 9, part 2 ###') # roamer
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 10 ###') # roamer
        await self.bot.use_teleporter(1020/2400, 200/1080)
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 5500)
        await self.bot.movepi(0.75, 4000)
        await self.bot.movepi(0.5, 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 11 ###')
        await self.bot.use_teleporter(1100/2400, 245/1080) # VIP Lounge Corridor
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 5500)
        await self.bot.movepi(0.9, 2000)
        await self.bot.movepi(1.0, 3000)
        await self.bot.movepi(1.1, 2000)
        await self.bot.sleep(2)
        await self.bot.movepi(1.1, 500)
        await self.bot.movepi(1.0, 5500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.1, 600)
        await self.bot.movepi(1.0, 7000)
        await self.bot.movepi(0.5, 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 11, part 2 ###')
        await self.bot.movepi(1.25, 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 12 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(980/2400, 230/1080, open_map=False, move_y=0.35) # VIP Lounge Corridor
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
        await self.bot.movepi(1.15, 2300)
        await self.bot.movepi(1, 300)
        await self.bot.interact()
        await self.bot.movepi(0.4, 200)
        await self.bot.movepi(0.5, 3800)
        await self.bot.movepi(0.6, 600)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 3500)
        await self.bot.movepi(1.3, 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 13 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(980/2400, 215/1080, open_map=False, move_y=0.35) # VIP Lounge Corridor
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
        await self.bot.movepi(1.15, 2300)
        await self.bot.movepi(1, 300)
        await self.bot.interact()
        await self.bot.movepi(1.5, 3000)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 2100)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 2100)
        await self.bot.action_button()
        await self.bot.movepi(0.5, 3000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 14 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(980/2400, 220/1080, open_map=False, move_y=0.35) # VIP Lounge Corridor
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
        await self.bot.movepi(1.15, 2300)
        await self.bot.movepi(1, 300)
        await self.bot.interact()
        await self.bot.movepi(1.5, 3000)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 2100)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 2100)
        await self.bot.action_button()
        await self.bot.movepi(0.5, 5000)
        await self.bot.movepi(0.26, 1300)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 15 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(980/2400, 200/1080, open_map=False, move_y=0.35) # VIP Lounge Corridor
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
        await self.bot.movepi(1.15, 2300)
        await self.bot.movepi(1, 300)
        await self.bot.interact()
        await self.bot.movepi(0.5, 900)
        await self.bot.movepi(1.0, 6000)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 2100)
        await self.bot.movepi(0.5, 3400)
        await self.bot.action_button()
        await self.bot.movepi(0.5, 3000)
        await self.bot.sleep(1) # wait for monster to spawn
        await self.bot.movepi(0.6, 500)
        await self.bot.attack()
        await self.bot.sleep(0.3) # in case destrucible is hit
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 16 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(981/2400, 148/1080, open_map=False, move_y=0.30) # VIP Lounge Corridor
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
        await self.bot.movepi(1.15, 2300)
        await self.bot.movepi(1, 300)
        await self.bot.interact()
        await self.bot.movepi(0.5, 900)
        await self.bot.movepi(1.0, 6000)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 2100)
        await self.bot.movepi(0.5, 3400)
        await self.bot.action_button()
        await self.bot.movepi(0.5, 2500)
        await self.bot.movepi(0.55, 700)
        await self.bot.movepi(0.7, 1200)
        await self.bot.movepi(0.5, 600)
        await self.bot.movepi(0.2, 1200)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 17 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(895/2400, 133/1080, move_y=1.0, open_map=False) # Dreamjolt Hostelry
        await self.bot.movepi(0.5, 7500)
        await self.bot.movepi(1.0, 500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 18 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1015/2400, 155/1080, open_map=False, move_y=0.1) # Dreamjolt Hostelry
        await self.bot.movepi(0.5, 7500)
        await self.bot.movepi(1.0, 500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.sleep(2)
        await self.bot.movepi(0.9, 1300)
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(0.95, 1100)
        await self.bot.movepi(1.5, 3800)
        await self.bot.movepi(0.00, 1200)
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(0.00, 4200)
        await self.bot.movepi(1.70, 2700)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 19 ###') # roamer
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1015/2400, 213/1080, open_map=False, move_y=0.15) # Dreamjolt Hostelry
        await self.bot.movepi(0.5, 7500)
        await self.bot.movepi(1.0, 500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.sleep(2)
        await self.bot.movepi(0.9, 1300)
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(0.95, 1100)
        await self.bot.movepi(1.5, 3800)
        await self.bot.movepi(0.00, 1200)
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(0.00, 2400)
        await self.bot.attack()
        await self.bot.sleep(0.5)
        await self.bot.movepi(1.49, 1800)
        await self.bot.interact()
        await self.bot.movepi(0.5, 4300)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 1800)
        await self.bot.movepi(1.1, 1000)
        await self.bot.interact()
        await self.bot.movepi(0.1, 1000)
        await self.bot.movepi(0.0, 1100)
        await self.bot.action_button()
        await self.bot.movepi(0.00, 1000)
        await self.bot.movepi(1.7, 800)
        await self.bot.movepi(1.5, 4200)
        await self.bot.movepi(1.7, 1300)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(0.00, 3200)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 20 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1015/2400, 220/1080, open_map=False, move_y=0.15) # Dreamjolt Hostelry
        await self.bot.movepi(0.5, 7500)
        await self.bot.movepi(1.0, 500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.sleep(2)
        await self.bot.movepi(0.9, 1300)
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(0.95, 1100)
        await self.bot.movepi(1.5, 3800)
        await self.bot.movepi(0.00, 1200)
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(0.00, 2400)
        await self.bot.movepi(1.49, 1800)
        await self.bot.interact()
        await self.bot.movepi(0.5, 4300)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 1800)
        await self.bot.movepi(1.1, 1000)
        await self.bot.interact()
        await self.bot.movepi(0.1, 1000)
        await self.bot.movepi(0.0, 1100)
        await self.bot.action_button()
        await self.bot.movepi(0.00, 1000)
        await self.bot.movepi(1.7, 800)
        await self.bot.movepi(1.5, 4200)
        await self.bot.movepi(1.7, 1300)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(0.0, 6200)
        await self.bot.action_button()
        await self.bot.movepi(0.0, 2100)
        await self.bot.movepi(0.19, 2100)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 21 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1100/2400, 815/1080, open_map=False, move_y=-0.1) # VIP Lounge Corridor
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 2000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 22 ###') # roamer
        await self.bot.use_teleporter(1100/2400, 450/1080) # VIP Lounge Corridor
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 4900)
        await self.bot.movepi(0.00, 2500)
        await self.bot.attack() # TODO: For Acheron, kill with skill and grab energy afterwards
        await self.bot.wait_for_onmap()
        logger.info('### group 23 ###')
        await self.bot.use_teleporter(871/2400, 164/1080) # Monitoring Room
        await self.bot.movepi(0.5, 1000)
        await self.bot.movepi(0.25, 4700)
        await self.bot.movepi(0.00, 6700)
        await self.bot.movepi(1.5, 7000)
        await self.bot.movepi(1.25, 1200)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger.info('### group 23, part 2 ###') # roamer
        await self.bot.movepi(1.2, 1000)
        await self.bot.attack()
        await self.bot.wait_for_onmap(min_duration=3)

    async def farm_golden_hour(self):
        x = self.Golden_Hour(bot=self.bot)
        await x.teleport()
        await x.path_1()
    class Golden_Hour:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info('--- Map: Golden Hour')
            logger.info('---')
            await self.bot.switch_map(y_list=650/1080, world='penacony',
                                      x=588/2400, y=356/1080, move_x=4, move_y=3,) # Sweet Corner
            await self.bot.movepi(1.6, 5000)
            await self.bot.movepi(1.25, 3000)
            await self.bot.attack()
        async def path_1(self):
            logger.info('### Path 1 ###')
            await self.bot.use_teleporter(815/2400, 245/1080, corner='botright', move_x=0, move_y=2) # Oti Mall
            await self.bot.movepi(0.7, 2000)
            await self.bot.movepi(0.9, 4400)
            await self.bot.attack()

    