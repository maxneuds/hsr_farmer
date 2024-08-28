import asyncio as aio
from nicegui import ui
from sys import exit
from datetime import datetime as dt
from logger import logger, log_runtime
import worlds


# DEVICE = 'usb'
DEVICE = '10.1.11.3:5555'
MODE = 'xp' # options: credits, xp


async def main():
    # load worlds
    universal = worlds.universal.Init(DEVICE)
    astral_express = worlds.astral_express.Init(DEVICE)
    herta_space_station = worlds.herta_space_station.Init(DEVICE)
    jarilo_vi = worlds.jarilo_vi.Init(DEVICE)
    xianzhou_luofu = worlds.xianzhou_luofu.Init(DEVICE)
    penacony = worlds.penacony.Init(DEVICE, mode=MODE)
    
    # dev
    # daily for free (guranteed): R2: 25, R4: 5
    # await universal.restore_tp(tp=4)
    # await xianzhou_luofu.farm()
    # await penacony.dev()
    await penacony.farm()
    # await xianzhou_luofu.the_shackling_prison.farm()
    # await penacony.dreams_edge.path_6()
    # await penacony.dreams_edge.path_7()
    # await penacony.dreams_edge.path_8()
    # await penacony.the_reverie_dreamscape.path_12()
    # await penacony.the_reverie_dreamscape.path_13()
    # await penacony.the_reverie_dreamscape.path_14()
    # await penacony.the_reverie_dreamscape.path_15()
    # await penacony.the_reverie_dreamscape.rest_tp4()
    # await penacony.the_reverie_dreamscape.path_16()
    # await penacony.the_reverie_dreamscape.rest_tp2()
    # await penacony.the_reverie_dreamscape.path_17()
    # await penacony.penacony_grand_theater.farm()
    raise SystemExit()
    
    # preperations
    await xianzhou_luofu.stockup()
    await universal.crafting()

    # farm worlds
    await herta_space_station.farm() # TP:+5->5 ✓
    await jarilo_vi.farm() # TP:+0->5 R2/4:0 ✓
    await xianzhou_luofu.farm() # TP:+0->5 R2:2 R4:3
    # await penacony.farm()
    
    # checkout
    await astral_express.checkout()
    
    
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


