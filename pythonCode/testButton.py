<<<<<<< HEAD
from utils import buttonSwitch as button
import time

def switch():
    global lamp
    if lamp == 'on':
        button.buttonOn()
        lamp = 'off'
    else:
        button.buttonOff()
        lamp = 'on'
    print(lamp)

button.on_button.config(command = switch)

lamp = 'off'

while button.x == True:
    button.update()
=======
from utils import buttonSwitch as button
import time

def switch():
    global lamp
    if lamp == 'on':
        button.buttonOn()
        lamp = 'off'
    else:
        button.buttonOff()
        lamp = 'on'
    print(lamp)

button.on_button.config(command = switch)

lamp = 'off'

while button.x == True:
    button.update()
>>>>>>> a406e59877fd3017b5c5d39c9ee713d9a18c3f59
