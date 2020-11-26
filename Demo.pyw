import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
from time import *
f = open("write.txt", 'w')
sleep(10)
for i in range(100):
    f.write("hello\n")
f.close()