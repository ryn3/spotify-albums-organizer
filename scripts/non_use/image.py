mongoexport --host 27017 --db discogs_masters --collection current_albums_recent_2019 ---type=csv --out text.csv --fields addDate,artist,title,label,genre,style,url,image
