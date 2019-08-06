Import your saved albums from Spotify and the monthly Discogs masters data -- ~1.5GB -- into MongoDB. You will have to download the XML Discogs masters data into the local directory. Since Spotify data lacks information about genre and subgenres (styles), discogs-spotify-import retrieves genre and subgenre data from the Discogs library and updates the Spotify data.

The Mongo database (localhost: 27017) is "discogs_masters" and the collections are "current_albums" (saved Spotify albums) and "current_masters" (Discogs masters). 

Use these commands to get started:

	chmod +x run.sh
	./run.sh <spotify-id> <discogs-masters-xml-file>

(You can find your Spotify id on your browser's tab when you go to https://open.spotify.com/settings/account)
*This will take some time depending on the number of saved Spotify albums. On my 2015 MacBook Air, importing Discogs data, ~600 saved albums, and cross-referencing genre and style data took roughly an hour. 

Next, import the album cover images (This is to minimize url requests): 
	
	$ cd scripts
	$ python import_images.py

Once you've imported the Discogs data, your saved Spotify albums with their transferred genre and styles information, and the album images, consider either cleaning your data for more accurate data (i.e release year, label, etc.):
	
	$ cd scripts
	$ python clean_data.py
	$ Enter album name: Moondog
	$ Title: Moondog
	$ Artist: Moondog
	$ Label: Columbia Masterworks
	$ Year: 1969
	$ Genre(s): ['Jazz', 'Classical']
	$ Style(s): ['Big Band', 'Contemporary']
	$ Select parameter to update ([label], [release_year], [genres], [styles], exit): label
	$ label: CBS

or displaying your saved albums using a Python GUI:
	
	$ cd scripts
	$ python display_albums.py
	$ Input is case-sensitive!
	$ choose genre([Electronic], [Jazz], [Rock], [Classical], [Funk / Soul], [Hip Hop], all): Jazz
	$ choose sorting option([release_year], [name], [artists[0].name], [label], [genres], [added_at]): release_year
	$ choose direction([ascending], [descending]): descending
	$ Loading 194/219 albums...

In the GUI, click on an album cover to go to its Spotify page. You may customize the number of columns by changing "cols" in display_albums.py (line 93). 

If you want to update your saved album data (after you've added or deleted any saved albums from the Spotify app), run these commands:
	
	$ chmod +x update_saved_albums.sh
	$ ./update_saved_albums.sh <spotify-id>

Since the Discogs masters data is rather large and this app essentially requires a copy of that data, allow for at least 3-4GB of free space before running this app. 





