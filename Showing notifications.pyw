import time 
from plyer import notification

for i in range(3):
    notification.notify(title = "HEADING HERE", message=" DESCRIPTION HERE" , timeout=3) 

    time.sleep(5)
    
