import asyncio as aio
from automation.bot import Bot
from datetime import datetime as dt

def logger(msg):
    dt_now = dt.now().strftime('%H:%M:%S')
    print(f'[{dt_now}] {msg}')


class World:
    def __init__(self, bot, xy):
        # initialize bot
        self.bot = bot
        self.xy = xy

    async def farm(self):
        logger('Farm: The Xianzhou Luofu')
        await self.bot.switch_world('the_xianzhou_luofu')
        # farm locations
        await self.farm_scalegorge_waterscape()
        await self.farm_alchemy_commission()
        await self.farm_fyxestroll_garden()
        await self.farm_artisan_commission()

    async def farm_next(self):
        await self.farm_artisan_commission()
        pass

    async def farm_artisan_commission(self):
        await self.bot.switch_map(0.5231)
        # group 1
        await self.bot.use_teleporter(int(self.xy.width*0.5121), int(self.xy.height*0.10926))
        await self.bot.move('n', 5400)
        await self.bot.move('e', 6000)
        await self.bot.attack()
        await self.bot.wait_for_onmap(min_duration=45)
        # group 2
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.3333), int(self.xy.height*0.6685))
        await self.bot.move('n', 9500)
        await self.bot.move('w', 1000)
        await self.bot.sleep(2)
        await self.bot.move('s', 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap(min_duration=30)
        # group 3
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.4358), int(self.xy.height*0.78056))
        await self.bot.move('n', 10700)
        await self.bot.move('e', 3900)
        await self.bot.move('n', 5800)
        await self.bot.move('e', 1400)
        await self.bot.sleep(2)
        await self.bot.move('s', 100)
        await self.bot.attack()
        # group 4
        await self.bot.open_map()
        cmd = f'input swipe {int(self.xy.width*0.4)} {int(self.xy.height*0.5)} {int(self.xy.width*0.6)} {int(self.xy.height*0.5)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*0.27917), int(self.xy.height*0.812))

    async def farm_fyxestroll_garden(self):
        await self.bot.switch_map(0.6296)
        # group 1
        await self.bot.use_teleporter(int(self.xy.width*0.2825), int(self.xy.height*0.40926))
        await self.bot.move('s', 1000)
        await self.bot.move('e', 4000)
        await self.bot.move('s', 500)
        await self.bot.move('e', 2000)
        await self.bot.move('s', 500)
        await self.bot.move('e', 1500)
        await self.bot.move('n', 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 2
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.4417), int(self.xy.height*0.699))
        await self.bot.move('s', 1000)
        await self.bot.move('e', 4000)
        await self.bot.move('se', 2500)
        await self.bot.move('ne', 3000)
        await self.bot.move('e', 1400)
        await self.bot.move('n', 1100)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 3
        await self.bot.move('e', 750)
        await self.bot.move('ne', 1100)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 4
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.3183), int(self.xy.height*0.7704))
        await self.bot.move('s', 5000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 5 | check this
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 6
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.3183), int(self.xy.height*0.3537))
        await self.bot.move('s', 6500)
        await self.bot.move('se', 2000)
        await self.bot.move('s', 1000)
        await self.bot.move('se', 2500)
        await self.bot.move('s', 2000)
        await self.bot.move('se', 1000)
        await self.bot.move('s', 3000)
        await self.bot.move('w', 1500)
        await self.bot.move('n', 1200)
        await self.bot.move('w', 1800)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 7
        await self.bot.open_map()
        cmd = f'input swipe {int(self.xy.width*0.5)} {int(self.xy.height*0.2)} {int(self.xy.width*0.5)} {int(self.xy.height*0.6)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(3)
        await self.bot.use_teleporter(int(self.xy.width*0.31875), int(self.xy.height*0.46759))
        await self.bot.move('s', 6500)
        await self.bot.move('se', 2000)
        await self.bot.move('s', 1000)
        await self.bot.move('se', 2500)
        await self.bot.move('s', 2000)
        await self.bot.move('se', 1000)
        await self.bot.move('s', 3000)
        await self.bot.move('e', 3000)
        await self.bot.move('s', 700)
        await self.bot.move('se', 1000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 8
        await self.bot.move('s', 4000)
        await self.bot.move('w', 3000)
        await self.bot.attack()
        await self.bot.wait_for_onmap(min_duration=30)

    async def farm_alchemy_commission(self):
        logger('farm: Alchemy Comission')
        await self.bot.switch_map(0.745)
        # group 1
        cmd = f'input swipe {int(self.xy.width*0.5)} {int(self.xy.height*0.85)} {int(self.xy.width*0.5)} {int(self.xy.height*0.15)} 1500'
        await self.bot.dev.shell(cmd)
        await aio.sleep(2)
        await self.bot.use_teleporter(int(self.xy.width*0.3658), int(self.xy.height*0.70833))
        await self.bot.move('s', 5500)
        await self.bot.move('sw', 2000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 2
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.3758), int(self.xy.height*0.71944))
        await self.bot.move('s', 5500)
        await self.bot.move('sw', 8000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 3
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.27), int(self.xy.height*0.2315))
        await self.bot.move('w', 1500)
        await self.bot.move('n', 4000)
        await self.bot.move('w', 500)
        await self.bot.move('n', 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 4
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.3721), int(self.xy.height*0.3574))
        await self.bot.move('w', 2500)
        await self.bot.move('n', 3000)
        await self.bot.move('w', 5000)
        await self.bot.move('s', 2500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 5
        await self.bot.move('w', 1500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 6
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.2717), int(self.xy.height*0.4898))
        await self.bot.move('w', 500)
        await self.bot.move('s', 5000)
        await self.bot.move('w', 4000)
        await self.bot.move('s', 2000)
        await self.bot.move('e', 5000)
        await self.bot.move('s', 750)
        await self.bot.move('e', 1800)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 7
        await self.bot.move('s', 100)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 8
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.6025), int(self.xy.height*0.3102))
        await self.bot.move('n', 1500)
        await self.bot.move('nw', 6500)
        await self.bot.move('w', 6000)
        await self.bot.move('sw', 3000)
        await self.bot.move('w', 3000)
        await self.bot.move('sw', 1500)
        await self.bot.move('w', 500)
        await self.bot.move('sw', 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        await self.bot.wait_for_onmap() # stability: in case of only 2/3
        # group 9
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.25833), int(self.xy.height*0.475))
        await self.bot.move('n', 1500)
        await self.bot.move('w', 500)
        await self.bot.move('n', 1500)
        for _ in range(8):
            await self.bot.move('e', 325)
            await self.bot.move('n', 500)
        await self.bot.move('n', 750)
        for _ in range(4):
            await self.bot.move('e', 300)
            await self.bot.move('n', 500)
        await self.bot.move('e', 1500)
        await self.bot.move('n', 250)
        await self.bot.move('e', 1000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 10
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.5479), int(self.xy.height*0.48796))
        await self.bot.move('n', 1500)
        await self.bot.move('w', 500)
        await self.bot.move('n', 1500)
        for _ in range(8):
            await self.bot.move('e', 325)
            await self.bot.move('n', 500)
        await self.bot.move('n', 750)
        for _ in range(4):
            await self.bot.move('e', 300)
            await self.bot.move('n', 500)
        await self.bot.move('e', 1500)
        await self.bot.move('n', 250)
        await self.bot.move('e', 1000)
        await self.bot.move('n', 1500)
        await self.bot.move('e', 2500)
        await self.bot.move('s', 500)
        await self.bot.move('e', 1500)
        await self.bot.move('n', 750)
        await self.bot.move('e', 1500)
        await self.bot.move('s', 800)
        await self.bot.move('e', 1700)
        await self.bot.move('s', 1200)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 11
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 12
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.5833), int(self.xy.height*0.6852))
        await self.bot.move('n', 1500)
        await self.bot.move('w', 500)
        await self.bot.move('n', 1500)
        for _ in range(8):
            await self.bot.move('e', 325)
            await self.bot.move('n', 500)
        await self.bot.move('n', 750)
        for _ in range(4):
            await self.bot.move('e', 300)
            await self.bot.move('n', 500)
        await self.bot.move('e', 1500)
        await self.bot.move('n', 250)
        await self.bot.move('e', 1000)
        await self.bot.move('n', 1500)
        await self.bot.move('e', 2500)
        await self.bot.move('s', 500)
        await self.bot.move('e', 1500)
        await self.bot.move('n', 750)
        await self.bot.move('e', 1500)
        await self.bot.move('s', 800)
        await self.bot.move('e', 1700)
        await self.bot.move('s', 3200)
        for _ in range(4):
            await self.bot.move('w', 400)
            await self.bot.move('s', 500)
        await self.bot.move('s', 2000)
        await self.bot.move('e', 750)
        await self.bot.move('s', 4000)
        await self.bot.move('w', 1500)
        await self.bot.move('s', 500)
        await self.bot.move('w', 2250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 12, part 2
        await self.bot.move('w', 250)
        await self.bot.attack()
        await self.bot.wait_for_onmap()

    async def farm_scalegorge_waterscape(self):
        await self.bot.switch_map(0.85, open_map=False, scroll_down=True)
        # group 1
        cmd = f'input swipe {int(self.xy.width*0.6)} {int(self.xy.height*0.5)} {int(self.xy.width*0.4)} {int(self.xy.height*0.5)} 1000'
        await self.bot.dev.shell(cmd)
        await aio.sleep(2)
        await self.bot.use_teleporter(int(self.xy.width*0.605), int(self.xy.height*0.49))
        await self.bot.move('s', 4400)
        await self.bot.move('e', 2000)
        await self.bot.move('n', 3300)
        await self.bot.move('e', 3800)
        await self.bot.attack()
        await self.bot.wait_for_onmap(min_duration=90)
        # group 2
        await self.bot.open_map()
        cmd = f'input swipe {int(self.xy.width*0.2)} {int(self.xy.height*0.5)} {int(self.xy.width*0.6)} {int(self.xy.height*0.5)} 1000'
        await self.bot.dev.shell(cmd)
        await aio.sleep(2)
        await self.bot.use_teleporter(int(self.xy.width*0.464), int(self.xy.height*0.6))
        await self.bot.move('w', 5400)
        await self.bot.move('s', 1300)
        await self.bot.move('w', 6500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 3 | check this
        await self.bot.move('w', 1500)
        await self.bot.move('nw', 2500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 4 | check this
        await self.bot.wait_for_onmap(min_duration=60)
        # group 5
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.2433), int(self.xy.height*0.6306))
        await self.bot.move('s', 10500)
        await self.bot.move('e', 333)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 6
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.40125), int(self.xy.height*0.70648))
        await self.bot.move('s', 7100)
        await self.bot.move('w', 9000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 7
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.3104), int(self.xy.height*0.642))
        await self.bot.move('s', 1600)
        await self.bot.move('e', 3000)
        for _ in range(12):
            await self.bot.move('s', 650)
            await self.bot.move('e', 650)
        await self.bot.move('e', 6000)
        await self.bot.move('s', 2000)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 8 | attack misses
        await self.bot.move('e', 1500)
        await self.bot.move('s', 500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 9
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.5533), int(self.xy.height*0.2583))
        await self.bot.move('s', 3000)
        await self.bot.move('e', 6300)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 10
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.37875), int(self.xy.height*0.6083))
        await self.bot.move('s', 3000)
        await self.bot.move('e', 3500)
        await self.bot.move('s', 3500)
        await self.bot.move('s', 3500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 11
        await self.bot.open_map()
        await self.bot.use_teleporter(int(self.xy.width*0.33), int(self.xy.height*0.1083))
        await self.bot.move('w', 3000)
        await self.bot.move('n', 750)
        await self.bot.move('w', 6500)
        await self.bot.attack()
        await self.bot.wait_for_onmap()
        # group 12 | check this again
        await self.bot.wait_for_onmap()
