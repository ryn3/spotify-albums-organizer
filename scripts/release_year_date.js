var albums = db.current_albums.find()
var ids=[]
var i = 0
albums.toArray().forEach(function(document){
	try{
		var id = document.items.album.id
		year = String(document.items.album.release_date)
		year = year.substring(0,4)
		print(year)
		document.items.album.release_year = year
		print(document.items.album.release_year)
		db.current_albums.update({"items.album.id":id},document)
		print("oh yeahh")
	} catch(e){
		print("oh no "+document._id)
		i++
	}

})
print(i)

// ids.forEach(function(id){
// 	db.current_albums.deleteOne({"_id": id})
// })

db.current_albums.find({"_id": ObjectId("5d450cbecfd7e3a1f9b5d8de")}).pretty()

		// db.current_albums.delete({"_id": id})


