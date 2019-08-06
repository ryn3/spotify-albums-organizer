import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
 
root = tk.Tk()
img_url = "https://i.scdn.co/image/6187aeb7e2e51ebeffe88f2bb7f46391e5a8cafa"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
# img = Scale(img, from_=0, to=200)
panel = tk.Button(root,activebackground='blue', image=img, )
# panel.invoke()


img_url = "https://i.scdn.co/image/7a4c5d294faefbb25aa20f681ee47ab83ac85792"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel.configure(image=img)
# panel.pack(side="bottom", fill="both", expand="yes")
panel.grid(row=5,column=5)
root.mainloop()