export SPOTIPY_CLIENT_ID='f3ff300198254e889a1ed55921b136d3'
export SPOTIPY_CLIENT_SECRET='5507e5e4e3614febbdf166785cc446c3'
export SPOTIPY_REDIRECT_URI='https://open.spotify.com/user/'$1

python scripts/user_saved_albums.py $1

echo "using discogs_masters database"
echo "using current_albums collection"

dir="data/saved_albums/"
for f in "$dir"/*; do
  mongoimport -d discogs_masters -c temp "$f"
done

mongo < scripts/aggregate_saved_albums.js

echo "Done with Spotify saved albums import."