# YouTube Playlist Downloader (CLI)

A command-line tool to download YouTube playlists. It allows you to specify the resolution and displays the progress of each download.

---

## Features
- **Fetch Playlist Info**: Displays the number of videos and available resolutions.
- **Download Videos**: Downloads all videos in the playlist at the specified resolution.
- **Progress Display**: Shows the current video being downloaded and the total number of videos.
- **Error Handling**: Skips private or unavailable videos.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/youtube-playlist-downloader-cli.git
   cd youtube-playlist-downloader-cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the script with the playlist URL and optional resolution:

```bash
python main.py "https://www.youtube.com/playlist?list=PLA62TgI_OxFw6smuWiroI9CEXpS5CAsYe" --resolution 720p
```

### Arguments
- `playlist_url`: The URL of the YouTube playlist.
- `--resolution` or `-r`: The desired video resolution (default: `720p`).

---

## Example Output

```plaintext
Fetching playlist info...

Playlist contains 15 videos.
Available resolutions: 144p, 360p, 720p, 1080p

Videos in the playlist:
- FNAF INTO THE PIT SONG "Drop Into the Pit" (Lyrics) (Resolutions: 144p, 360p, 720p, 1080p)
- FNAF Security Breach Song “Get Away (Remix)” (Resolutions: 144p, 360p, 720p, 1080p)
- THE MANDELA CATALOGUE SONG "That Me Is Not Me" (Resolutions: 144p, 360p, 720p, 1080p)
...

Do you want to download the playlist in 720p? (y/n): y

Starting download...

Downloading video 1 of 15: downloads/FNAF INTO THE PIT SONG "Drop Into the Pit" (Lyrics).mp4
Downloading video 2 of 15: downloads/FNAF Security Breach Song “Get Away (Remix)”.mp4
Downloading video 3 of 15: downloads/THE MANDELA CATALOGUE SONG "That Me Is Not Me".mp4
...

Download complete. Files saved in the 'downloads' folder:
- FNAF INTO THE PIT SONG "Drop Into the Pit" (Lyrics).mp4
- FNAF Security Breach Song “Get Away (Remix)”.mp4
- THE MANDELA CATALOGUE SONG "That Me Is Not Me".mp4
...
```

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
