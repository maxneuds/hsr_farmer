import asyncio as aio
# import streamlit as st
from sys import exit
from logger import logger
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

    # 4/4 Herta Space Station (7128/7128)
    # await herta_space_station.farm_seclusion_zone() # (1620/1620) TP:x>=2->2
    # await herta_space_station.farm_base_zone() # (432/432) TP:2->5
    # await herta_space_station.farm_storage_zone() # (2592/2592) TP:5->3
    # await herta_space_station.farm_supply_zone() # (2484/2484) TP:3->5

    # 7/7 Jarilo-VI (19440/19440)
    # await jarilo_vi.farm_outlying_snow_plains() # (2052/2052) TP:5->4
    # await jarilo_vi.farm_backwater_pass() # (3024/3024) TP:4->4
    # await jarilo_vi.farm_robot_settlement() # (2592/2592) TP:4->5
    # await jarilo_vi.farm_corridor() # (3672/3672) TP:5->3
    # await jarilo_vi.farm_everwinter_hill() # (1404/1404) TP:3->1
    # await jarilo_vi.silvermane_guard.teleport(tp_restore=0) # TP:1->3
    # await jarilo_vi.farm_great_mine() # (4536/4536) TP:3->1
    # await jarilo_vi.silvermane_guard.teleport(tp_restore=1) # TP:1->3
    # await jarilo_vi.farm_rivet_town() # (2160/2160) TP:3->4

    # 4/7 Xianzhou Luofu (42596/42596)
    # await the_xianzhou_luofu.farm_starskiff_haven()
    # await the_xianzhou_luofu.farm_cloudford() # (4644/4644) TP:4->1
    # await herta_space_station.supply_zone.teleport(tp_restore=0) # TP:1->3
    # await the_xianzhou_luofu.farm_stargazer_navalia() # (6264/6264) TP:3->2
    # await herta_space_station.storage_zone.teleport(tp_restore=0) # TP:2->4
    # await the_xianzhou_luofu.farm_divination_commission() # (6000/6000) TP:4->2 TODO
    # await jarilo_vi.silvermane_guard.teleport(tp_restore=2) # TP:2->4
    # await the_xianzhou_luofu.farm_fyxestroll_garden() # (4644/4644) TP:4->2
    await the_xianzhou_luofu.farm_artisanship_commission() # verified (9548/9548) TP:2->2 TODO: check path5

    # 5/5 Penacony (47176/50092)
    # await penacony.farm_dreams_edge() # (7668/9612)
    # await penacony.farm_childs_dream() # (5832/5832)
    # await penacony.golden_hour.teleport(tp_restore=0) # (+2TP)
    # await penacony.farm_the_reverie_dreamscape() # (14580/15552) TODO: rework with position_fixing
    # await penacony.farm_dewlight_pavilion() # (11448/11448) check: path5
    # await penacony.farm_clock_studios_theme_park() # (7648/7648)

    # 1/1 Astral Express
    # await astral_express.parlor_car()
    
    # TOTAL XP: 116.340 / 119.256
    # TOTAL TIME: 

    ### TODO

    # await the_xianzhou_luofu.farm_scalegorge_waterscape() # verified (4752/4752)
    # await the_xianzhou_luofu.farm_alchemy_commission() # verified (6912/6912)

    # await penacony.golden_hour.teleport(tp_restore=1) # TP:2->4


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
