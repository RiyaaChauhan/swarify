# Swarify

Swarify is a Python-based application that allows users to download MP3 files from Spotify playlists or tracks by finding and extracting the audio from YouTube.


### Key Sections:
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Features
- Fetches tracks from Spotify playlists or individual track URLs.
- Searches for corresponding tracks on YouTube and downloads the audio in MP3 format.
- Downloads and saves the audio files to the system's Music folder by default or a custom directory.

## Requirements

- Python 3.x
- Spotipy (Spotify API)
- yt-dlp (YouTube downloader)
- FFmpeg (for audio extraction)
- youtube-search-python (for finding tracks on YouTube)

To install the packages listed in requirements.txt, run:

```bash
pip install -r requirements.txt
```
This command will install all the dependencies specified in the file into your virtual environment.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/swarify.git
cd swarify
```

2. **Set up the virtual environment:**

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up your Spotify API credentials:**
Create a .env file in the root directory of the project and add the following:

```bash
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=your_redirect_uri
```
You can obtain the CLIENT_ID and CLIENT_SECRET by registering an app in the Spotify Developer Dashboard.

5. **Install FFmpeg:**

FFmpeg installation instructions[https://ffmpeg.org/download.html]

## Usage
1. Run the application:
```bash
python swarify.py
```

2. Enter a Spotify playlist or track URL:

You will be prompted to provide a Spotify playlist or track URL.

3. Save location:

You can choose to save the downloaded MP3 files in a custom folder or the system's default Music folder.

## Example 

```bash
Enter the Spotify playlist or track URL: https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd?si=a1234567890
Found YouTube URL for Song 1: https://www.youtube.com/watch?v=example1
Downloaded Song 1 to C:\Users\YourName\Music
Found YouTube URL for Song 2: https://www.youtube.com/watch?v=example2
Downloaded Song 2 to C:\Users\YourName\Music
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

