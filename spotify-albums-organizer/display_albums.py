"""
	Displays saved Spotify albums in a GUI. Click on an album cover to open album's Spotify page.

"""

import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
from sys import stdout
import pymongo
from functools import partial
import webbrowser

def go_to(url):
	"""
		Opens the Spotify album's URL in open.spotify.com

	"""
	webbrowser.open(url)

def onFrameConfigure(canvas):
    """
    	Reset the scroll region to encompass the inner frame

    """
    canvas.configure(scrollregion=canvas.bbox("all"))

def truncate(param):
	"""
		return a substring of param to fit column grid

		:param: album data parameter such as label, year, and album title

	"""
	max = 21
	if (len(param) > max):
		param = param[:max]
	return param

"""
	Select sorting options

"""
client = pymongo.MongoClient("localhost", 27017)
db = client.discogs_masters
print("Input is case-sensitive!")
genre = input("choose genre([Electronic], [Jazz], [Rock], [Classical], [Funk / Soul], [Hip Hop], all): ")
param = input("choose sorting option([release_year], [name], [artists[0].name], [label], [genres], [added_at]): ")
sort_option = "items.album."+param
direction = input("choose direction([ascending], [descending]): ")

"""
	Check if release_year type is string. Update if necessary.

"""
albums = db.current_albums.find()
for album in albums:
	try:
		id = album["_id"]
		year = album["items"]["album"]["release_year"]
		year = str(year)
		album["items"]["album"]["release_year"] = year
		# str(album["items"]["album"]["release_year"])
		db.current_albums.update({"_id": id}, album)
	except Exception:
		j = 0


select_albums = 0
if (direction == "ascending" and genre != 'all'):
	select_albums = db.current_albums.find({"items.album.genres": genre}).sort(sort_option, pymongo.ASCENDING)
elif (direction == "descending" and genre != 'all'):
	select_albums = db.current_albums.find({"items.album.genres": genre}).sort(sort_option, pymongo.DESCENDING)
elif (direction == "ascending" and genre == 'all'):
	select_albums = db.current_albums.find().sort(sort_option, pymongo.ASCENDING)
elif (direction == "descending" and genre == 'all'):
	select_albums = db.current_albums.find().sort(sort_option, pymongo.DESCENDING)

"""
	Retrieve album data from db.current_albums

"""
photos = []
object_ids = []
ids = []
names = []
artists = []
labels = []
years = []
genres = []
urls = []

for album in select_albums:
	try:
		object_id = album["_id"]
		id = album["items"]["album"]["id"]
		name = album["items"]["album"]["name"]
		artist = album["items"]["album"]["artists"][0]["name"]
		label = album["items"]["album"]["label"]
		year = album["items"]["album"]["release_year"]
		genre = album["items"]["album"]["genres"]
		url = album["items"]["album"]["external_urls"]["spotify"]

		object_ids.append(object_id)
		ids.append(id)
		names.append(name)
		artists.append(artist)
		labels.append(label)
		years.append(year)
		genres.append(genre)
		urls.append(url)
	except Exception:
		print(album["items"]["album"]["name"]+" doesn't work.")

"""
	Create tkinter canvas

"""
root = tk.Tk()
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff", width=1440, height=800)
frame = tk.Frame(canvas, background="#ffffff")
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((15,15), window=frame, anchor="nw")
frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))


i=0
cols = 8
a = int(len(ids)/cols)+1

for r in range(a):
	for c in range(cols):
		try:
			filename = ids[i]
			img = ImageTk.PhotoImage(Image.open("../data/images/"+filename).resize((150, 150), Image.ANTIALIAS))
			photos.append(img)
			name = truncate(names[i])
			artist = truncate(artists[i])
			label = truncate(labels[i])
			url = urls[i]

			"""
				Display album image. Hyperlink to album's Spotify page.
			
			"""
			tk.Button(frame,image=photos[i], borderwidth=10 ,command=partial(go_to, url)).grid(row=4*r,column=c)
			
			"""
				Display album name and artist.
			
			"""
			tk.Label(frame, text=str(artist)).grid(row=(4*r)+1, column=c)
			tk.Label(frame, text=str(name)).grid(row=(4*r)+2, column=c)
			
			"""
				Display album ObjectId (selectable)

			"""
			
			# v = tk.StringVar()
			# w = tk.Entry(frame,textvariable=v,fg="black",bg="white",bd=0,state="readonly").grid(row=(4*r)+1, column=c)
			# v.set(object_ids[i])

			"""
				Display album label and year.
			
			"""
			tk.Label(frame, text=str(label[:13])+", " +years[i]).grid(row=(4*r)+3, column=c)

			"""
				Display album year.
			
			"""
			# tk.Label(frame, text=str(years[i])).grid(row=(4*r)+3, column=c)
			
			i+=1

			"""
				Display albums loading e.g. 5/112
			
			"""
			denom = '/'+str(len(ids))
			stdout.write("\rLoading %d" % i +denom+" albums...")
			stdout.flush()

		except IndexError:
			break

stdout.write("\n")
root.mainloop(  )