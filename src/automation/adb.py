import asyncio as aio
import cv2 as cv
import numpy as np
import subprocess
from ppadb.client_async import ClientAsync as AdbClient
from datetime import datetime as dt
from logger import logger

class ADB:
    def __init__(self, device):
        logger.info('try to disconnect from all devices')
        try:
            subprocess.run('adb disconnect', shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logger(f'Error executing command: {e}')
        logger.info('try to connect to device')
        try:
            if device == 'usb':
                subprocess.run('adb devices', shell=True, check=True)
            else:
                subprocess.run(f'adb connect {device}', shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logger(f'Error executing command: {e}')

    async def get_dev(self):
        logger.info('get device connection to adb')
        client = AdbClient(host='127.0.0.1', port=5037)
        devices = await client.devices()
        dev = devices[0]
        logger.info(f'Connected to: {dev.serial}')
        return dev

    async def get_screensize(self, dev):
        result = await dev.shell('wm size')
        hxw = result.strip().split()[2]
        h, w = hxw.split('x')
        return(int(h), int(w))

    async def get_screen(self, dev, custom_msg=False, debug=False):
        if custom_msg == False:
            logger.info('get screenshot from device')
        elif custom_msg == None:
            pass
        else:
            logger.info(custom_msg)
        # get screen from device
        success = False
        while not success:
            try:
                im_byte_array = await dev.screencap()
                success = True
            except KeyboardInterrupt:
                logger.debug('Ctrl+C detected. Exiting gracefully.')
                exit()
            except:
                await aio.sleep(0.1)
        # convert to cv image
        screenshot = cv.imdecode(np.frombuffer(bytes(im_byte_array), np.uint8), cv.IMREAD_COLOR)
        if debug == True:
            cv.imshow('debug', screenshot)
            cv.imwrite('debug.png', screenshot)
            cv.setMouseCallback('debug', self.click_event)
            cv.waitKey(0)
            cv.destroyAllWindows()
        return(screenshot)

    # function to display the coordinates of
    # of the points clicked on the image
    def click_event(self, event, x, y, flags, params):
        # checking for left mouse clicks
        if event == cv.EVENT_LBUTTONDOWN:
            logger.debug(f'{x},{y}')