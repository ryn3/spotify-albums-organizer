Import your saved albums from Spotify and the monthly Discogs masters data -- ~1.5GB -- into MongoDB. You will have to download the XML Discogs masters data into the local directory. Since Spotify data lacks information about genre and subgenres (styles), discogs-spotify-import retrieves genre and subgenre data from the Discogs library and updates the Spotify data.

The Mongo database is "discogs_masters" and the collections are "current_albums" (saved Spotify albums) and "current_masters" (Discogs masters). 

Use these commands to get started:

	chmod +x run.sh
	./run.sh <spotify-id> <discogs-masters-xml-file>

(You can find your spotify id on your browser's tab when you go to https://open.spotify.com/settings/account)



