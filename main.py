# the biggest mistake ill ever make, i want this code to automatically play the game "Leaf blower Revolution Idle"
# made by CallMeRinChan and Zeehondie

# importing modules
import keyboard
import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab, Image

#variable declaration
leaf = 'leaf' # so we can change the leaf its looking for easier

# TODO: number recognition

# recognising the leaves at the "counter", so that later on we can make it recognise the numbers besides it

while True:
    if keyboard.is_pressed("="): # if the "=" key is pressed
        print("The code ran") # just some confirmation we used while debugging
        img = cv2.cvtColor(np.array(pyautogui.screenshot()),cv2.COLOR_RGB2BGR) # make a screenshot that cv2 can use
        leaf_img = cv2.imread(f"./images/{leaf}.png") # render the leaf by using the leaf variable we made earlier
        w, h = leaf_img.shape[:-1]
        result = cv2.matchTemplate(img, leaf_img, cv2.TM_CCOEFF_NORMED) # look for leaf_img within img
        threshold = .9 # how much the images need to match
        loc = np.where(result >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + h, pt[1] + w), (0, 0, 255), 2) # put a rectangle around the found result
            cv2.imwrite(f"./test.png", img) # save test.png
