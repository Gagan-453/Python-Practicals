import os
import sys
def run_in_bg(a):
    if a == True:
        os.system(r'cmd /c "pyw server_test.py"')
    else:
        sys.exit()
    
if __name__ == '__main__':
    run_in_bg(True)