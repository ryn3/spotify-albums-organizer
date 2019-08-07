"""
    Retrieves saved Spotify albums as JSON. 

"""

import pprint
import sys
import json
import spotipy
import spotipy.util as util
import os.path

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    saved_albums = str(sp.current_user_saved_albums(limit=15))
    j = int(int(saved_albums[saved_albums.rfind(' ')+1:len(saved_albums)-1])/50)+1 #total saved albums
    jsone = json.JSONEncoder()
    for i in range(0,j):
	    results = sp.current_user_saved_albums(limit=50,offset=(50*i))
	    file_name = "album_data" + str(i) + ".json"
	    save_path = 'data/saved_albums/'
	    completeName = os.path.join(save_path, file_name)
	    with open(completeName, 'w') as f:
	        json.dump(results,f)
	    print(completeName+" was created successfully.")
else:
    print("Can't get token for", username)
