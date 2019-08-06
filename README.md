# Saved Spotify Albums Organizer

Import your saved albums from Spotify and the monthly Discogs masters data -- ~1.5GB -- into MongoDB. 
You will have to download the XML Discogs masters data into the local directory. 
Since Spotify data lacks information about genre and subgenres (styles), discogs-spotify-import retrieves genre and subgenre data from the Discogs library and updates the Spotify data. FYI, there may be a few bugs with XML files other than discogs_20190701_masters.xml.

## Specifications
The Mongo database uses localhost: 27017
*Database name: **discogs_masters** and the 
*Collections: **current_albums** (saved Spotify albums) **current_masters** (Discogs masters). 

## 1. Import album data:
	$ chmod +x run.sh
	$ ./run.sh <spotify-id> <discogs-masters-xml-file>

(You can find your Spotify id on your browser's tab when you go to <https://open.spotify.com/settings/account>)

This will take some time depending on the number of saved Spotify albums. On my 2015 MacBook Air, importing Discogs data, ~600 saved albums, and cross-referencing genre and style data took roughly an hour. 

## 2. Import album cover images:
	
	$ cd scripts
	$ python import_images.py

## 3. Clean data: 

**There will likely be incomplete album data.** Consider cleaning your data for more accurate data (i.e release year, label, etc.):

### Example: 
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

## 4. Display saved Spotify albums

### Example:

	$ cd scripts
	$ python display_albums.py
	$ Input is case-sensitive!
	$ choose genre([Electronic], [Jazz], [Rock], [Classical], [Funk / Soul], [Hip Hop], all): Jazz
	$ choose sorting option([release_year], [name], [artists[0].name], [label], [genres], [added_at]): release_year
	$ choose direction([ascending], [descending]): descending
	$ Loading 194/219 albums...

In the GUI, click on an album cover to go to its Spotify page. You may customize the number of columns by changing "cols" in `display_albums.py` (line 93). 

## Updating saved albums

If you want to update your saved album data (after you've added or deleted any saved albums from the Spotify app), run these commands:
	
	$ chmod +x update_saved_albums.sh
	$ ./update_saved_albums.sh <spotify-id>

## Note

Allow for around 5GB of free space before running this app. 