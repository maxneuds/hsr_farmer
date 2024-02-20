
import asyncio as aio
from datetime import datetime as dt


# from time import sleep
# from mss import mss
# from difflib import get_close_matches
# import pytesseract as tes
# import numpy as np
# import cv2 as cv
# import re
# from ppadb.client_async import ClientAsync as AdbClient
# # from asyncio import sleep, run, subprocess, create_subprocess_shell


# from worlds.herta_space_station import World as herta_space_station
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
    # initialize bot
    xy = OnePlus7T()
    adb = ADB()
    dev = await adb.get_dev()
    bot = Bot(adb=adb, dev=dev, xy=xy)
    # load worlds
    herta_space_station = Herta_Space_Station(bot=bot, xy=xy)
    penacony = Penacony(bot=bot, xy=xy)
    the_xianzhou_luofu = The_Xianzhou_Luofu(bot=bot, xy=xy)
    jarilo_vi = JariloVI(bot=bot, xy=xy)
    # farm worlds
    await herta_space_station.farm()
    # await penacony.farm()
    # await the_xianzhou_luofu.farm()
    # await jarilo_vi.farm()

    # await adb.get_screen(dev=dev, debug=True)
    # await self.bot.adb.get_screen(dev=dev, debug=True)

if __name__ == '__main__':
    aio.run(main())
