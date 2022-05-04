# the biggest mistake ill ever make, i want this code to automatically play the game "Leaf blower Revolution Idle"
# made by CallMeRinChan and Zeehondie

import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab, Image

# TODO: number recognition

# recognising the leaves at the "counter", so that later on we can make it recognise the numbers besides it
screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()),cv2.COLOR_RGB2BGR) # format a screenshot so opencv can use it
leaf_img = cv2.imread('./images/leaf.png')
result = cv2.matchTemplate(screenshot, leaf_img, cv2.TM_CCOEFF_NORMED) # look if leaf_img is recognised inside of screenshot
