db = connect("localhost:27017/discogs_masters");

db.current_masters.drop()
db.current_albums.drop()
db.temp.drop()