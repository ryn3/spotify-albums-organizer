db = connect("localhost:27017/discogs_masters");

var docs = db.temp.aggregate([{$unwind: {path: "$items"}}, {$project: {"_id": 0}}])
db.temp2.insert(docs.toArray())

if (db.current_albums.count() > 0) {
	print('db.current_albums.count()>0')
	// var current = db.current_albums.find()
	// var temp2 = db.temp2.find()

	db.current_albums.find().forEach(function(document){
		// print(document)
		try {
			var current_artist = document.items.album.artists[0].name
			var current_album = document.items.album.name
			var current_id = document.items.album.id
			// print(current_id)
			if (db.temp2.find({"items.album.id": current_id}).toArray().length == 0 ) {
				db.current_albums.deleteOne({"items.album.id": current_id})
				print("deleteOne")
			}
		} catch(e){
			print("does not contain album delete")
		}
	})

	print("pass")

	db.temp2.find().forEach(function(document){
		// print(document.toArray())
		try{
			// var temp2_id = document.items.album.id
			var temp2_artist = document.items.album.artists[0].name
			var temp2_album = document.items.album.name
			var temp2_id = document.items.album.id

			// print(temp2_artist+":  "+temp2_album)
			if (db.current_albums.find({"items.album.id": temp2_id}).toArray().length == 0  ) {
				db.current_albums.insert(document)
				print("insert")
			}
		} catch(e){
			print("does not contain album insert")
		}
	})

} else {
	db.current_albums.insert(docs.toArray())
}
db.temp2.drop()
db.temp.drop()
print("current_albums contains "+db.current_albums.count()+" albums.")