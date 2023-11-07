    
from pynput.mouse import Listener


def print_current_pos(x, y):
    print('The current pointer position is {0}'.format((x, y)))
    

with Listener(on_move=print_current_pos) as lis:
    lis.join()
    
