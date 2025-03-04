import asyncio as aio
import cv2 as cv
import numpy as np
import subprocess
from ppadb.client_async import ClientAsync as AdbClient
from datetime import datetime as dt
from logger import logger

class ADB:
    def __init__(self):
        pass

    async def connect_dev(self, device, n_try=1):
        try:
            logger.info('try to disconnect from all devices')
            subprocess.run('adb disconnect', shell=True, check=True)
            await aio.sleep(0.25)
            logger.info(f'try to connect to device: {device}')
            if device == 'usb':
                subprocess.run('adb devices', shell=True, check=True)
            else:
                subprocess.run(f'adb connect {device}', shell=True, check=True)
            logger.info('connect to first device on local adb server')
            client = AdbClient(host='127.0.0.1', port=5037)
            devices = await client.devices()
            dev = devices[0]
            logger.info(f'connected to: {dev.serial}')
            await aio.sleep(1)
            return(dev)
        except subprocess.CalledProcessError as e:
            logger.info(f"[#{n_try}] Executing system command failed:\n{e}\nRetry in 1s...")
            await aio.sleep(1)
            self.dev = await self.connect_dev(device=device, n_try=n_try+1)
        except RuntimeError as e:
            logger.info(f"[#{n_try}] ADB connection to {device} failed:\n{e}\nRetry in 1s...")
            await aio.sleep(1)
            self.dev = await self.connect_dev(device=device, n_try=n_try+1)
        except IndexError as e:
            logger.info(f"[#{n_try}] ADB device {device} not found:\n{e}\nRetry in 1s...")
            await aio.sleep(1)
            self.dev = await self.connect_dev(device=device, n_try=n_try+1)
            


