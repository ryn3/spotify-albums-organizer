import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.discogs_masters
empty = db.current_albums.find({"items.album.genres":[]},{"items.album.name": 1, "items.album.artists.name":1})

i = 0
for album in empty:
	print(str(i)+". title: "+str(album["items"]["album"]["name"]))
	print("   artist: "+str(album["items"]["album"]["artists"][0]["name"]))
	i+=1
