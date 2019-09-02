export SPOTIPY_CLIENT_ID='3285ca840c1c4f0fb053486d59687374'
export SPOTIPY_CLIENT_SECRET='c8b2f0d296f04f5895d402d8628bc374'
export SPOTIPY_REDIRECT_URI='https://verve3349.wordpress.com'
mkdir data
mkdir data/saved_albums
mkdir data/images
python3 user_saved_albums.py $1

echo "using discogs_masters database"
echo "using current_albums collection"

dir="data/saved_albums/"
for f in "$dir"/*; do
  mongoimport -d discogs_masters -c temp "$f"
done

mongo < aggregate_saved_albums.js

echo "Done with Spotify saved albums import."
