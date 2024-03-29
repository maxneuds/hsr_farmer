import asyncio as aio
from sys import exit
from datetime import datetime as dt
from automation.bot import Bot
from automation.adb import ADB
from automation.xy import OnePlus7T
from worlds.astral_express import World as Astral_Express
from worlds.herta_space_station import World as Herta_Space_Station
from worlds.the_xianzhou_luofu import World as The_Xianzhou_Luofu
from worlds.penacony import World as Penacony
from worlds.jarilo_vi import World as JariloVI


DEVICE = '10.1.11.3:5555'


def logger(msg):
    dt_now = dt.now().strftime('%H:%M:%S')
    print(f'[{dt_now}] {msg}')

async def main():

    ###
    # initialize bot
    ###
    xy = OnePlus7T()
    adb = ADB(DEVICE)
    dev = await adb.get_dev()
    bot = Bot(adb=adb, dev=dev, xy=xy, character_speed=1.00) # movement animatiopn speed base value: Acheron (Bronya)

    ###
    # load worlds
    ###
    astral_express = Astral_Express(bot=bot, xy=xy)
    herta_space_station = Herta_Space_Station(bot=bot, xy=xy)
    penacony = Penacony(bot=bot, xy=xy)
    the_xianzhou_luofu = The_Xianzhou_Luofu(bot=bot, xy=xy)
    jarilo_vi = JariloVI(bot=bot, xy=xy)

    # total mapped xp: 95'624/100k
    # time: 4h30

    ###
    # farm worlds
    # ###
    
    logger('\n\nFarm: Herta Space Station\n') # 4/4 (7128/7128) verified
    await bot.switch_world('herta_space_station')
    await herta_space_station.farm_base_zone() # verified (432/432)
    await herta_space_station.farm_storage_zone() # verified (2592/2592)
    await herta_space_station.farm_supply_zone() # verified (2484/2484)
    await herta_space_station.farm_seclusion_zone() # verified (1620/1620)
    
    logger('\n\nFarm: Jarilo-VI\n') # 7/7 (19440/19440) verified
    await bot.switch_world('jarilo_vi')
    await jarilo_vi.farm_outlying_snow_plains() # verified (2052/2052)
    await jarilo_vi.farm_backwater_pass() # verified (3024/3024)
    await jarilo_vi.farm_corridor() # verified (3672/3672)
    await jarilo_vi.farm_everwinter_hill() # verified (1404/1404)
    await jarilo_vi.farm_great_mine() # verified  (4536/4536)
    await jarilo_vi.farm_rivet_town() # verified (2160/2160)
    await jarilo_vi.farm_robot_settlement() # verified (2592/2592)
    
    logger('\n\nFarm: The Xianzhou Luofu\n') # 7/7 (42596/42596) verified
    await bot.switch_world('the_xianzhou_luofu')
    await the_xianzhou_luofu.farm_scalegorge_waterscape() # verified (4752/4752)
    await the_xianzhou_luofu.farm_alchemy_commission() # verified (6912/6912)
    await the_xianzhou_luofu.farm_artisanship_commission() # verified (9548/9548)
    await the_xianzhou_luofu.farm_divination_commission() # verified (6000/6000)
    await the_xianzhou_luofu.farm_stargazer_navalia() # verified (6264/6264)
    await the_xianzhou_luofu.farm_cloudford() # verified (4644/4644)
    # await the_xianzhou_luofu.farm_fyxestroll_garden() # verified (4644/4644)
    
    logger('\n\nFarm: Penacony\n') # 3/3 (26460/30560 [17820]) verified
    await bot.switch_world('penacony')
    await penacony.farm_dreams_edge() # verified (7668/9612 [7668])
    await penacony.farm_childs_dream() # verified (5508/5832 [2376])
    await penacony.farm_reverie_dreamscape() # verified (13284/15552 [6912])
    
    logger('\n\nEnd: Return to the Express\n')
    await astral_express.parlor_car()

if __name__ == '__main__':
    try:
        aio.run(main())
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting gracefully.")
        exit()


