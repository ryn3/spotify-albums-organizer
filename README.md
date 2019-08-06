# Saved Spotify Albums Organizer

![GUI example](https://raw.githubusercontent.com/savoy1211/spotify-albums-organizer/master/display_example.png?token=AGCPCLNPJJ3XPM5ATHXQQHS5JHHPU)

This app lets you organize and visualize your saved Spotify albums. You can sort by genre, year, date added, etc.

Import your saved albums from Spotify and the monthly Discogs masters data -- ~1.5GB -- into MongoDB. Since Spotify data lacks information about genre and subgenres (styles), discogs-spotify-import retrieves genre and subgenre data from the Discogs library and updates the Spotify data. 

**This app hasn't been tested on Python 2.x**

Download MongoDB if needed from <https://www.mongodb.com/download-center/community>

## Specifications
The Mongo database uses localhost: 27017

* Database name: **discogs_masters** 

* Collections: **current_albums** (saved Spotify albums) **current_masters** (Discogs masters). 

## Dependencies

## Usage

### 1. Import album data

	$ chmod +x run.sh
	$ ./run.sh [spotify-id] [discogs-masters-xml-file]

* Find your Spotify id on your browser's tab when you go to <https://open.spotify.com/settings/account>
* Download the XML Discogs masters data into the local directory from <https://discogs-data.s3-us-west-2.amazonaws.com/data/2019/discogs_20190701_masters.xml.gz>. Importing others may be buggy. 

**This will take some time. On my 2015 MacBook Air, this step took ~1hr.**

### 2. Import album cover images
	
	$ cd scripts
	$ python import_images.py

### 3. Clean data

**There will likely be incomplete album data.** Consider cleaning your data for more accurate data (i.e release year, label, etc.):

#### Example: 
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

### 4. Display saved Spotify albums

#### Example:

	$ cd scripts
	$ python display_albums.py
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

## Note

Allow for around 5GB of free space before running this app. 
