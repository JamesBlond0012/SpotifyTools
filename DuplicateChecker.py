import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

scope = "playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='https://example.com/callback'))

playlists = sp.current_user_playlists()
playlist_ids = [playlist['id'] for playlist in playlists['items']]

def is_song_in_array(song_title, song_artist, track_array):
    for track in track_array:
        if track['name'] == song_title and track['artist'] == song_artist:
            return True
    return False

def get_all_playlist_tracks(sp, playlist_id):
    all_tracks = []
    offset = 0
    limit = 50
    while True:
        playlist_tracks = sp.playlist_tracks(playlist_id, offset=offset, limit=limit)
        all_tracks.extend(playlist_tracks['items'])
        if len(playlist_tracks['items']) < limit:
            break
        offset += limit
    return all_tracks

for playlist_id in playlist_ids:
    print("-" * 20)
    playlist_info = sp.playlist(playlist_id)
    print(playlist_info['name'])
    all_tracks = get_all_playlist_tracks(sp, playlist_id)
    print(len(all_tracks))
    playlist_tracks = sp.playlist_tracks(playlist_id)
    tracks_array = []
    all_tracks = get_all_playlist_tracks(sp, playlist_id)
    for track in all_tracks:
        track_info = track['track']
        if track_info:
            track_data = {
                'name': track_info['name'],
                'artist': track_info['artists'][0]['name'],
            }
            if is_song_in_array(track_data['name'], track_data['artist'], tracks_array):
                print(track_data)
            else:
                tracks_array.append(track_data)
    print("-" * 20)
