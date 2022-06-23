import json

import requests
import spotipy
from spotipy.oauth2 import SpotifyAuthBase, SpotifyOAuth
from bs4 import BeautifulSoup

Client_ID = "9c63bccbde504d5997382453ddf32ac2"
Client_Secret = "13d79910b6eb47018295b82652582012"
OAUTH_AUTHORIZE_URL = "https://www.google.com/"
date = input("Which year do you want to travel to? Type the date in this format YYY-MM-DD")
URL = "https://www.billboard.com/charts/the-billboard-hot-100/" + date + "/"
spotify_end = "https://api.spotify.com."
response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
songs = soup.find_all("h3", class_="a-no-trucate")
songs_list = []
for song in songs:
    song_title = song.getText().strip()
    songs_list.append(song_title)
login = SpotifyOAuth(client_id=Client_ID, client_secret=Client_Secret, redirect_uri=OAUTH_AUTHORIZE_URL,
                     scope="playlist-modify-private", username="My playlist", cache_path="token.txt", show_dialog=True)
sp = spotipy.Spotify(oauth_manager=login)
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f":{song}  genre:R&B", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=date, public=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)


