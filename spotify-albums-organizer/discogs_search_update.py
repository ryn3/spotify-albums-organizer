import pymongo
import discogs_client

client = pymongo.MongoClient("localhost", 27017)
db = client.discogs_masters
current_albums = db.current_albums

d = discogs_client.Client('discogs-spotify/0.1', user_token="dWWIJonGNxkDNGsIbncBUtkMMBMygBoGIqbWeQcu")

while True:
	title = input("enter album title from db.current_albums: ")
	doc = db.current_albums.find({"items.album.name": title})
	search_title = input("enter album to search in Discogs: ")
	for album in doc:
		id = album["_id"]
		try:
			
			artist = album["items"]["album"]["artists"][0]["name"]
			label = album["items"]["album"]["label"]
			year = album["items"]["album"]["release_year"]
			genres = album["items"]["album"]["genres"]
			styles = album["items"]["album"]["styles"]
		except Exception:
			styles = []
		print("Here is the current data: ")
		print("label: "+str(label))
		print("year: "+str(year))
		print("genres: "+str(genres))
		print("styles: "+str(styles))
		print()
		results = d.search(search_title, type='master')
		choose_next = input("Is this the correct data [y/n]? ")
		i = 0
		while (choose_next != 'y'):
			print("artist: "+str(results[i].main_release.artists[0].name))
			print("label: "+str(results[i].main_release.labels[0].name))
			print("year: "+str(results[i].main_release.year))
			print("genres: "+str(results[i].genres))
			print("styles: "+str(results[i].styles))
			choose_next = input("Is this the correct data [y/n]? ")
			if (choose_next == "n"):
				i+=1
		

		album["items"]["album"]["release_year"] = results[0].main_release.year
		album["items"]["album"]["genres"] = results[0].genres
		album["items"]["album"]["styles"] = results[0].styles
		album["items"]["album"]["label"] = results[0].main_release.labels[0].name

		db.current_albums.update({"_id": id}, album)
		print()
		print("--Updated data--")
		print("label: "+str(album["items"]["album"]["label"]))
		print("year: "+str(album["items"]["album"]["release_year"]))
		print("genres: "+str(album["items"]["album"]["genres"]))
		print("styles: "+str(album["items"]["album"]["styles"]))
		print()
