db = connect("localhost:27017/discogs_masters");

var total_albums = db.current_albums.count()
var i = 1
var found = 0
print(db.current_albums.find({"items.album.genres":[]}).count() +" documents with empty genre data")
db.current_albums.find({"items.album.genres":[]}).forEach(function(document){
		// if ( document.items.album.genres == null ) {
					// print("This document is empty: "+document.items.album.genres)
					var id = document._id
					var artist = document.items.album.artists[0].name;
					var album  = document.items.album.name;
					// print(artist+ ", "+album+"\n")

					if (album.length >= 5){
						album = album.substring(0,5)
					}
					
					var discogs_doc = db.current_masters.findOne({"masters.master.artists.artist.name":  {$regex: artist, $options: "i" }, "masters.master.title": {$regex: album, $options: "i" }});
					if (discogs_doc != null) {
						if (typeof discogs_doc.masters.master.genres !== "undefined"){
							var genres = discogs_doc.masters.master.genres.genre;
							document.items.album.genres = genres;
							if (typeof discogs_doc.masters.master.styles !== "undefined" ){
								var styles = discogs_doc.masters.master.styles.style;
								document.items.album.styles = styles;
							}
						}
						var year   = discogs_doc.masters.master.year;
						document.items.album.release_year = year;
						db.current_albums.update( {"_id": id}  , document)
						print("+"+("("+i+"/"+total_albums+") ")+document.items.album.name + " by " + artist + " was found.");
						found++
					} else {
						db.current_albums_DIRTY.insert(document)
						print("-"+("("+i+"/"+total_albums+") ")+document.items.album.name + " by " + artist + " was null.");
					}
					i++ 
					print(i)
		// }

})



print(found+"/"+total_albums+" albums were found.")
