from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from youtubesearchpython import VideosSearch
from pathlib import Path
import yt_dlp
import re

app = Flask(__name__, template_folder='../frontend/templates')  # Specify template folder location

# Load environment variables from .env file
load_dotenv()

# Spotify API setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URI"),
    scope=["playlist-read-private", "user-library-read"]
))

def search_youtube(query):
    videos_search = VideosSearch(query, limit=1)
    result = videos_search.result()
    return result['result'][0]['link']

def download_audio(youtube_url, output_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def get_music_folder_path():
    if os.name == 'nt':  # Windows
        return Path(os.path.expanduser('~/Music'))
    else:  # macOS/Linux
        return Path.home() / 'Music'

def extract_spotify_id(spotify_url):
    if "playlist" in spotify_url:
        match = re.search(r'playlist/([a-zA-Z0-9]+)', spotify_url)
        if match:
            return match.group(1), 'playlist'
    elif "track" in spotify_url:
        match = re.search(r'track/([a-zA-Z0-9]+)', spotify_url)
        if match:
            return match.group(1), 'track'
    
    raise ValueError("Invalid Spotify URL. Please provide a valid Spotify playlist or track URL.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    spotify_url = data.get('spotify_url')
    
    if not spotify_url:
        return jsonify({'error': 'Spotify URL is required.'})
    
    try:
        spotify_id, url_type = extract_spotify_id(spotify_url)
        if url_type == 'playlist':
            playlist = sp.playlist_tracks(spotify_id)
        elif url_type == 'track':
            playlist = {'items': [{'track': sp.track(spotify_id)}]}
    except ValueError as e:
        return jsonify({'error': str(e)})
    except Exception as e:
        return jsonify({'error': str(e)})

    output_dir = get_music_folder_path()

    for item in playlist['items']:
        track = item['track']
        song_name = track['name']
        artist_name = track['artists'][0]['name']
        query = f"{song_name} {artist_name} lyrics"
        youtube_url = search_youtube(query)
        download_audio(youtube_url, output_dir)
    
    return jsonify({'success': 'Download complete!'})

if __name__ == "__main__":
    app.run(debug=True)