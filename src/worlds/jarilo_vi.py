import asyncio as aio
from logger import logger
from automation.bot import Bot
from datetime import datetime as dt
from sys import exit

class World:
    def __init__(self, bot):
        self.bot = bot

    async def farm_outlying_snow_plains(self):
        x = self.Outlying_Snow_Plains(bot=self.bot)
        await x.teleport()
        await x.path_1()
        await x.path_2()
    class Outlying_Snow_Plains:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Outlying Snow Plains")
            logger.info('---')
            await self.bot.switch_map(y_list=508/1080, world='jarilo_vi', scroll_down=False,
                                      x=1079/2400, y=430/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Bud of Memories
            await self.bot.movepi(1.3, 3000)
            await self.bot.attack_technique(2, wait=False) # +2 TP
            await self.bot.movepi(1.1, 1000)
            await self.bot.attack_technique(10)
        async def path_1(self):
            logger_set_path(1)
            await self.bot.use_teleporter(x=998/2400, y=338/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Long Slope
            await self.bot.movepi(0.21, 2100)
            await self.bot.attack()
            await self.bot.movepi(1.2, 6300)
            await self.bot.attack()
            await self.bot.movepi(0.95, 4700)
            await self.bot.attack_technique(2)
        async def path_2(self):
            logger_set_path(2)
            await self.bot.use_teleporter(x=998/2400, y=338/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Long Slope
            await self.bot.movepi(0.61, 2900)
            await self.bot.attack() # +2 TP
            await self.bot.movepi(0.58, 5400)
            await self.bot.attack() # +2 TP
            await self.bot.movepi(0.65, 9000)
            await self.bot.attack_technique(2, wait=False) # items
            await self.bot.movepi(1.00, 1000)
            await self.bot.movepi(0.6, 100)
            await self.bot.attack_technique(3, wait=False)
            await self.bot.restore_tp(n=1) # +2 TP
            exit() # improve path
            await self.bot.movepi(1.4, 5500)
            await self.bot.attack_technique(6, wait=False)
            await self.bot.movepi(0.64, 4400)
            await self.bot.attack_technique(1, wait=False)
            await self.bot.movepi(0.42, 5200)
            await self.bot.attack_technique(2)
    
    async def farm_backwater_pass(self):
        x = self.Backwater_Pass(bot=self.bot)
        # await x.teleport()
        # await x.path_1()
        await x.path_99()
    class Backwater_Pass:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Backwater Pass")
            await self.bot.switch_map(y_list=629/1080, world='jarilo_vi', scroll_down=False,
                                      x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
            await self.bot.movepi(0.8, 700)
            await self.bot.attack() # +2 TP
            await self.bot.movepi(1.53, 5000)
            await self.bot.movepi(1.1, 300)
            await self.bot.attack() # items
            await self.bot.movepi(1.5, 700)
            await self.bot.movepi(1.03, 2300)
            await self.bot.attack() # items
            await self.bot.movepi(0.97, 2500)
            await self.bot.attack_technique(4)
        async def path_99(self):
            logger_set_path(1)
            await self.bot.use_teleporter(x=829/2400, y=273/1080, corner='botright', move_x=0, move_y=0) # Transport Hub
            await self.bot.movepi(1.5, 6000)
            await self.bot.movepi(1.75, 3000)
            await self.bot.movepi(0.4, 300)
            await self.bot.attack_technique(4, wait=False)
            await self.bot.movepi(0.3, 1500)
            await self.bot.attack_technique(4, wait=False)
            exit() # check rest
            await self.bot.movepi(0.4, 1000)
            await self.bot.attack_technique(4)
        async def path_99(self):
            logger_set_path(1)
            await self.bot.use_teleporter(x=907/2400, y=753/1080, corner='topright', move_x=0, move_y=1, confirm=True) # Bud of Abundance
            # await self.bot.use_teleporter(x=945/2400, y=715/1080, corner='topright', move_x=0, move_y=1, confirm=True) # Leisure Plaza
            # await self.bot.use_teleporter(x=830/2400, y=360/1080, corner='topright', move_x=0, move_y=1) # Bud of Aether
            
    # async def farm_backwater_pass(self):
    #     logger('### group 2 ###')
    #     await self.bot.use_teleporter(846/2400, 386/1080) # Transport Hub
    #     await self.bot.movepi(1.5, 6000)
    #     await self.bot.movepi(1.75, 3000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 2, part 2 ###') # roamer
    #     await self.bot.movepi(1.5, 500)
    #     await self.bot.movepi(0.00, 2000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 3 ###')
    #     await self.bot.movepi(0.00, 7500)
    #     await self.bot.movepi(0.5, 3600)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 4 ###')
    #     await self.bot.use_teleporter(978/2400, 341/1080, confirm=True)
    #     await self.bot.movepi(1.5, 6000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 5 ###')
    #     await self.bot.movepi(1.5, 2500)
    #     await self.bot.movepi(1.75, 1500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()

            

    async def farm_silvermane_guard(self):
        x = self.Silvermane_Guard(bot=self.bot)
        # await x.teleport()
        # await x.path_1()
        await x.path_99()
    class Silvermane_Guard:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Silvermane Guard Restricted Zone")
            logger.info('---')
            await self.bot.switch_map(y_list=750/1080, world='jarilo_vi', scroll_down=False,
                                      x=659/2400, y=648/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Energy Hub
            await self.bot.movepi(1.5, 1200)
            await self.bot.movepi(1.05, 1200)
            await self.bot.attack() # items
        async def path_99(self):
            logger_set_path(1)
            await self.bot.use_teleporter(x=659/2400, y=648/1080, corner='botright', move_x=0, move_y=0, confirm=True) # Energy Hub
            await self.bot.movepi(0.5, 2500)
            await self.bot.movepi(0.72, 5200)
            await self.bot.attack()
            await self.bot.movepi(0.75, 3900)
            await self.bot.movepi(1.24, 6300)
            await self.bot.attack()
            await self.bot.movepi(0.6, 3300)
            await self.bot.movepi(0.3, 2500)
            await self.bot.movepi(0.0, 1100)
            await self.bot.attack()
            await self.bot.movepi(1.2, 1000)
            await self.bot.movepi(0.75, 7000)
            await self.bot.attack()

    async def farm_rivet_town(self):
        x = self.Rivet_Town(bot=self.bot)
        await x.teleport()
        # await x.path_1()
        # await x.path_99()
    class Rivet_Town:
        def __init__(self, bot):
            self.bot = bot
        async def teleport(self):
            logger.info('---')
            logger.info("--- Map: Rivet Town")
            logger.info('---')
            await self.bot.switch_map(y_list=808/1080, world='jarilo_vi', scroll_down=True,
                                      x=832/2400, y=597/1080, corner='topleft', move_x=0, move_y=0) # Abandoned Market
            await self.bot.movepi(0.9, 700)
            await self.bot.attack() # +2 TP
        async def path_99(self):
            logger_set_path(1)
            # await self.bot.use_teleporter(x=1044/2400, y=405/1080, corner='topright', move_x=0, move_y=0, debug=True) #
            # await self.bot.movepi(1.5, 3800)
            # await self.bot.attack_technique(10)
    
    
    # async def farm_rivet_town(self):
    #     logger('farm: Rivet Town')
    #     await self.bot.switch_map(807/1080, scroll_down=True)
    #     logger('### group 1 ###')
    #     await self.bot.use_teleporter(1001/2400, 281/1080, open_map=False) # Orphanage
    #     await self.bot.movepi(1.6, 1500)
    #     await self.bot.movepi(1.25, 1000)
    #     await self.bot.movepi(1.1, 1000)
    #     await self.bot.movepi(1.0, 2800)
    #     await self.bot.movepi(0.9, 1000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 2 ###')
    #     await self.bot.use_teleporter(999/2400, 394/1080) # Orphanage
    #     await self.bot.movepi(1.6, 1500)
    #     await self.bot.movepi(1.25, 1000)
    #     await self.bot.movepi(1.1, 1000)
    #     await self.bot.movepi(1.0, 2800)
    #     await self.bot.movepi(0.58, 5000)
    #     await self.bot.movepi(0.50, 8000)
    #     await self.bot.movepi(1.0, 1500)
    #     await self.bot.movepi(0.5, 4000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 3 ###')
    #     await self.bot.use_teleporter(1016/2400, 775/1080, confirm=True)
    #     await self.bot.movepi(0.5, 2500)
    #     await self.bot.movepi(0.0, 2400)
    #     await self.bot.movepi(0.25, 500)
    #     await self.bot.movepi(0.75, 700)
    #     await self.bot.movepi(1.0, 7800)
    #     await self.bot.movepi(0.5, 2400)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 4 ###') # roamer
    #     await self.bot.movepi(0.7, 4000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
        

    # async def farm_robot_settlement(self):
    #     logger('farm: Robot Settlement')
    #     await self.bot.switch_map(927/1080, scroll_down=True)
    #     logger('### group 1 ###')
    #     await self.bot.use_teleporter(626/2400, 678/1080, open_map=False) # Bud of Harmony
    #     await self.bot.movepi(1.75, 1700)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 2 ###')
    #     await self.bot.use_teleporter(766/2400, 533/1080) # Energy Conversion Station
    #     await self.bot.movepi(1.75, 1900)
    #     await self.bot.movepi(1.95, 3500)
    #     await self.bot.movepi(1.75, 1200)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     await self.bot.movepi(0.0, 800)
    #     await self.bot.attack()
    #     await self.bot.sleep(1)
    #     logger('### group 3 ###')
    #     await self.bot.use_teleporter(767/2400, 682/1080) # Energy Conversion Station
    #     await self.bot.movepi(1.75, 1900)
    #     await self.bot.movepi(1.95, 1400)
    #     await self.bot.movepi(1.4, 4000)
    #     await self.bot.movepi(1.5, 2000)
    #     await self.bot.movepi(1.37, 5000)
    #     await self.bot.movepi(1.5, 1300)
    #     await self.bot.movepi(1.3, 1600)
    #     await self.bot.movepi(1.5, 800)
    #     await self.bot.movepi(1.25, 300)
    #     await self.bot.attack()
    #     await self.bot.sleep(0.5)
    #     await self.bot.movepi(1.6, 2300)
    #     await self.bot.movepi(1.4, 1000)
    #     await self.bot.movepi(1.25, 2100)
    #     await self.bot.attack()
    #     await self.bot.sleep(1.0)
    #     await self.bot.movepi(1.25, 700)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 4 ###')
    #     await self.bot.use_teleporter(768/2400, 576/1080) # Energy Conversion Station
    #     await self.bot.movepi(1.75, 1900)
    #     await self.bot.movepi(1.95, 1400)
    #     await self.bot.movepi(1.4, 4000)
    #     await self.bot.movepi(1.5, 2000)
    #     await self.bot.movepi(1.37, 5000)
    #     await self.bot.movepi(1.5, 1300)
    #     await self.bot.movepi(1.3, 1600)
    #     await self.bot.movepi(1.5, 800)
    #     await self.bot.movepi(1.25, 300)
    #     await self.bot.movepi(1.6, 2400)
    #     await self.bot.movepi(1.88, 1400)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 4, part 2 ###')
    #     await self.bot.movepi(1.75, 1200)
    #     await self.bot.movepi(0.4, 1800)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()


    # async def farm_great_mine(self):
    #     logger('farm: Great Mine')
    #     await self.bot.switch_map(687/1080, scroll_down=True)
    #     logger('### group 1 ###')
    #     await self.bot.use_teleporter(955/2400, 818/1080, open_map=False, confirm=True) # Overlook
    #     await self.bot.movepi(1.8, 2000)
    #     await self.bot.movepi(0.1, 4700)
    #     await self.bot.movepi(0.3, 1000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 2 ###')
    #     await self.bot.movepi(0.5, 3000)
    #     await self.bot.movepi(0.28, 700)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 3 ###')
    #     await self.bot.use_teleporter(944/2400, 675/1080, confirm=True) # Bud of Treasures
    #     await self.bot.movepi(1.5, 500)
    #     await self.bot.movepi(1.75, 2000)
    #     await self.bot.movepi(1.9, 2500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 4 ###')
    #     await self.bot.movepi(0.0, 1000)
    #     await self.bot.movepi(0.25, 1900)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 5 ###')
    #     await self.bot.use_teleporter(912/2400, 758/1080) # Main Mine Shaft
    #     await self.bot.movepi(1.05, 2600)
    #     await self.bot.attack()
    #     await self.bot.sleep(0.5)
    #     await self.bot.movepi(1.1, 4100)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 6 ###')
    #     await self.bot.movepi(0.9, 3500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 7 ###')
    #     await self.bot.movepi(0.75, 1500)
    #     await self.bot.movepi(0.3, 1500)
    #     await self.bot.movepi(0.00, 2500)
    #     await self.bot.movepi(1.9, 2000)
    #     await self.bot.movepi(0.25, 2300)
    #     await self.bot.movepi(0.5, 1500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 8 ###')
    #     await self.bot.use_teleporter(950/2400, 482/1080) # Stagnant Shadow
    #     await self.bot.movepi(0.8, 2300)
    #     await self.bot.movepi(1.0, 2000)
    #     await self.bot.movepi(1.12, 3300)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 8, part 2 ###') # roamer, can be finetuned
    #     await self.bot.movepi(0.53, 1500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 9 ###') # roamer
    #     await self.bot.movepi(0.50, 2800)
    #     await self.bot.movepi(0.2, 1500)
    #     await self.bot.movepi(0.75, 500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()

    # async def farm_everwinter_hill(self):
    #     logger('farm: Everwinter Hill')
    #     await self.bot.switch_map(984/1080)
    #     logger('### group 1 ###')
    #     await self.bot.use_teleporter(647/2400, 761/1080, open_map=False, confirm=True) # Ancient Battlefield: Snow Plains
    #     await self.bot.movepi(0.48, 3300)
    #     await self.bot.attack()
    #     await self.bot.sleep(0.5)
    #     await self.bot.movepi(0.5, 3000)
    #     await self.bot.movepi(0.9, 4000)
    #     await self.bot.movepi(1.1, 3000)
    #     await self.bot.movepi(0.95, 900)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 2 ###')
    #     await self.bot.movepi(0.95, 600)
    #     await self.bot.movepi(1.1, 2000)
    #     await self.bot.movepi(0.8, 1800)
    #     await self.bot.movepi(0.85, 2500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 3 ###')
    #     await self.bot.use_teleporter(1054/2400, 683/1080) # Cavern of Corrosion
    #     await self.bot.movepi(1.1, 6000)
    #     await self.bot.movepi(0.75, 700)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 4 ###')
    #     await self.bot.movepi(0.75, 1500)
    #     await self.bot.movepi(0.475, 2200)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()

    # async def farm_corridor(self): # TODO: do battle 4 first
    #     logger('farm: Corridor of Fading Echoes')
    #     await self.bot.switch_map(869/1080)
    #     logger('### group 1 ###') # roamer
    #     await self.bot.use_teleporter(963/2400, 781/1080, open_map=False, move_y=-0.3) # Ancient Battlefield: Frontline
    #     await self.bot.movepi(1.5, 5000)
    #     await self.bot.movepi(1, 4500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 2 ###')
    #     await self.bot.use_teleporter(963/2400, 645/1080) # Ancient Battlefield Frontline
    #     await self.bot.movepi(1.5, 5000)
    #     await self.bot.movepi(1, 3500)
    #     await self.bot.movepi(1.51, 6000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 3 ###')
    #     await self.bot.use_teleporter(963/2400, 622/1080) # Ancient Battlefield Frontline
    #     await self.bot.movepi(1.5, 5000)
    #     await self.bot.movepi(1, 3500)
    #     await self.bot.movepi(1.51, 6000)
    #     await self.bot.movepi(1.6, 2000)
    #     await self.bot.movepi(1.5, 4300)
    #     await self.bot.attack()
    #     await self.bot.sleep(0.5)
    #     await self.bot.movepi(0, 7300)
    #     await self.bot.movepi(0.5, 3500)
    #     await self.bot.attack()
    #     await self.bot.sleep(0.5) # in case attack misses
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 4 ###')
    #     await self.bot.use_teleporter(869/2400, 258/1080, move_y=0.2) # Command Center
    #     await self.bot.movepi(0.375, 5000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 4, part 2 ###') # roamer
    #     await self.bot.movepi(0.6, 1500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap(min_duration=10)
    #     logger('### group 5 ###') # shitty roamer
    #     await self.bot.use_teleporter(909/2400, 136/1080) # Stagnant Shadow
    #     await self.bot.movepi(1, 1000)
    #     await self.bot.movepi(0.75, 1550)
    #     await self.bot.attack()
    #     await self.bot.sleep(0.5)
    #     await self.bot.movepi(0.5, 1500)
    #     await self.bot.movepi(1, 3600)
    #     await self.bot.movepi(0.5, 5500)
    #     await self.bot.movepi(0.25, 3500)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     logger('### group 6 ###') # shitty roamer
    #     await self.bot.use_teleporter(909/2400, 600/1080) # Stagnant Shadow
    #     await self.bot.movepi(1, 1000)
    #     await self.bot.movepi(0.75, 1550)
    #     await self.bot.movepi(0.5, 1500)
    #     await self.bot.movepi(1, 3800)
    #     await self.bot.movepi(0.5, 5500)
    #     await self.bot.movepi(0.25, 6500)
    #     await self.bot.movepi(1.75, 3000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap(min_duration=45)
    #     logger('### group 7 ###') # roamer
    #     await self.bot.use_teleporter(908/2400, 510/1080) # Stagnant Shadow
    #     await self.bot.movepi(1.2, 1800)
    #     await self.bot.movepi(1, 8700)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap(min_duration=30)
    #     logger('### group 8 ###')
    #     await self.bot.use_teleporter(1071/2400, 261/1080) # Cavern of Corrosion
    #     await self.bot.movepi(1.78, 7000)
    #     await self.bot.movepi(1.6, 1000)
    #     await self.bot.attack()
    #     await self.bot.wait_for_onmap()
    #     await self.bot.movepi(0.9, 1000)
    #     await self.bot.attack()
    #     await self.bot.sleep(1)

    