import asyncio as aio
from automation.bot import Bot
from datetime import datetime as dt
from sys import exit

def logger(msg):
    dt_now = dt.now().strftime('%H:%M:%S')
    print(f'[{dt_now}] {msg}')

class World:
    def __init__(self, bot, xy):
        # initialize bot
        self.bot = bot
        self.xy = xy

    async def farm_reverie_dreamscape(self):
        # await self.bot.switch_map(925/1080, scroll_down=True)
        # logger('### group 1 ###') # roamer
        # # await self.bot.use_teleporter(1238/2400, 462/1080, move_x = -0.25, move_y = 0.3, open_map=False, confirm=True)  # Platinum Guest Room
        # await self.bot.movepi(0.5, 2800)
        # await self.bot.movepi(1.0, 13000)
        # await self.bot.movepi(0.5, 3000)
        # await self.bot.movepi(0.75, 1000)
        # await self.bot.attack()
        # await self.bot.sleep(0.5)
        # # await self.bot.wait_for_onmap()
        # logger('### group 1, part 2 ###') # aggro pull
        # await self.bot.movepi(0.74, 2700)
        # await self.bot.movepi(0.66, 900)
        # await self.bot.attack()
        # await self.bot.wait_for_onmap()
        # logger('### group 1, part 3 ###') # aggro pull
        # await self.bot.movepi(1.75, 200)
        # await self.bot.attack()
        # await self.bot.wait_for_onmap()
        # logger('### group 2 ###')
        await self.bot.use_teleporter(1245/2400, 325/1080, move_y = 0.2, confirm=True) # Platinum Guest Room
        await self.bot.movepi(0.5, 2800)
        await self.bot.movepi(1.0, 5000)
        await self.bot.attack()
        await self.bot.sleep(0.5)
        await self.bot.movepi(1.0, 7900)
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.25, 1500)
        await self.bot.movepi(0.56, 6500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 3 ###')
        exit() # sus teleport
        await self.bot.use_teleporter(1361/2400, 169/1080, confirm=True) # Platinum Guest Room
        await self.bot.movepi(0.5, 2800)
        await self.bot.movepi(1.0, 28000)
        await self.bot.movepi(1.25, 1200)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 4 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1134/2400, 129/1080, move_y=0.3, open_map=False, confirm=True) # Platinum Guest Room
        await self.bot.movepi(0.5, 2800)
        await self.bot.movepi(1.0, 28000)
        await self.bot.movepi(0.75, 1000)
        await self.bot.movepi(0.5, 750)
        await self.bot.movepi(0.75, 750)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # logger('### group 5 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1134/2400, 129/1080, move_y=0.3, open_map=False, confirm=True) # Platinum Guest Room
        await self.bot.movepi(0.5, 2800)
        await self.bot.movepi(1.0, 28000)
        await self.bot.movepi(1.1, 700)
        await self.bot.interact()
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.3, 1800)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(0.0, 2000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 6 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1134/2400, 129/1080, move_y=0.3, open_map=False, confirm=True) # Platinum Guest Room
        await self.bot.movepi(0.5, 2800)
        await self.bot.movepi(1.0, 13000)
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.25, 1500)
        await self.bot.movepi(0.56, 6000)
        await self.bot.movepi(0.5, 3300)
        await self.bot.movepi(0.9, 2300)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 6, part 2 ###') # roamer
        await self.bot.movepi(0.9, 1000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 7 ###')
        await self.bot.use_teleporter(687/2400, 666/1080, move_x=0.2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 4800)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 7, part 2 ###') # roamer
        await self.bot.attack()
        await self.bot.wait_for_onmap(min_duration=10)
        logger('### group 8 ###')
        await self.bot.use_teleporter(754/2400, 160/1080)
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 8200)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 9 ###')
        await self.bot.use_teleporter(990/2400, 250/1080)
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 5500)
        await self.bot.movepi(0.92, 4400)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 9, part 2 ###') # roamer
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 10 ###') # roamer
        await self.bot.use_teleporter(1020/2400, 200/1080)
        await self.bot.movepi(1.25, 1200)
        await self.bot.movepi(1, 5500)
        await self.bot.movepi(0.75, 4000)
        await self.bot.movepi(0.5, 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 11 ###')
        await self.bot.use_teleporter(1100/2400, 245/1080)
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
        logger('### group 11, part 2 ###')
        await self.bot.movepi(1.25, 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 12 ###')
        exit()
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(980/2400, 215/1080, open_map=False, move_y=0.35) # TODO: check this
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
        logger('### group 13 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(980/2400, 215/1080, open_map=False, move_y=0.35) # VIP Lounge Corridor 
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 2000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 14 ###') # roamer
        await self.bot.use_teleporter(1100/2400, 450/1080)
        await self.bot.movepi(0.5, 1500)
        await self.bot.movepi(1.0, 2500)
        await self.bot.movepi(0.5, 4900)
        await self.bot.movepi(0.00, 2500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 15 ###')
        await self.bot.use_teleporter(871/2400, 164/1080)
        await self.bot.movepi(0.5, 1000)
        await self.bot.movepi(0.25, 4700)
        await self.bot.movepi(0.00, 6700)
        await self.bot.movepi(1.5, 7000)
        await self.bot.movepi(1.25, 1200)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 15, part 2 ###') # roamer
        await self.bot.movepi(1.2, 1000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 16 ###')
        await self.bot.use_teleporter(1017/2400, 162/1080, move_y=0.35)
        await self.bot.movepi(0.5, 7400)
        await self.bot.movepi(1.0, 500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 17 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1015/2400, 155/1080, open_map=False, move_y=0.1)
        await self.bot.movepi(0.5, 7400)
        await self.bot.movepi(1.0, 500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 500)
        await self.bot.movepi(0.75, 700)
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(1.0, 1400)
        await self.bot.movepi(1.5, 3800)
        await self.bot.movepi(0.00, 1000)
        await self.bot.movepi(0.5, 5300)
        await self.bot.movepi(0.00, 4100)
        await self.bot.movepi(1.75, 2000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 18 ###') # roamer
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1015/2400, 225/1080, open_map=False, move_y=0.15)
        await self.bot.movepi(0.5, 7400)
        await self.bot.movepi(1.0, 500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 500)
        await self.bot.movepi(0.75, 700)
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(1.0, 1400)
        await self.bot.movepi(1.5, 3800)
        await self.bot.movepi(0.00, 1000)
        await self.bot.movepi(0.5, 5300)
        await self.bot.movepi(0.00, 2750)
        await self.bot.movepi(1.5, 1800)
        await self.bot.interact()
        await self.bot.movepi(0.5, 4300)
        await self.bot.movepi(1.0, 200)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 2600)
        await self.bot.interact()
        await self.bot.movepi(0.00, 1800)
        await self.bot.action_button()
        await self.bot.movepi(0.00, 1000)
        await self.bot.movepi(1.75, 800)
        await self.bot.movepi(1.5, 4800)
        await self.bot.movepi(1.75, 700)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 4000)
        await self.bot.movepi(0.00, 3200)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 19 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1015/2400, 221/1080, open_map=False, move_y=0.15)
        await self.bot.movepi(0.5, 7400)
        await self.bot.movepi(1.0, 500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 2500)
        await self.bot.sleep(2)
        await self.bot.movepi(1.0, 500)
        await self.bot.movepi(0.75, 700)
        await self.bot.movepi(0.5, 5200)
        await self.bot.movepi(1.0, 1400)
        await self.bot.movepi(1.5, 3800)
        await self.bot.movepi(0.0, 1000)
        await self.bot.movepi(0.5, 5300)
        await self.bot.movepi(0.0, 2750)
        await self.bot.movepi(1.5, 1800)
        await self.bot.interact()
        await self.bot.movepi(0.5, 4300)
        await self.bot.movepi(1.0, 200)
        await self.bot.action_button()
        await self.bot.movepi(1.0, 2600)
        await self.bot.interact()
        await self.bot.movepi(0.0, 1800)
        await self.bot.action_button()
        await self.bot.movepi(0.0, 1000)
        await self.bot.movepi(1.75, 800)
        await self.bot.movepi(1.5, 4800)
        await self.bot.movepi(1.75, 700)
        await self.bot.action_button()
        await self.bot.movepi(1.5, 4200)
        await self.bot.movepi(0.0, 6200)
        await self.bot.action_button()
        await self.bot.movepi(0.0, 2100)
        await self.bot.movepi(0.19, 2100)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### return to normal map ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(870/2400, 577/1080, open_map=False)

    async def farm_childs_dream(self):
        logger('farm: Childs Dream')
        await self.bot.switch_map(895/1080)
        logger('### group 1 ###')
        await self.bot.use_teleporter(1011/2400, 378/1080, open_map=False) # Corridor of Memories
        await self.bot.movepi(0.25, 2000)
        await self.bot.movepi(0.00, 2000)
        await self.bot.movepi(0.5, 1000)
        await self.bot.movepi(0.25, 1100)
        await self.bot.movepi(0.00, 250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 2 ###')
        await self.bot.use_teleporter(1011/2400, 620/1080) # Corridor of Memories
        await self.bot.movepi(1.5, 9300)
        await self.bot.movepi(1.0, 5500)
        await self.bot.movepi(1.25, 750)
        await self.bot.attack()
        await self.bot.wait_for_onmap() # warning: view rotates after fight
        logger('### group 3 ###')
        await self.bot.movepi(0.75, 8100)
        await self.bot.attack()
        await self.bot.wait_for_onmap() # warning: view rotates after fight
        logger('### group 3, part 2 ###')
        await self.bot.movepi(0.5, 3000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 4 ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(960/2400, 790/1080, open_map=False) # Eddying Dreamscape
        await self.bot.movepi(1.5, 3500)
        await self.bot.movepi(1.75, 250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 5 ###')
        await self.bot.use_teleporter(960/2400, 435/1080) # Eddying Dreamscape
        await self.bot.movepi(1.5, 14500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 6 ###')
        await self.bot.use_teleporter(962/2400, 521/1080) # Eddying Dreamscape
        await self.bot.movepi(1.25, 500)
        await self.bot.movepi(1.5, 2100)
        await self.bot.movepi(0.00, 1500)
        await self.bot.movepi(1.75, 1000)
        await self.bot.movepi(0.00, 1500)
        await self.bot.movepi(1.75, 1000)
        await self.bot.movepi(0.00, 500)
        await self.bot.movepi(1.75, 500)
        await self.bot.movepi(0.00, 2000)
        await self.bot.movepi(1.75, 1500)
        await self.bot.interact()
        await self.bot.movepi(0.00, 3000)
        await self.bot.movepi(1.75, 750)
        await self.bot.action_button()
        await self.bot.movepi(0.00, 3000)
        await self.bot.movepi(1.5, 2000)
        await self.bot.movepi(1.25, 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### return from special map ###')
        await self.bot.open_map(penacony=True)
        await self.bot.use_teleporter(1120/2400, 725/1080, open_map=False)

    async def farm_dreams_edge(self):
        logger('farm: Dreams Edge')
        await self.bot.switch_map(775/1080)
        logger('### group 1 ###')
        await self.bot.use_teleporter(1445/2400, 113/1080, open_map=False) # Dreamweaver Plaza
        await self.bot.movepi(0.00, 4000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 2 ###')
        await self.bot.use_teleporter(1076/2400, 515/1080) # Dreamweaver Plaza
        await self.bot.movepi(0.25, 1500)
        await self.bot.movepi(0.5, 4500)
        await self.bot.movepi(0.00, 3700)
        await self.bot.movepi(0.5, 5500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 3 ###')
        await self.bot.use_teleporter(1092/2400, 261/1080) # Dreamweaver Plaza
        await self.bot.movepi(0.25, 1500)
        await self.bot.movepi(0.5, 4500)
        await self.bot.movepi(0.00, 3700)
        await self.bot.movepi(0.5, 11250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 3, part 2 ###') # roamer
        await self.bot.movepi(0.00, 250)
        await self.bot.attack()
        await self.bot.wait_for_onmap(min_duration=5)
        logger('### group 4 ###')
        await self.bot.use_teleporter(551/2400, 928/1080) # Rooftop Garden
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.75, 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 4, part 2 ###')
        await self.bot.movepi(1.0, 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 5 ###')
        await self.bot.use_teleporter(1012/2400, 484/1080) # Rooftop Garden
        await self.bot.movepi(0.5, 3500)
        await self.bot.movepi(0.00, 2750)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 5, part 2 ###')
        await self.bot.movepi(0.5, 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap(min_duration=5)
        logger('### group 6 ###')
        await self.bot.use_teleporter(1052/2400, 569/1080) # Rooftop Garden
        await self.bot.movepi(0.5, 5000)
        await self.bot.movepi(0.75, 1500)
        await self.bot.movepi(0.5, 3000)
        await self.bot.movepi(0.95, 2700)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 7 ###')
        await self.bot.use_teleporter(380/2400, 492/1080) # Bud of Memories
        await self.bot.movepi(1.5, 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 8 ###')
        await self.bot.use_teleporter(656/2400, 556/1080) # Bud of Memories
        await self.bot.movepi(1.25, 2750)
        await self.bot.movepi(0.75, 1500)
        await self.bot.movepi(1.0, 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 9 ###')
        await self.bot.use_teleporter(656/2400, 256/1080, move_y=0.2) # Front Observation Deck
        await self.bot.movepi(0.5, 5000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        logger('### group 10 ###')
        await self.bot.use_teleporter(1007/2400, 213/1080, move_y=0.5, confirm=True) # THe Family's
        await self.bot.movepi(0.25, 3000)
        await self.bot.movepi(0.5, 8500)
        await self.bot.movepi(1.0, 6000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()