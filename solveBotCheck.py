import json
import pyautogui
from time import sleep
import os
from bs4 import BeautifulSoup
import threading
current_directory = os.getcwd()
print(current_directory)
def getPath(RelativePath,notImage=False):
    if notImage:
        p = os.path.join(current_directory,RelativePath)
        print(p)
        return p
    return os.path.join(current_directory,RelativePath+'.png')

start = getPath('start')
reload = getPath('reload')
submit = getPath('submit')
nextTarget = getPath('nextTarget')

current = ''
directions = {
    'none': 0,
    'n': 0,
    'ne': 0,
    'e': 0,
    'se': 0,
    's': 0,
    'sw': 0,
    'w': 0,
    'nw': 0
}
def __waitUntilWindow__(callback,repeat,y=False):
    while not pyautogui.locateCenterOnScreen(start):
        sleep(0)
    print("RUNNING")
    callback()
    if(repeat and y):
        while pyautogui.locateCenterOnScreen(start):
            sleep(0)
        __waitUntilWindow__(callback,repeat)
def waitUntilWindow(callback,repeat):
    threading.Thread(target=__waitUntilWindow__,args=(callback,repeat,True)).start()
animalPassed = False
def checkAnimal(path):
    global animalPassed
    global directions
    print(path)
    b = not not pyautogui.locateCenterOnScreen(path,confidence=.65)
    if b:
        print(path)
        animalPassed = True
def check(path,dir='n'):
    global directions
    b = not not pyautogui.locateCenterOnScreen(path,confidence=.82)
    if b:
        directions[dir] +=1
tries = 0
def animalfun(direction):
    print(direction)
    global animalPassed
    global tries
    tries +=1
    if tries > 6:
        #pyautogui.click(pyautogui.locateCenterOnScreen(reload)) #Closes Gui
        #passVertifcation()
        return
    
    directoryPath = os.path.join(getPath('animals',True), direction)
    print(directoryPath)
    children = os.listdir(directoryPath)    
    for childName in children:
        childPath = os.path.join(directoryPath, childName)
        checkAnimal(childPath)
    if animalPassed:
        print('Animal passed')
        pyautogui.click(pyautogui.locateCenterOnScreen(submit)) #Submit's
    else:
        print("Moving to NEXT target")
        nextPosition = pyautogui.locateCenterOnScreen(nextTarget)
        pyautogui.click(nextPosition) #Move to next animal
        sleep(.01)
        animalfun(direction)

def passVertifcation():
    sleep(2)
    st = pyautogui.locateCenterOnScreen(start)
    if(st):
        pyautogui.click(st)
    directoryPath = getPath('dir',True)
    print("AHHHHH")
    print(directoryPath)
    children = os.listdir(directoryPath)
    for childName in children:
        childPath = os.path.join(directoryPath, childName)
        check(childPath, childName.split('.')[0])
    print(directions)
    direction = max(directions, key=lambda key: directions[key])
    if not direction or direction=='none':
        pass
        #pyautogui.click(pyautogui.locateCenterOnScreen(reload))  # Closes Gui
        #passVertifcation()
    else:
        animalfun(direction)
        print("DONE")
passVertifcation()
#waitUntilWindow(passVertifcation,True)
#sleep(1000)