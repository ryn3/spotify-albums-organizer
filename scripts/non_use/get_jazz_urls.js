


use discogs_masters


db.jazz_albums.insert(jazz.toArray())


var jazz = db.current_albums.find({"items.album.genres":"Jazz"})

var albums = []
jazz.forEach(function(doc){
	url = doc.items.album.images[0].url
	albums.push('"'+url+'"')

})
print('['+albums+']')