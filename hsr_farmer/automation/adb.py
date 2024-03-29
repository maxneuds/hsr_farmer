import asyncio as aio
import cv2 as cv
import numpy as np
import subprocess
from ppadb.client_async import ClientAsync as AdbClient
from datetime import datetime as dt


DEVICE = '10.1.11.3:5555'
DEVICE = 'usb'


def logger(msg):
    dt_now = dt.now().strftime('%H:%M:%S')
    print(f'[{dt_now}] {msg}')

class ADB:
    def __init__(self, device='usb'):
        logger('try to disconnect from all devices')
        try:
            subprocess.run('adb disconnect', shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logger(f'Error executing command: {e}')
        logger('try to connect to device')
        try:
            if device == 'usb':
                subprocess.run('adb devices', shell=True, check=True)
            else:
                subprocess.run(f'adb connect {device}', shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logger(f'Error executing command: {e}')

    async def get_dev(self):
        logger('get device connection to adb')
        client = AdbClient(host='127.0.0.1', port=5037)
        devices = await client.devices()
        dev = devices[0]
        logger(f'Connected to: {dev.serial}')
        return dev

    async def get_screensize(self, dev):
        result = await dev.shell('wm size')
        hxw = result.strip().split()[2]
        h, w = hxw.split('x')
        return(int(h), int(w))

    async def get_screen(self, dev, custom_msg=False, debug=False):
        if custom_msg == False:
            logger('get screenshot from device')
        elif custom_msg == None:
            pass
        else:
            logger(custom_msg)
        # get screen from device
        im_byte_array = await dev.screencap()
        # convert to cv image
        screenshot = cv.imdecode(np.frombuffer(bytes(im_byte_array), np.uint8), cv.IMREAD_COLOR)
        if debug == True:
            cv.imshow('debug', screenshot)
            cv.setMouseCallback('debug', self.click_event)
            cv.waitKey(0)
            cv.destroyAllWindows()
        return(screenshot)

    # function to display the coordinates of
    # of the points clicked on the image
    def click_event(self, event, x, y, flags, params):
        # checking for left mouse clicks
        if event == cv.EVENT_LBUTTONDOWN:
            print(f'{x},{y}')