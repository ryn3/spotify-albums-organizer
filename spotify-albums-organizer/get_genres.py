import pymongo
import discogs_client
import time
from sys import stdout

# t_end = time.time() + 60 * 15

client = pymongo.MongoClient("localhost", 27017)
db = client.discogs_masters2
d = discogs_client.Client('discogs-spotify/0.1', user_token="dWWIJonGNxkDNGsIbncBUtkMMBMygBoGIqbWeQcu")

total_albums = db.current_albums.count()
i = 1
found = 0
albums = db.current_albums.find({"items.album.genres":[]})
print(str(albums.count()) +" documents with empty genre data")

for document in albums:
	db_id = document["_id"]
	db_artist = document["items"]["album"]["artists"][0]["name"]
	db_album  = document["items"]["album"]["name"]
	query = db_artist+" "+db_album
	# if (album.length >= 5):
	# 	album = album.substring(0,6)
	try: 
		master = d.search(query, type="release")[0].master
		# print(master)
		document["items"]["album"]["name"] = master.title
		document["items"]["album"]["artists"][0]["name"] = master.main_release.artists[0].name
		document["items"]["album"]["genres"] = master.genres
		document["items"]["album"]["styles"] = master.styles
		document["items"]["album"]["label"] = master.main_release.labels[0].name
		document["items"]["album"]["release_year"] = master.main_release.year
		print("+"+("("+str(i)+"/"+str(total_albums)+") ")+db_album + " by " + db_artist + " was found.")

		db.current_albums.update( {"_id": db_id}  , document)
		found += 1

	except discogs_client.exceptions.HTTPError:
		# albums.append(document)
		t_end = time.time() + 30
		while time.time() < t_end:
			# print('waiting '+str(int(t_end)))
			denom = '/'+str(int(t_end))
			total_time = int(t_end) - int(time.time())

			stdout.write("\rWait %d" % total_time+"s...")
			stdout.flush()
		stdout.write("\n")

	except Exception:
		# print(Exception)
		print("-"+("("+str(i)+"/"+str(total_albums)+") ")+db_album + " by " + db_artist + " was null.");
	i+=1


print(str(found)+"/"+str(total_albums)+" albums were found.")
