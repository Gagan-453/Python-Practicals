import os
from win10toast import ToastNotifier

def notification():
    toast = ToastNotifier()
    title = "Flash Chat"
    msg = "Hi"
    icon = 'icon.ico'
    length=30

    toast.show_toast(title, msg, icon_path=icon, duration=length)

notification()