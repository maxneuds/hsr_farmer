from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra
from datetime import datetime as dt
from worlds.penacony.paperfold_university import Paperfold_University


class Dewlight_Pavilion:
    '''
    R2/4: 1 / 1
    '''
    def __init__(self, device):
        self.map = 'Dewlight Pavilion'
        self.bot = Bot(device)
        self.extra = Extra(device)
        self.paperfold_university = Paperfold_University(device)
    async def farm(self):
        t_start = dt.now()
        await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.extra.restore_tp(tp=4, info='Dewlight Pavilion 1')
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.extra.restore_tp(tp=4, info='Dewlight Pavilion 2')
        await self.path_6()
        await self.path_7()
        await self.path_8()
        await self.path_9()
        await self.path_10()
        await self.penacony.paperfold_univeristy.restore_tp(tp=4)
        await self.path_11()
        await self.extra.metrics(self.map, t_start)
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info("--- Map: Dewlight Pavilion")
        logger.info('---')
        await self.bot.switch_map_new(world='penacony', y_list=255/1080, scroll_down=True, # Reception Counter
                                      x=979/2400, y=718/1080, start=1.75, deg=0.0, n=0, confirm=False)
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
        logger_set_path(self.map, 1)
        await self.bot.teleport(x=910/2400, y=707/1080, start=0.75, deg=0.0, n=0) # Dreammaster Hall
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
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.teleport(x=910/2400, y=707/1080, start=0.75, deg=0.0, n=0) # Dreammaster Hall
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
        await self.bot.move(1.75, 1500)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.6, 2800)
        await self.bot.move(0.2, 300)
        await self.bot.action_button()
        await self.bot.move(0.0, 1200)
        await self.bot.move(0.1, 300)
        await self.bot.attack_technique(4) # -1TP, roamer, spawner
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(3) # -2 TP, roamer
        for _ in range(2): # stability & corner
            await self.bot.move(0.25, 300)
            await self.bot.attack_technique(2)
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.restore_tp(item='punitive_energy', n=1) # +4TP
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
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.switch_map_new(world='penacony', y_list=255/1080, scroll_down=True, # Dreammaster Hall
                                      x=910/2400, y=707/1080, start=0.75, deg=0.0, n=0, confirm=False)
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
        await self.bot.move(0.26, 2600)
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
        await self.bot.posfix(0.9, 4500)
        await self.bot.move(1.78, 5800)
        await self.bot.move(1.5, 100)
        await self.bot.attack() # items
        await self.bot.move(0.32, 1700)
        await self.bot.move(0.48, 700)
        await self.bot.attack() # +2TP
        await self.bot.move(1.7, 1700)
        await self.bot.attack_technique(3) # -2TP
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.teleport(x=979/2400, y=718/1080, start=1.75, deg=0.0, n=0) # Reception Counter
        await self.bot.move(0.5, 10350)
        await self.bot.move(0.0, 7000)
        await self.bot.move(1.5, 7000)
        await self.bot.move(1.7, 2100)
        await self.bot.move(1.3, 1900)
        await self.bot.interact()
        await self.bot.move(0.3, 2000)
        await self.bot.move(0.4, 1650)
        await self.bot.action_button()
        await self.bot.move(0.0, 1900)
        await self.bot.move(1.9, 400)
        await self.bot.attack() # +2TP
        await self.bot.move(1.5, 1300)
        await self.bot.move(0.1, 900)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(2) # items
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.teleport(x=979/2400, y=718/1080, start=1.75, deg=0.0, n=0) # Reception Counter
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
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.switch_map_new(world='penacony', y_list=255/1080, scroll_down=True, # Dreammaster Hall
                                      x=910/2400, y=707/1080, start=0.75, deg=0.0, n=0, confirm=False)
        await self.bot.move(0.5, 1000)
        await self.bot.interact()
        await self.bot.move(0.51, 2800)
        await self.bot.attack() # items
        await self.bot.move(0.69, 1500)
        await self.bot.attack() # items
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.move(0.3, 2500)
        await self.bot.move(1.83, 6300)
        await self.bot.move(0.45, 700)
        await self.bot.attack_technique(2) # -1TP
        await self.bot.move(1.8, 300)
        await self.bot.attack_technique(5) # -1TP, roamer
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(5)
        await self.bot.move(1.75, 300)
        await self.bot.attack_technique(6) # items
    async def path_8(self):
        logger_set_path(self.map, 8)
        await self.bot.use_teleporter(1093/2400, 629/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # Shape of Ire
        await self.bot.move(1.2, 1600)
        await self.bot.attack() # items
        await self.bot.move(1.5, 3300)
        await self.bot.move(0.0, 600)
        await self.bot.attack_technique(1) # +2TP
    async def path_9(self):
        logger_set_path(self.map, 9)
        await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.move(0.35, 500)
        await self.bot.attack_technique(14) # move
        await self.bot.move(0.3, 500)
        await self.bot.attack_technique(8) # items
        await self.bot.move(0.3, 1000)
        await self.bot.move(0.1, 500)
        await self.bot.move(0.0, 1700)
        await self.bot.move(0.7, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.75, 1500)
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
        await self.bot.restore_tp('trick_snack', n=1) # +2TP
    async def path_10(self):
        logger_set_path(self.map, 10)
        await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.move(0.5, 11500)
        await self.bot.interact(wait_for_ready=False)
        await self.bot.action_tap(1535, 960)
        await self.bot.wait_for_ready(min_duration=5, reason='use pinball teleporter')
        await self.bot.move(0.51, 5500)
        await self.bot.interact(wait_for_ready=False)
        await self.bot.action_tap(1535, 960)
        await self.bot.wait_for_ready(min_duration=5, reason='use pinball teleporter')
        await self.bot.move(0.47, 2200)
        await self.bot.attack() # items
        await self.bot.move(0.65, 2200)
        await self.bot.attack_technique(1) # -1TP
        await self.bot.move(0.1, 1600)
        await self.bot.attack_technique(2) # -1TP
    async def path_11(self):
        logger_set_path(self.map, 11)
        await self.bot.switch_map_new(world='penacony', y_list=255/1080, scroll_down=True, # Dreammaster Hall
                                      x=910/2400, y=707/1080, start=0.75, deg=0.0, n=0, confirm=False)
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
        logger_set_path(self.map, 'extra')
        await self.bot.use_teleporter(1333/2400, 502/1080, move_x=0, move_y=0, corner='botleft', special_exit=False) # City Sandpit
        await self.bot.move(0.5, 11500)
        await self.bot.interact(wait_for_ready=False)
        await self.bot.action_tap(1535, 960)
        await self.bot.wait_for_ready(min_duration=5, reason='use pinball teleporter')
        await self.bot.move(0.51, 5500)
        await self.bot.interact(wait_for_ready=False)
        await self.bot.action_tap(1535, 960)
        await self.bot.wait_for_ready(min_duration=5, reason='use pinball teleporter')
        await self.bot.move(0.25, 300)
        await self.bot.attack_technique(2) # +2TP


