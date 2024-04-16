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
    # await herta_space_station.farm_seclusion_zone() # (1620/1620)
    # await herta_space_station.farm_base_zone() # (432/432)
    # await herta_space_station.farm_storage_zone() # (2592/2592)
    # await herta_space_station.farm_supply_zone() # (2484/2484)

    # 2/7 Jarilo-VI (19440/19440)
    # await jarilo_vi.farm_outlying_snow_plains() # (2052/2052) check1
    # await jarilo_vi.farm_backwater_pass() # (3024/3024) done1
    # await jarilo_vi.farm_silvermane_guard() # (TP)
    await jarilo_vi.farm_corridor() # (3672/3672) done0

    # 4/5 Penacony (26460/???)
    # await penacony.farm_dreams_edge() # (7668/9612)
    # await penacony.farm_childs_dream() # (5832/5832)
    # await penacony.farm_the_reverie_dreamscape() # (14148/15552)
    # await penacony.farm_dewlight_pavilion() # (11448/11448)
    # await penacony.farm_golden_hour() # (TP)
    # await penacony.farm_clock_studios_theme_park() # (7648/7648) 77.776

    # 1/7 Xianzhou Luofu (42596/42596)
    # await the_xianzhou_luofu.farm_starskiff_haven()
    # await the_xianzhou_luofu.farm_cloudford() # (4644/4644) # in progress
    # await the_xianzhou_luofu.farm_fyxestroll_garden() # (4644/4644)
    # await herta_space_station.farm_tp()

    # 1/1 Astral Express
    # await astral_express.parlor_car()


    ### TODO

    # await jarilo_vi.farm_everwinter_hill() # (1404/1404)
    # await jarilo_vi.farm_great_mine() #  (4536/4536)
    # await jarilo_vi.farm_rivet_town() # (2160/2160)
    # await jarilo_vi.farm_robot_settlement() # (2592/2592)

    # await the_xianzhou_luofu.farm_cloudford() # verified (4644/4644)
    # await the_xianzhou_luofu.farm_scalegorge_waterscape() # verified (4752/4752)
    # await the_xianzhou_luofu.farm_alchemy_commission() # verified (6912/6912)
    # await the_xianzhou_luofu.farm_artisanship_commission() # verified (9548/9548)
    # await the_xianzhou_luofu.farm_divination_commission() # verified (6000/6000)
    # await the_xianzhou_luofu.farm_stargazer_navalia() # verified (6264/6264)



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
