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
    # await herta_space_station.farm() # status: 4/4 checked & stable
    # await penacony.farm() # status: 3/3 debug/fix needed in reverie
    await jarilo_vi.farm() # status: 2/7,
    # await the_xianzhou_luofu.farm() # status: 7/7 debug/fix needed in divination
    # xp before: 97162 (sampo)
    # xp after: 164446
    # total mapped xp: 67k/100k

    # await self.bot.adb.get_screen(dev=self.bot.dev, debug=True)
    # await adb.get_screen(dev=dev, debug=True)
    # await self.bot.adb.get_screen(dev=dev, debug=True)

if __name__ == '__main__':
    aio.run(main())
