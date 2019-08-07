"""
	Imports album images to the app for easy access for display_albums.py.

"""

import os.path
import os
import shutil
import urllib.request
import pymongo
from sys import stdout
from time import sleep


client = pymongo.MongoClient("localhost", 27017)
db = client.discogs_masters

all_albums = db.current_albums.find()

i = 1
for album in all_albums:
	
	try:
		url = album["items"]["album"]["images"][0]["url"]
		album_id = album["items"]["album"]["id"]
		filename = str(url)+".jpg"
		file = album_id
		urllib.request.urlretrieve(url,file)
		shutil.move(file, "data/images/"+file)
		i+=1
		denom = '/'+str(all_albums.count())
		stdout.write("\r%d" % i +denom)
		stdout.flush()
	except Exception:
		i+=1
		print(str(i)+" doesn't work.")
	


