import asyncio as aio
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
    penacony = worlds.Penacony(DEVICE)
    amphoreus = worlds.Amphoreus(DEVICE)
    
    # dev
    # await extra.restore_tp(tp=2)
    # await extra.restore_tp(tp=4)
    # await jarilo_vi.dev()
    # await jarilo_vi.silvermane_guard.restore_tp(tp=4.2)
    # await xianzhou_luofu.dev()
    # await penacony.dev()
    # await penacony.paperfold_university.restore_tp(tp=4)        # TP:+4->5 Time:???
    # await penacony.audition_venue.farm()
    # await penacony.farm() # TP:??? R2:5 R4:3
    # await amphoreus.okhema.restore_tp(tp=4.1)               # TP:+4->5 Time:???
    # raise SystemExit()
    
    # daily grind
    await extra.craft_items(['trick_snack', 'punitive_energy'])
    await herta_space_station.farm() # TP:+5->5
    await jarilo_vi.farm() # TP:+0->5 R2/4:0
    await xianzhou_luofu.farm() # TP:+0->5 R2:1 R4:0
    await penacony.farm() # TP:??? R2:5 R4:3

if __name__ == '__main__':
    try:
        aio.run(main())
    except KeyboardInterrupt:
        logger.debug('Ctrl+C detected. Exiting gracefully.')
        exit()


