import asyncio as aio
# import streamlit as st
from sys import exit
from datetime import datetime as dt
from logger import logger, log_runtime
from automation.bot import Bot
from automation.adb import ADB
from automation.xy import OnePlus7T
from farmer.penacony import Penacony
from farmer.the_xianzhou_luofu import The_Xianzhou_Luofu
from farmer.herta_space_station import Herta_Space_Station
from farmer.jarilo_vi import Jarilo_VI

DEVICE = '10.1.11.3:5555'

async def main():
    # initialize bot
    xy = OnePlus7T()
    adb = ADB(DEVICE)
    dev = await adb.get_dev()
    bot = Bot(adb=adb, dev=dev, xy=xy)

    # load worlds
    # astral_express = Astral_Express(bot=bot)
    herta_space_station = Herta_Space_Station(bot=bot)
    jarilo_vi = Jarilo_VI(bot=bot)
    the_xianzhou_luofu = The_Xianzhou_Luofu(bot=bot)
    penacony = Penacony(bot=bot)

    from time import time

    # 4/4 Herta Space Station XP:7128/7128 Time:840s TP:2->5
    # await herta_space_station.farm_seclusion_zone() # XP:1620/1620 Time:220s TP:x>=2->2
    # await herta_space_station.farm_base_zone() # XP:432/432 Time:90s TP:2->5
    # await herta_space_station.farm_storage_zone() # XP:2592/2592 Time:250s TP:5->3
    # await herta_space_station.farm_supply_zone() # XP:2484/2484 Time:281s TP:3->5

    # 7/7 Jarilo-VI XP:19440/19440 Time:2219 TP:5->4
    # await jarilo_vi.farm_outlying_snow_plains() # XP:2052/2052 Time:188sin TP:5->4
    # await jarilo_vi.farm_backwater_pass() # XP:3024/3024 Time:240sin TP:4->4
    # await jarilo_vi.farm_robot_settlement() # XP:2592/2592 Time:237sin TP:4->5
    # await jarilo_vi.farm_corridor() # XP:3672/3672 Time:432s TP:5->3
    # await jarilo_vi.farm_everwinter_hill() # XP:1404/1404 Time:119s TP:3->1
    # await jarilo_vi.silvermane_guard.teleport(tp_restore=0) # Time:91s TP:1->3
    # await jarilo_vi.farm_great_mine() # XP:4536/4536 Time:326s TP:3->1
    # await jarilo_vi.farm_rivet_town() # XP:2160/2160 Time:262sin TP:1->4
    

    # 7/7 Xianzhou Luofu XP:42596/42596 Time: TP:4->
    # await the_xianzhou_luofu.farm_starskiff_haven() # Time:118s
    # await the_xianzhou_luofu.farm_cloudford() # XP:4644/4644 Time:441s TP:4->5
    # await the_xianzhou_luofu.farm_stargazer_navalia() # XP:6264/6264 Time:420s TP:5->2
    # await jarilo_vi.everwinter_hill.teleport(tp_restore=0) # Time:45s TP:2->4
    # await the_xianzhou_luofu.farm_divination_commission() # XP:6000/6000 Time: TP:4->1
    # await jarilo_vi.silvermane_guard.teleport(tp_restore=1) # Time:83s TP:1->5
    # await the_xianzhou_luofu.farm_fyxestroll_garden() # XP:4644/4644 Time:306s TP:5->1
    # await penacony.golden_hour.teleport(tp_restore=0) # Time:70s TP:1->5
    # await the_xianzhou_luofu.farm_scalegorge_waterscape() # XP:4752/4752 Time:503s TP:5->3
    # await herta_space_station.storage_zone.teleport(tp_restore=0) # Time:33s TP:3->5
    # await the_xianzhou_luofu.farm_artisanship_commission() # XP:9548/9548 Time: TP:5->1
    # await herta_space_station.supply_zone.teleport(tp_restore=0) # TP:1->3
    # await the_xianzhou_luofu.farm_alchemy_commission() # XP:6912/6912 Time: TP:3->2
    

    # 5/5 Penacony (47176/50092)
    # await penacony.farm_dreams_edge() # (7668/9612) TP:2->4
    await penacony.farm_childs_dream() # (5832/5832) TP:4->
    t0 = dt.now()
    log_runtime(t0=t0)
    # await penacony.golden_hour.teleport(tp_restore=1) # TP:
    # await penacony.farm_the_reverie_dreamscape() # (14580/15552) TODO: rework with position_fixing
    # await penacony.farm_dewlight_pavilion() # (11448/11448) check: path5
    # await penacony.farm_clock_studios_theme_park() # (7648/7648)

    # 1/1 Astral Express
    # await astral_express.parlor_car()
    
    # TOTAL XP: 116.340 / 119.256
    # TOTAL TIME: 

    ### TODO
    
    




if __name__ == '__main__':
    try:
        aio.run(main())
    except KeyboardInterrupt:
        logger.debug('Ctrl+C detected. Exiting gracefully.')
        exit()
    # st.title('HSR Farmer')
    # st.selectbox('Startmap:', ('Base Zone', 'Storage Zone'))
    # st.button('Reset', type='primary')
    # st.write('Hello')
