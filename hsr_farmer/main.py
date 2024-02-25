import asyncio as aio
import subprocess
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

    # xp before: 165650 (swan)
    # xp after:
    # total mapped xp: 90k/100k

    ###
    # farm worlds
    ###
    # logger('Farm: Herta Space Station') # 4/4 (7128/7128) 68600 (sampo)
    # await bot.switch_world('herta_space_station')
    # await herta_space_station.farm_base_zone() # checked (432/432)
    # await herta_space_station.farm_storage_zone() # checked (2592/2592)
    # await herta_space_station.farm_supply_zone() # checked (2484/2484)
    # await herta_space_station.farm_seclusion_zone() # checked (1620/1620)

    # logger('Farm: Penacony') # 3/3 (24300/30560 [17820])
    # await bot.switch_world('penacony')
    # await penacony.farm_dreams_edge() # checked (7668/9612 [7668])
    # await penacony.farm_childs_dream() # checked (4664/5832 [2376])
    # await penacony.farm_reverie_dreamscape() # modified (11988/15552 [6912])

    # logger('Farm: The Xianzhou Luofu')
    # await bot.switch_world('the_xianzhou_luofu')
    # await the_xianzhou_luofu.farm_scalegorge_waterscape() # checked (4752/4752) 100028
    await the_xianzhou_luofu.farm_alchemy_commission() # checked (/6480 [6156]) 104780
    # await the_xianzhou_luofu.farm_fyxestroll_garden() # checked (/4644)
    # await the_xianzhou_luofu.farm_artisan_commission() # checked (/9548)
    # await the_xianzhou_luofu.farm_divination_commission() # checked (/5832)
    # await the_xianzhou_luofu.farm_stargazer_navalia() # checked (/6264)
    # await the_xianzhou_luofu.farm_cloudford() # checked (/4644)

    # logger('Farm: Jarilo-VI')
    # await bot.switch_world('jarilo_vi')
    # await jarilo_vi.farm_outlying_snow_plains() # checked (/2052)
    # await jarilo_vi.farm_backwater_pass() # checked (/3024)
    # await jarilo_vi.farm_corridor() # finetune needed # checked (/3672)
    # await jarilo_vi.farm_everwinter_hill() # check needed # checked (/1404)
    # await jarilo_vi.farm_great_mine() # checked & verified # checked (/4536)
    # await jarilo_vi.farm_rivet_town() # checked (/2160)
    # await jarilo_vi.farm_robot_settlement() # checked (/2592)

if __name__ == '__main__':
    aio.run(main())
