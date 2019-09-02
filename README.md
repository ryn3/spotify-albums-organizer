# Spotify Albums Organizer

![GUI example](https://raw.githubusercontent.com/savoy1211/spotify-albums-organizer/master/display_covers.png)

This app lets you organize and visualize your saved Spotify albums. You can sort by genre, year, date added, etc.

Import your saved albums from Spotify and the monthly Discogs masters data -- ~1.5GB -- into MongoDB. Since Spotify data lacks information about genre and subgenres (styles), discogs-spotify-import retrieves genre and subgenre data from the Discogs library and updates the Spotify data. 

**This app only works on Python 3.7+ due to restriction on Tkinter**

Download MongoDB if needed from <https://www.mongodb.com/download-center/community>
If you're on Windows, make sure to download Xming <https://sourceforge.net/projects/xming/>
## Specifications
The Mongo database uses localhost: 27017

* Database name: **discogs_masters** 

* Collections: **current_albums** (saved Spotify albums) **current_masters** (Discogs masters). 

## Dependencies

	$ pip3 install -r REQUIREMENTS

## Usage

### 1. Import album data
	
	$ cd spotify-albums-organizer
	$ chmod +x run.sh
	$ ./run.sh [spotify-id] [discogs-masters-xml-file]

* Find your Spotify id on your browser's tab when you go to <https://open.spotify.com/settings/account>
* Download the XML Discogs masters data into the spotify-albums-organizer directory from <https://discogs-data.s3-us-west-2.amazonaws.com/data/2019/discogs_20190701_masters.xml.gz>. Importing others may be buggy. 

**This will take some time. On my 2015 MacBook Air, this step took ~1hr.**

### 1.5 Import album data

Additionally, search Discogs data using Discogs' Python client. This bypasses adding the masters data into Mongo.

	$ cd spotify-albums-organizer
	$ chmod +x run_quicker.sh
	$ ./run_quicker.sh [spotify-id]

Or, if saved Spotify albums already exist in Mongo:

	$ python3 get_genres.py

### 2. Import album cover images
	
	$ python3 import_images.py

### 3. Clean data

**There will likely be incomplete album data.** Consider cleaning your data for more accurate data (i.e release year, label, etc.):

#### Example: 

#### `clean_data.py` 

Cleans album data by updating parameters (label, release year, genres, styles).

	$ python3 clean_data.py
	$ Enter album name: Moondog
	$ Title: Moondog
	$ Artist: Moondog
	$ Label: Columbia Masterworks
	$ Year: 1969
	$ Genre(s): ['Jazz', 'Classical']
	$ Style(s): ['Big Band', 'Contemporary']
	$ Select parameter to update ([label], [release_year], [genres], [styles], exit): label
	$ label: CBS

#### `show_empty_genre_albums.py` 

Prints albums (album title and artist) with empty genre data.

	$ python3 show_empty_genre_albums.py
	1. title: Mr Finish Line
	   artist: Vulfpeck
	2. title: COGNITIO
	   artist: Yokaze
	3. title: Rhapsody In White (Reissue)
	   artist: The Love Unlimited Orchestra

#### `discogs_search_update.py` 

Update album data by searching with Discogs Python client.

	$ python3 discogs_search_update.py
	enter album to search in Discogs: Rhapsody In White
	Here is the current data: 
	label: Mercury Records
	year: 1998
	genres: []
	styles: []

	Is this the correct data [y/n]? n
	artist: Love Unlimited Orchestra
	label: 20th Century Records
	year: 1974
	genres: ['Jazz', 'Funk / Soul']
	styles: ['Soul-Jazz', 'Jazz-Funk', 'Soul', 'Disco']
	Is this the correct data [y/n]? y

### 4. Display saved Spotify albums

#### Example:

#### `display_albums.py`

Displays saved Spotify albums in a GUI. Click on an album cover to open album's Spotify page. The search buttons allow you to query the artist name and album title in the Discogs or RateYourMusic search bars.
	$ export DISPLAY=:0;
	$ python3 display_albums.py
	$ Input is case-sensitive!
	$ choose genre([Electronic], [Jazz], [Rock], [Classical], [Funk / Soul], [Hip Hop], all): Jazz
	$ choose sorting option([release_year], [name], [artists[0].name], [label], [genres], [added_at]): release_year
	$ choose direction([ascending], [descending]): descending
	$ Loading 194/219 albums...

In the GUI, click on an album cover to go to its Spotify page. You may customize the number of columns by changing "cols" in `display_albums.py` (line 93). 

### Updating saved albums

If you want to update your saved album data (after you've added or deleted any saved albums from the Spotify app), run these commands:
	
	$ chmod +x update_saved_albums.sh
	$ ./update_saved_albums.sh [spotify-id]


