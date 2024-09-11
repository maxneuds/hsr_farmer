from logger import logger, logger_set_path
from automation.bot import Bot
from worlds.extra import Extra


class Audition_Venue:
    '''
    R2: 2
    '''
    def __init__(self, device):
        self.map = 'Audition Venue'
        self.bot = Bot(device)
        self.extra = Extra(device)
    async def farm(self):
        # await self.extra.restore_tp(tp=4, info='dev') # not needed
        # await self.teleport()
        await self.path_1()
        await self.path_2()
        await self.path_3()
        await self.path_4()
        await self.path_5()
        await self.path_6()
        await self.path_7()
        await self.path_99()
    async def teleport(self):
        logger_set_path(self.map, 'Teleport')
        logger.info('---')
        logger.info('--- Map: SoulGlad Scorchsand Audition Venue')
        logger.info('---')
        await self.bot.switch_map(y_list=686/1080, world='penacony', scroll_down=True, # Audition Plaza
                                    x=940/2400, y=580/1080, corner='botright', move_x=0, move_y=0)
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(5) # move
        raise SystemExit('get items') 
    async def path_1(self):
        logger_set_path(self.map, 1)
        await self.bot.use_teleporter(x=1120/2400, y=745/1080, corner='botright', move_x=0, move_y=6, x2=751/2400, y2=310/1080) # Dreamplay Fantasia: Action Challenge
        await self.bot.move(0.275, 3100)
        await self.bot.attack_technique(2) # -2TP
        await self.bot.move(1.75, 3000)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(1.05, 3000)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(0.5, 500)
        await self.bot.attack_technique(2) # move
        await self.bot.move(0.75, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.6, 500)
        await self.bot.move(0.75, 1000)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.75, 1200)
        await self.bot.move(0.5, 700)
        await self.bot.move(0.6, 500)
        await self.bot.move(0.75, 1000)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(4) # -2TP
        await self.bot.move(1.4, 3000)
        await self.bot.move(1.1, 1000)
        await self.bot.restore_tp('trick_snack') # +2TP
        await self.bot.posfix(1.25, 500)
        await self.bot.move(0.25, 1500)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(7) # move
        await self.bot.move(0.2, 300)
        await self.bot.attack_technique(4) # move
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(8) # -3TP
        await self.bot.move(1.75, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.0, 2000)
        await self.bot.move(1.75, 1500)
        await self.bot.restore_tp('trick_snack') # +2TP
        await self.bot.posfix(0.75, 1000)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6) # -1TP
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(3) # -1TP, roamer
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(6) # move
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.75, 1500)
        await self.bot.posfix(0.75, 500)
        await self.bot.move(1.75, 1600)
        await self.bot.move(1.5, 300)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(5) # move
        await self.bot.move(1.0, 1000)
        await self.bot.move(0.5, 800)
        await self.bot.move(0.1, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.25, 1600)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(3) # items
    async def path_2(self):
        logger_set_path(self.map, 2)
        await self.bot.use_teleporter(x=1162/2400, y=741/1080, corner='botright', move_x=0, move_y=6, x2=609/2400, y2=326/1080) # Dreamplay Fantasia: Acting Challenge
        raise SystemExit('check: path')
        await self.bot.move(0.5, 900)
        await self.bot.move(1.0, 1600)
        await self.bot.attack() # items
        await self.bot.move(0.125, 2400)
        await self.bot.attack() # +2TP
        await self.bot.move(0.7, 1500)
        await self.bot.move(0.5, 300)
        await self.bot.attack() # items
        await self.bot.move(0.75, 1000)
        await self.bot.move(0.35, 300)
        await self.bot.attack_technique(8) # items
        await self.bot.move(0.0, 1500)
        await self.bot.posfix(0.0, 500)
        await self.bot.move(1.5, 1000)
        await self.bot.move(0.0, 500)
        await self.bot.move(0.5, 2000)
        await self.bot.move(0.8, 1000)
        await self.bot.attack_technique(6) # items
        await self.bot.move(1.9, 300)
        await self.bot.attack_technique(10) # items
        await self.bot.move(1.75, 1500)
        await self.bot.posfix(1.75, 500)
        await self.bot.move(0.75, 1500)
        await self.bot.move(0.5, 1500)
        await self.bot.move(0.7, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.4, 300)
        await self.bot.attack_technique(7) # items
        await self.bot.move(0.25, 1500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.25, 1500)
        await self.bot.move(1.0, 300)
        await self.bot.attack_technique(10) # move
        await self.bot.move(1.4, 300)
        await self.bot.attack_technique(3) # -2TP
        await self.bot.move(1.9, 300)
        await self.bot.attack_technique(2) # items
    # 1TP
    async def path_3(self):
        logger_set_path(self.map, 3)
        await self.bot.use_teleporter(x=1163/2400, y=851/1080, corner='topleft', move_x=0, move_y=7, x2=661/2400, y2=750/1080) # Superstar Showdown: Arena I
        raise SystemExit('check')
        await self.bot.move(0.8, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(9) # items
        await self.bot.move(0.25, 500)
        await self.bot.posfix(0.25, 500)
        await self.bot.move(1.3, 1600)
        await self.bot.attack_technique(1) # +2TP
        await self.bot.move(0.8, 300)
        await self.bot.attack_technique(3) # move
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(18) # move
        await self.bot.move(0.3, 900)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.7, 300)
        await self.bot.attack_technique(4) # items
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(4) # items
    # 3TP
    async def path_4(self):
        logger_set_path(self.map, 4)
        await self.bot.use_teleporter(x=1235/2400, y=690/1080, corner='topleft', move_x=0, move_y=7, x2=805/2400, y2=750/1080, confirm=True, confirm_x=1493/2400, confirm_y=763/1080) # Superstar Showdown: Arena II
        raise SystemExit('check')
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(3) # items
        await self.bot.move(0.95, 300)
        await self.bot.attack_technique(4) # items
        raise SystemExit('check: items done?')
        await self.bot.move(1.75, 700)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(1) # +2TP
        raise SystemExit('check: keep to the left side')
        await self.bot.move(0.2, 900)
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(16) # items
        await self.bot.move(0.3, 300)
        await self.bot.attack_technique(5) # items
        await self.bot.move(0.6, 300)
        await self.bot.attack_technique(6) # items
    # 5TP
    async def path_5(self):
        logger_set_path(self.map, 5)
        await self.bot.use_teleporter(x=746/2400, y=781/1080, corner='botright', move_x=0, move_y=8, x2=1316/2400, y2=270/1080) # Gunfire Time: Time Trial
        raise SystemExit('check: todo')
        await self.bot.move(0.3, 800)
        await self.bot.move(0.0, 300)
        await self.bot.attack_technique(5) # -2TP
        await self.bot.move(1.75, 500)
        await self.bot.posfix(1.75, 500)
        raise SystemExit('todo: items, +2TP, monster right')
    async def path_6(self):
        logger_set_path(self.map, 6)
        await self.bot.use_teleporter(x=1390/2400, y=332/1080, corner='botright', move_x=0, move_y=8, x2=1316/2400, y2=270/1080) # Gunfire Time: Time Trial (Posterior)
        raise SystemExit('check: todo')
    async def path_7(self):
        logger_set_path(self.map, 7)
        await self.bot.use_teleporter(x=1169/2400, y=756/1080, corner='botright', move_x=0, move_y=8, x2=1175/2400, y2=270/1080) # Gunfire Time: Gunfire Trial
        raise SystemExit('check: todo')
    async def path_99(self):
        logger_set_path(self.map, 99)
        await self.bot.use_teleporter(x=974/2400, y=686/1080, corner='topleft', move_x=0, move_y=3) # Path of the Superstar
        raise SystemExit('check')
        await self.bot.move(1.25, 1100)
        await self.bot.move(1.5, 300)
        await self.bot.attack_technique(8) # items
        await self.bot.move(0.0, 1000)
        await self.bot.attack_technique(2) # items
        await self.bot.move(0.5, 300)
        await self.bot.attack_technique(8) # items


