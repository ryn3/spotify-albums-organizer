"""
	Cleans album data by updating parameters (label, release year, genres, styles).

"""

import os
import pymongo
from sys import stdout

class cleanData:

	def inputParam(parameter,document):
		"""
			return updated document

			param: album parameter data such as genres, styles, and label
	
		"""
		if (parameter == "genres" or parameter == "styles"):
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
		else:
			genre = input(parameter+": ")
			document["items"]["album"][parameter] = genre

		return document


	client = pymongo.MongoClient("localhost", 27017)
	db = client.discogs_masters

	next_album = ''
	while(next_album != "n"):
		album_name = input("Enter album name: ")

		doc = db.current_albums.find({"items.album.name": album_name})
		for album in doc:
			try:
				id = album["_id"]
				artist = album["items"]["album"]["artists"][0]["name"]
				label = album["items"]["album"]["label"]
				year = album["items"]["album"]["release_year"]
				genres = album["items"]["album"]["genres"]
				styles = album["items"]["album"]["styles"]
			except Exception:
				styles = []


			print("Title: "+album_name)
			print("Artist: "+artist)
			print("Label: "+label)
			print("Year: "+year)
			print("Genre(s): "+str(genres))
			print("Style(s): "+str(styles))

			parameter = ''
			while (parameter != "exit"):
				parameter = input("Select parameter to update ([label], [release_year], [genres], [styles], exit): ")
				updates = ""
			
				# if (parameter == "genres" or parameter == "styles"):
				# 	# print("If more than one, use array brackets []")
				# 	inputParam(parameter,album)
				# 	# updates = input("Input updates for "+parameter+": ")
				# 	in
				# else:
				# 	updates = input("Input updates for "+parameter+": ")

				
				# print(id)
				if (parameter != "exit"):
					inputParam(parameter,album)
					# album["items"]["album"][parameter] = updates
					db.current_albums.update({"_id": id}, album)

		
		next_album = input("Update another [y/n]? ")

	print("Goodbye.")

