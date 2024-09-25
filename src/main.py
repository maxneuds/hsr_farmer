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
    extra = worlds.Extra(DEVICE)
    astral_express = worlds.Astral_Express(DEVICE)
    herta_space_station = worlds.Herta_Space_Station(DEVICE)
    jarilo_vi = worlds.Jarilo_VI(DEVICE)
    xianzhou_luofu = worlds.Xianzhou_Luofu(DEVICE)
    penacony = worlds.Penacony(DEVICE, mode=MODE)
    
    
    # dev
    # await extra.restore_tp(tp=2)
    # await extra.restore_tp(tp=4)
    # await jarilo_vi.rivet_town.farm()
    # await xianzhou_luofu.farm()
    # await xianzhou_luofu.the_shackling_prison.dev()
    # await penacony.farm()
    # await penacony.dev()
    # await penacony.audition_venue.teleport()
    await penacony.audition_venue.farm()
    raise SystemExit()

    # preperations
    # daily for free (guranteed): R2: 25, R4: 5
    # await xianzhou_luofu.stockup() # disabled, got enough
    await extra.craft_items(['trick_snack', 'punitive_energy'])

    # farm worlds
    await herta_space_station.farm() # TP:+5->5 ✓✓
    await jarilo_vi.farm() # TP:+0->5 R2/4:0 ✓✓
    await xianzhou_luofu.farm() # TP:+0->5 R2:1 R4:0 ✓✓
    await penacony.farm() # TP:??? R2:5 R4:3
    
    # checkout
    await astral_express.checkout()
    
    
    # TOTAL XP: 116.340 / 119.256
    # TOTAL TIME: 
    
    
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


