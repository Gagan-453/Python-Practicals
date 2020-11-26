import base64

with open("Bird.png", "rb") as image_file:
    image_data_base64_encoded_string = base64.b64encode(image_file.read())
    
import tkinter as tk

root = tk.Tk()

im = tk.PhotoImage(data=image_data_base64_encoded_string)

tk.Label(root, image=im).pack()

root.mainloop()