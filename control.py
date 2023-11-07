#from pynput.mouse import Controller
from pynput.keyboard import Controller


def control_mouse(x, y):
    mouse = Controller()
    print('The current pointer position is {0}'.format(mouse.position))
    mouse.position = (x, y)   #topleft of the screen is (0, 0)
    print('The new pointer position is {0}'.format(mouse.position))
   

def control_mouse():
    keyboard = Controller()
    keyboard.type("helow world")



control_mouse(10, 20)