from pynput import mouse
import pyautogui
    
cnt = 0

#One of the features of Wayland is its security design, which helps to guard the user against malicious apps. Apps can no longer see everything on the screen and spy on you. But that also means you cannot run a common application (like shutter or gtk-recordmydesktop) and use it to make a screenshot or a screencast of your desktop – it will see only its own window, but nothing else (or it might crash right away). System (trusted) apps need to be used to perform these actions.
def take_screenshot():
    global cnt
    im = pyautogui.screenshot()
    path = "img/" + str(cnt) + ".png"
    print(path)
    cnt = cnt + 1
    im.save(path)
   

def control_mouse(x, y):
    mouse = mouse.Controller()
    print('The current pointer position is {0}'.format(mouse.position))
    mouse.position = (x, y)   #topleft of the screen is (0, 0)
    print('The new pointer position is {0}'.format(mouse.position))
   


def print_current_pos(x, y):
    print('The current pointer position is {0}'.format((x, y)))
    

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    take_screenshot()

 

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
    
with mouse.Listener(on_move=print_current_pos, on_click=on_click, on_scroll=on_scroll) as lis:
    lis.join()


