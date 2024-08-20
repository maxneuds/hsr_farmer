import asyncio as aio
from nicegui import ui
from sys import exit
from datetime import datetime as dt
from logger import logger, log_runtime
from farmer.the_xianzhou_luofu import The_Xianzhou_Luofu
from farmer.jarilo_vi import Jarilo_VI
from worlds.astral_express import Astral_Express
from worlds.herta_space_station import Herta_Space_Station
from worlds.penacony import Penacony

# DEVICE = 'usb'
DEVICE = '10.1.11.3:5555'
MODE = 'credits' # options: credits, xp


async def main():

    # load worlds
    astral_express = Astral_Express(DEVICE)
    herta_space_station = Herta_Space_Station(DEVICE)
    jarilo_vi = Jarilo_VI(DEVICE)
    the_xianzhou_luofu = The_Xianzhou_Luofu(DEVICE)
    penacony = Penacony(DEVICE)

    # TODO: check for TP full message on restore and return to map directly
    # dev
    await penacony.dev()
    raise SystemExit()
    
    # 1/1 Preperation
    # await the_xianzhou_luofu.farm_starskiff_haven() # Time:160

    # farm worlds
    await herta_space_station.farm()
    await penacony.farm(mode=MODE)
    
    # checkout
    # await astral_express.checkout()

    # ### 7/7 Jarilo-VI XP:19440/19440 Time:1750 TP:5->5 R4:1
    # await jarilo_vi.farm_outlying_snow_plains() # XP:2052/2052 Time:188 TP:5->4
    # await jarilo_vi.farm_backwater_pass() # XP:3024/3024 Time:240 TP:4->4
    # await jarilo_vi.farm_robot_settlement() # XP:2592/2592 Time:237 TP:4->5
    # await jarilo_vi.farm_corridor() # XP:3672/3672 Time:432 TP:5->3
    # await jarilo_vi.farm_everwinter_hill() # XP:1404/1404 Time:119 TP:3->3
    # await jarilo_vi.farm_great_mine() # XP:4536/4536 Time:326 TP:3->3 R4:1
    # await jarilo_vi.farm_rivet_town() # XP:2160/2160 Time:262 TP:3->5
    
    # ### 7/8 Xianzhou Luofu XP:42596/42596 Time:3900 TP:5->2 R4:6 R2:1
    # await the_xianzhou_luofu.farm_fyxestroll_garden() # XP:4644/4644 Time:265 TP:5->1
    # await jarilo_vi.silvermane_guard.teleport(tp_restore=4) # Time:85 TP:1->5
    # await the_xianzhou_luofu.farm_artisanship_commission() # XP:9548/9548 Time:610 TP:5->1 R4:2
    # await herta_space_station.supply_zone.teleport(tp_restore=4) # Time:65 TP:1->5
    # await the_xianzhou_luofu.farm_alchemy_commission() # XP:6912/6912 Time:610 TP:5->2 R4:1 R2:1
    # await jarilo_vi.silvermane_guard.teleport(tp_restore=2) # Time:91 TP:2->4
    # await the_xianzhou_luofu.farm_cloudford() # XP:4644/4644 Time:395 TP:4->5
    # await the_xianzhou_luofu.farm_stargazer_navalia() # XP:6264/6264 Time:425 TP:5->4 R4:1
    # await the_xianzhou_luofu.farm_divination_commission() # XP:6000/6000 Time:540 TP:4->2 R4:1
    # await the_xianzhou_luofu.farm_scalegorge_waterscape() # XP:4752/4752 Time:450 TP:2->2 R4:1
    
    
    # TOTAL XP: 116.340 / 119.256
    # TOTAL TIME: 
    # t0 = dt.now()
    # log_runtime(t0=t0)

    ### TODO
    
    
if __name__ == '__main__':
    try:
        aio.run(main())
    except KeyboardInterrupt:
        logger.debug('Ctrl+C detected. Exiting gracefully.')
        exit()


# names = {
#     'herta_space_station': 'Herta Space Station',
#     'jarilo_vi': 'Jarilo VI',
#     'the_xianzhou_luofu': 'The Xianzhou Luofu',
#     'penacony': 'Penacony',
#     'astral_express': 'The Astral Express',
# }

# with ui.row():
#     with ui.column():
#         ui.markdown('## **Planets**')
#         ui.select(names, multiple=True, value=list(names.keys()), label=None, clearable=True) \
#             .classes('w-64').props('use-chips')

# ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'))

# ui.run()


