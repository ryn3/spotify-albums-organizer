import pymongo

class pymongoUpdate:

	def inputParam(parameter, document):
		# print(parameter)
		genres_array = input("How many "+parameter+"? ")
		if (int(genres_array) > 1):
			number = int(genres_array)
			genres = []
			for i in range(0, number):
				genre = input(parameter+": ")
				genres.append(genre)
			document["items"]["album"][parameter] = genres
		elif (int(genres_array) == 1):
			genre = input(parameter+": ")
			document["items"]["album"][parameter] = genre
		# print(0)


	client = pymongo.MongoClient("localhost", 27017)
	db = client.discogs_masters
	current_albums = db.current_albums
	# print(current_albums.count())
	# "items.album.genres": [], 
	dirty = current_albums.find({"items.album.genres": []})
	dirty_num = dirty.count()

	for document in dirty:
		# document = dirty[i]
		# print(document["items"]["album"]["name"])
		doc_id = document["_id"]
		artist = document["items"]["album"]["artists"][0]["name"]
		album = document["items"]["album"]["name"]
		print(album +": "+artist)
		# genres_array = input("How many genres? ")
		# if (genres_array > 1):
		# 	number = int(genres_array)
		# 	genres = []
		# 	for i in (0, number):
		# 		genre = input("Genre: ")
		# 		genres.append(genre)
		# 	document["items"]["album"]["genres"] = genres
		# else:
		# 	genre = input("Genre: ")
		# 	document["items"]["album"]["genres"] = genre

		# genres_array = input("What is the genre(s)? ")
		# # list(map(int, input().split()))
		
		# styles = input("What is the style(s)? ")
		# document["items"]["album"]["styles"] = styles

		inputParam("genres",document)
		inputParam("styles",document)
		year = input("What is the year? ")
		document["items"]["album"]["year"] = year


		db.current_albums.update({"_id": doc_id}, document)

