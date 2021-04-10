import pyautogui
from pyautogui import *
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while True:
    if pyautogui.pixel(487,269)[0]==0:
         click(487,269)
    if pyautogui.pixel(604,269)[0]==0:
         click(604,269)
    if pyautogui.pixel(713,269)[0]==0:
         click(713,269)
    if pyautogui.pixel(819,269)[0]==0:
         click(819,269)
    if pyautogui.pixel(487,369)[0]==0:
         click(487,369)
    if pyautogui.pixel(604,369)[0]==0:
         click(604,369)
    if pyautogui.pixel(713,369)[0]==0:
         click(713,369)
    if pyautogui.pixel(819,369)[0]==0:
         click(819,369)
    if pyautogui.pixel(470,492)[0]==0:
         click(487,492)
    if pyautogui.pixel(604,469)[0]==0:
         click(604,469)
    if pyautogui.pixel(713,469)[0]==0:
         click(713,469)
    if pyautogui.pixel(819,469)[0]==0:
         click(819,469)
    if pyautogui.pixel(487,573)[0]==0:
         click(487,573)
    if pyautogui.pixel(604,573)[0]==0:
         click(604,573)
    if pyautogui.pixel(713,573)[0]==0:
         click(713,573)
    if pyautogui.pixel(819,571)[0]==0:
         click(819,571)
