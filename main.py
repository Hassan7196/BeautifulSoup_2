from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

ClIENT_ID = "your_id"
CLIENT_SECRET = "your_id"
REDRIECT_URI = "http://example.com"
scope_spotify = "playlist-modify-private"
USER_ID = "your_id"
year = "2016"
PLAYLIST_ID = "your_id"

# BILLBOARD
date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

headings = soup.select(selector="li ul li h3")
songs = []

for i in range(0, len(headings), 1):
    heading = headings[i].getText().replace("\n", "").replace("\t", "")
    songs.append(heading)

#  SPOTIFY
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=ClIENT_ID,
                              client_secret=CLIENT_SECRET,
                              redirect_uri=REDRIECT_URI,
                              scope=scope_spotify,
                              cache_path="token.txt",
                              show_dialog=True)
)

uri_songs = []
for song in songs:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result['tracks']['items'][0]['uri'])
        uri_songs.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print("OH HI ")

r = sp.user_playlist_add_tracks(user=USER_ID, playlist_id=PLAYLIST_ID, tracks=uri_songs)
print(r)
