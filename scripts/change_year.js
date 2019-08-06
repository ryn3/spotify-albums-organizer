use discogs_masters
id = "5d44ac9c98d39042582be52b"
new_year = "1977"
var change = db.current_albums.findOne({"_id": ObjectId(id)})
change.items.album.release_year = new_year
db.current_albums.update({"_id": ObjectId(id)}, change)
print("new year: "+ db.current_albums.findOne({"_id": ObjectId(id)}).items.album.release_year)
