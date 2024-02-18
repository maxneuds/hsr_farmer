from pynput.keyboard import Key, Controller as PyKB
from pynput.mouse import Button, Controller as PyMouse
from time import sleep
from datetime import datetime as dt
from mss import mss
from difflib import get_close_matches
import pytesseract as tes
import numpy as np
import cv2 as cv
import re
import pyautogui

def logger(msg):
  dt_now = dt.now().strftime("%H:%M:%S")
  print(f"[{dt_now}] {msg}")

with mss() as sct:
  monitor = sct.monitors[1]
  if monitor['width'] > 1920:
    xfactor = monitor['width'] / 1920
    yfactor = monitor['height'] / 1080
  else:
    xfactor = 1
    yfactor = 1

kb = PyKB()
ms = PyMouse()

def get_sct_gs(scale=False, debug=False):
  with mss() as sct:
    sct_img = sct.grab(monitor)
    img = np.array(sct_img)
    img_gs = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
    if monitor['width'] > 1920 and scale:
      # fix resolution to 1920x1080
      img_gs = cv.resize(img_gs, (1920, 1080), interpolation = cv.INTER_AREA)
    if debug == True:
      cv.imshow('debug', img_gs)
      cv.waitKey(0)
      cv.destroyAllWindows()
  return(img_gs)

def get_sct_gs_area(x, y, w, h, debug=False):
  with mss() as sct:
    sct_img = sct.grab(monitor)
    img = np.array(sct_img)
    img_gs = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
    # fix resolution to 1920x1080
    img_resize = cv.resize(img_gs, (1920, 1080), interpolation = cv.INTER_AREA)
    # crop area
    img_crop = img_resize[y:y+h, x:x+w]
    if debug == True:
      cv.imshow('debug', img_crop)
      cv.waitKey(0)
      cv.destroyAllWindows()
  return(img_crop)

def get_white_text():
  sct_gs = get_sct_gs(scale=False)
  img = cv.threshold(sct_gs, 150, 255, cv.THRESH_BINARY_INV)[1]
  # cv.imshow('debug', img)
  # cv.waitKey(0)
  # cv.destroyAllWindows()
  ocr = tes.image_to_data(img, output_type=tes.Output.DICT, lang='eng')
  return(ocr)

def get_black_text():
  sct_gs = get_sct_gs(scale=False)
  img = cv.threshold(sct_gs, 150, 255, cv.THRESH_BINARY)[1]
  # cv.imshow('debug', img)
  # cv.waitKey(0)
  # cv.destroyAllWindows()
  ocr = tes.image_to_data(img, output_type=tes.Output.DICT, lang='eng')
  return(ocr)

def action_teleport():
  logger('click: Teleport')
  sleep(0.1)
  ms.click(Button.left, 1)
  sleep(1)
  ms.position = (monitor['left']+1650*xfactor, 970*yfactor)
  sleep(0.05)
  ms.click(Button.left, 1)
  sleep(5)
  logger('Teleported.')

def action_sprint_on():
  sleep(0.05)
  kb.press(Key.shift_l)
  sleep(0.05)
  kb.release(Key.shift_l)

def wait_fight_end():
  logger('wait for fight to end...')
  sleep(10)
  check = False
  # load search template
  img_chat = cv.imread('res/chat.png')
  img_chat = cv.cvtColor(img_chat, cv.COLOR_BGRA2GRAY)
  while check == False:
    # extract search region
    img_sct = get_sct_gs_area(x=27, y=945, w=45, h=51)
    # calculate match
    p_match = cv.matchTemplate(image=img_sct, templ=img_chat, method=cv.TM_CCORR_NORMED).item()
    print(p_match)
    check = p_match > 0.85
    sleep(0.5)
  logger('fight won.')



def farm_herta_base():
  # img = get_sct_gs(scale=True, debug=True)<
  # Farm: Base Zone
  # -> teleport
  logger('open map')
  kb.tap('<')
  sleep(1.25)
  logger('zoom map')
  ms.position = (monitor['left']+1000, 500)
  sleep(0.5)
  ms.scroll(0, -2000)
  logger('click: Base Zone')
  ms.position = (monitor['left']+1580*xfactor, 430*yfactor)
  sleep(0.05)
  ms.click(Button.left, 1)
  sleep(1)
  logger('click: Teleporter')
  ms.position = (monitor['left']+835*xfactor, 162*yfactor)
  sleep(0.05)
  ms.click(Button.left, 1)
  sleep(1)
  action_teleport()
  # -> farm monsters
  kb.press("s")
  action_sprint_on()
  sleep(2.3)
  kb.release("s")
  ms.click(Button.left, 1)
  wait_fight_end()
  sleep(0.5)




def farm_herta_storage():
  # img = get_sct_gs(scale=True, debug=True)
  # Farm: Storage Zone
  # -> teleport
  logger('open map')
  kb.tap('<')
  sleep(1.25)
  logger('zoom map')
  ms.position = (monitor['left']+1000, 500)
  sleep(0.5)
  ms.scroll(0, -2000)
  logger('click: Storage Zone')
  ms.position = (monitor['left']+1580*xfactor, 522*yfactor)
  sleep(0.05)
  ms.click(Button.left, 1)
  sleep(1)
  logger('click: Teleporter')
  ms.position = (monitor['left']+487*xfactor, 514*yfactor)
  sleep(0.05)
  ms.click(Button.left, 1)
  sleep(1)
  action_teleport()
  # -> farm monsters
  kb.press('s')
  action_sprint_on()
  sleep(4.4)
  kb.release('s')
  ms.click(Button.left, 1)
  wait_fight_end()
  sleep(0.5)
  kb.press('a')
  action_sprint_on()
  sleep(2.2)
  kb.release('a')
  kb.press('w')
  sleep(5)
  kb.release('w')



def farm_herta_seclusion():
  # img = get_sct_gs(scale=True, debug=True)
  # Farm: Storage Zone
  # -> teleport
  # logger('open map')
  # kb.tap('<')
  # sleep(1.25)
  # logger('zoom map')
  # ms.position = (monitor['left']+1000, 500)
  # sleep(0.5)
  # ms.scroll(0, -2000)
  # logger('click: Seclusion Zone')
  # ms.position = (monitor['left']+1580*xfactor, 720*yfactor)
  # sleep(0.05)
  # ms.click(Button.left, 1)
  # sleep(1)
  # logger('click: Teleporter')
  # img = get_sct_gs(scale=True, debug=True)
  # ms.position = (monitor['left']+877*xfactor, 300*yfactor) # anderer 735, 792
  # sleep(0.05)
  # ms.click(Button.left, 1)
  # sleep(1)
  # action_teleport()
  # -> farm monsters
  kb.press('w')
  action_sprint_on()
  sleep(0.75)
  kb.release('w')
  kb.press('d')
  sleep(5)
  kb.release('d')
  kb.press('s')
  sleep(2)
  kb.release('s')
  # ms.click(Button.left, 1)
  # wait_fight_end()


def farm_jarilo_snow():
  # img = get_sct_gs(scale=True, debug=True)
  logger('### Outlying Snow Plains ###')
  # -> teleport
  logger('open map')
  kb.tap('<')
  sleep(1.25)
  logger('zoom map')
  ms.position = (monitor['left']+900, 500)
  sleep(0.5)
  ms.scroll(0, -2000)
  sleep(0.5)
  logger('click: Outlying Snow Plans')
  ms.position = (monitor['left']+1600*xfactor, 425*yfactor)
  sleep(0.1)
  ms.click(Button.left, 1)
  sleep(1)
  logger('click: Teleporter')
  ms.position = (monitor['left']+1106*xfactor, 566*yfactor)
  action_teleport()
  # -> farm monsters
  kb.press('a')
  kb.press('s')
  action_sprint_on()
  sleep(3)
  kb.release('a')
  kb.release('s')
  kb.press('a')
  sleep(1.2)
  kb.release('a')
  kb.press('a')
  kb.press('s')
  sleep(1)
  kb.release('a')
  kb.release('s')
  ms.click(Button.left, 1)
  wait_fight_end()
  kb.press('a')
  kb.press('s')
  action_sprint_on()
  sleep(1.5)
  kb.release('a')
  kb.release('s')
  kb.press('a')
  sleep(2.5)
  kb.release('a')
  # -> new untested
  kb.press('w')
  sleep(5)
  kb.release('w')
  ms.click(Button.left, 1)
  wait_fight_end()
  # <- new untested
  logger('open map')
  kb.tap('<')
  sleep(1.25)
  logger('click: Teleporter')
  ms.position = (monitor['left']+768*xfactor, 388*yfactor)
  action_teleport()
  kb.press('s')
  sleep(1)
  kb.release('s')
  kb.press('a')
  sleep(10)
  kb.press('s')
  sleep(4.8)
  kb.release('s')
  kb.release('a')
  ms.click(Button.left, 1)
  wait_fight_end()
  kb.press('w')
  sleep(4.4)
  kb.press('a')
  sleep(1)
  kb.release('w')
  kb.release('s')
  ms.click(Button.left, 1)
  wait_fight_end()


def action_use_teleporter(x,y):
  sleep(1)
  logger('click: Teleporter')
  ms.position = (monitor['left']+x*xfactor, y*yfactor)
  action_teleport()

def action_select_location(y, scroll_down=False):
  logger('open map')
  kb.tap('<')
  sleep(1.25)
  logger('zoom map')
  ms.position = (monitor['left']+900, 500)
  sleep(0.5)
  ms.scroll(0, -2000)
  sleep(0.5)
  if scroll_down:
    logger('scroll locations')
    sleep(0.25)
    ms.position = (monitor['left']+1600*xfactor, 500)
    sleep(0.1)
    ms.click(Button.left, 1)
    sleep(0.25)
    ms.scroll(0, -500)
    sleep(1)
  logger('click: location')
  ms.position = (monitor['left']+1600*xfactor, y*yfactor)
  sleep(0.1)
  ms.click(Button.left, 1)

def farm_luofu_water():
  # img = get_sct_gs(scale=True, debug=True)
  logger('### Scalegorge Waterscape ###')
  # -> teleport
  action_select_location(y=933, scroll_down=True)
  action_use_teleporter(1313, 531)
  # -> farm monsters
  kb.press('s')
  sleep(4.4)
  kb.release('s')
  kb.press('d')
  sleep(2)
  kb.release('d')
  kb.press('w')
  sleep(3.3)
  kb.release('w')
  kb.press('d')
  sleep(3.8)
  kb.release('d')
  ms.click(Button.left, 1)
  wait_fight_end()
  sleep(1)
  ms.click(Button.left, 1)
  wait_fight_end()
  action_use_teleporter(125, 557)

def action_move_down(s):
    kb.press('s')
    sleep(s)
    kb.release('s')
    sleep(0.05)

def action_move_left(s):
    kb.press('a')
    sleep(s)
    kb.release('a')
    sleep(0.05)

def action_open_map():
    kb.tap('<')
    sleep(1.25)

print('startup')
sleep(1)
# img = get_sct_gs(scale=True, debug=True)
logger('### Scalegorge Waterscape ###')
# -> teleport
# action_select_location(y=842, scroll_down=True)
# action_use_teleporter(664, 739)
# action_open_map()
# action_use_teleporter(822, 897)
# -> farm monsters
#  -> group 1
# kb.press('s')
# sleep(4.22)
# kb.press('a')
# sleep(3)
# kb.release('a')
# kb.release('s')
# ms.click(Button.left, 1)
# wait_fight_end()
#  -> group 2

# ms.click(Button.left, 1)
# wait_fight_end()


# print(ms.position)
# ms.position = (500, 500)
ms.position = (monitor['left']+1000*xfactor, 500*yfactor)
# print(ms.position)
sleep(0.1)
ms.click(Button.right)
sleep(0.1)


# ms.move(-200, 100)
# sleep(1)
# ms.move(200, -100)
# pyautogui.move(-200, 0, duration=2)
# ms.position = (monitor['left']+900*xfactor, 500*yfactor)
# print(ms.position)

# farm_jarilo_snow()
# farm_herta_seclusion()


# img = get_sct_gs(scale=True, debug=True)


# 835,162

# # select: Base
# ocr = get_white_text()
# ocr_text = ocr['text']
# ocr_target = get_close_matches('Base', ocr_text)[0]
# idx = ocr_text.index(ocr_target)
# top = ocr['top'][idx]
# left = ocr['left'][idx]
# ms.position = (int(monitor['left']+left+1), int(top+1))

# # open: star rail map
# ocr = get_white_text()
# ocr_text = ocr['text']
# ocr_target = get_close_matches('Map', ocr_text)[0]
# idx = ocr_text.index(ocr_target)
# top = ocr['top'][idx]
# left = ocr['left'][idx]
# ms.position = (int(monitor['left']+left+10), int(top+10))
# sleep(0.05)
# ms.click(Button.left, 1)
# sleep(1.25)
# # select: herta space station
# while True:
#   ocr = get_white_text()
#   ocr_text = ocr['text']
#   ocr_target = get_close_matches('Herta', ocr_text)
#   if len(ocr_target) > 0:
#     ocr_target = ocr_target[0]
#     break
# idx = ocr_text.index(ocr_target)
# top = ocr['top'][idx]
# left = ocr['left'][idx]
# ms.position = (int(monitor['left']+left+100), int(top-50))
# sleep(0.05)
# for _ in range(20):
#   ms.click(Button.left, 1)
#   sleep(0.5)



# Scroll two steps down
# mouse.scroll(0, 2)


# ms.position = (0, 0)
# ms.move(-1600, 0)
# ms.position = (0, 0)


# Palace Ruin Depths
# kb.press("s")
# sprint_on()
# sleep(2.35)
# kb.release("s")
# kb.press("a")
# sleep(3)
# kb.release("a")

# Ancient Sea Palace Ruins
# sleep(0.05)
# kb.press("a")
# sleep(0.05)
# kb.press(Key.shift_l)
# sleep(0.05)
# kb.release(Key.shift_l)
# sleep(4.25)
# kb.press("s")
# sleep(0.05)
# kb.release("a")
# sleep(0.7)
# kb.press("a")
# sleep(0.05)
# kb.release("s")
# sleep(3.5)
# kb.release("a")


# keyboard.press("<")

# print('send keys')
# keyboard.press('a')
# sleep(3)
# keyboard.release('a')
