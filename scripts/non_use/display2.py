import io
import base64
import requests
from PIL import ImageTk, Image
from io import BytesIO
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
root = tk.Tk()

 

def load_image_to_base64(image_url):
    """ Load an image from a web url and return its data base64 encoded"""
    image_byt = urlopen(image_url).read()
    image_b64 = base64.encodestring(image_byt)
    return image_b64

# load photos to photos list
urllist = [ 'https://i.scdn.co/image/87b6a28acfa2b9b26c5d8673648286cf85b07d01','https://i.scdn.co/image/7a4c5d294faefbb25aa20f681ee47ab83ac85792',]
photos = []

w = 800
h = 600
x = 200
y = 300

root.geometry("%dx%d+%d+%d" % (w, h, x, y))

cv = tk.Canvas(bg='white')


for i, url in enumerate(urllist):
    print(i,"loading",url)
    try:
        # img_url = "https://i.scdn.co/image/6187aeb7e2e51ebeffe88f2bb7f46391e5a8cafa"
        response = requests.get(url)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        cv.create_image(10, 10, image=img, anchor='nw')

        # photo = tk.PhotoImage(data=load_image_to_base64(url))
        photos.append(img)
        print("done")
    # except HTTPError as err:
    #     print("image not found, http error code:", err.code)
    except ValueError:
        print("invalid url", url)

cv.pack(side='top', fill='both', expand='yes')
# iterate through photos and put them onto the canvas
for photo in photos:
    cv.create_image(10*i, 10*i, image=photo, anchor='nw')

root.mainloop()