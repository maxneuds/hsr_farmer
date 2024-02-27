import asyncio as aio
import subprocess
from sys import exit
from datetime import datetime as dt
from automation.bot import Bot
from automation.adb import ADB
from automation.xy import OnePlus7T
from worlds.herta_space_station import World as Herta_Space_Station
from worlds.the_xianzhou_luofu import World as The_Xianzhou_Luofu
from worlds.penacony import World as Penacony
from worlds.jarilo_vi import World as JariloVI

def logger(msg):
    dt_now = dt.now().strftime('%H:%M:%S')
    print(f'[{dt_now}] {msg}')

# logger(f'Screensize: {self.width} x {self.height}')

async def main():
    # try to connect to device
    try:
        subprocess.run('adb connect 10.1.11.3:5555', shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logger(f'Error executing command: {e}')

    ###
    # initialize bot
    ###
    xy = OnePlus7T()
    adb = ADB()
    dev = await adb.get_dev()
    bot = Bot(adb=adb, dev=dev, xy=xy)

    ###
    # load worlds
    ###
    herta_space_station = Herta_Space_Station(bot=bot, xy=xy)
    penacony = Penacony(bot=bot, xy=xy)
    the_xianzhou_luofu = The_Xianzhou_Luofu(bot=bot, xy=xy)
    jarilo_vi = JariloVI(bot=bot, xy=xy) # finetune needed

    # total mapped xp: 93k/100k

    ###
    # farm worlds
    ###
    logger('Farm: Herta Space Station') # 4/4 (7128/7128)
    await bot.switch_world('herta_space_station')
    await herta_space_station.farm_base_zone() # modified (432/432)
    await herta_space_station.farm_storage_zone() # modified (2592/2592)
    await herta_space_station.farm_supply_zone() # modified (2484/2484)
    await herta_space_station.farm_seclusion_zone() # modified (1620/1620)

    logger('Farm: Penacony') # 3/3 (24300/30560 [17820])
    await bot.switch_world('penacony')
    await penacony.farm_dreams_edge() # modified (7668/9612 [7668])
    await penacony.farm_childs_dream() # modified (4664/5832 [2376])
    await penacony.farm_reverie_dreamscape() # modified (11988/15552 [6912])

    logger('Farm: The Xianzhou Luofu') # 7/7 (42164/42596)
    await bot.switch_world('the_xianzhou_luofu')
    await the_xianzhou_luofu.farm_scalegorge_waterscape() # checked (4752/4752)
    await the_xianzhou_luofu.farm_alchemy_commission() # modified (6912/6912)
    await the_xianzhou_luofu.farm_fyxestroll_garden() # modified (4644/4644)
    await the_xianzhou_luofu.farm_artisanship_commission() # modified (9548/9548)
    await the_xianzhou_luofu.farm_divination_commission() # modified (/5832)
    await the_xianzhou_luofu.farm_stargazer_navalia() # modified (6264/6264)
    await the_xianzhou_luofu.farm_cloudford() # modified (4644/4644)

    logger('Farm: Jarilo-VI') # 7/7 (19440/19440)
    await bot.switch_world('jarilo_vi')
    await jarilo_vi.farm_outlying_snow_plains() # modified (2052/2052)
    await jarilo_vi.farm_backwater_pass() # modified (3024/3024)
    await jarilo_vi.farm_corridor() # modified (3672/3672)
    await jarilo_vi.farm_everwinter_hill() # modified (1404/1404)
    await jarilo_vi.farm_great_mine() # modified  (4536/4536)
    await jarilo_vi.farm_rivet_town() # modified (2160/2160)
    await jarilo_vi.farm_robot_settlement() # modified (2592/2592)

if __name__ == '__main__':
    aio.run(main())
