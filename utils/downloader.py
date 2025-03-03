from yt_dlp import YoutubeDL
import os
from config.settings import DOWNLOAD_PATH

def download_playlist(playlist_url, resolution):
    ydl_opts = {
        'format': f'best[height<={resolution}]',  # Download a single file with both video and audio
        'outtmpl': os.path.join(DOWNLOAD_PATH, '%(title)s.%(ext)s'),
        'quiet': True,
        'ignoreerrors': True,  # Skip private/unavailable videos
        'progress_hooks': [progress_hook],  # Add progress hook
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        # Fetch playlist info to get the total number of videos
        info = ydl.extract_info(playlist_url, download=False)
        total_videos = len(info['entries']) if 'entries' in info else 0
        
        # Start download
        ydl.download([playlist_url])

def progress_hook(d):
    """
    Progress hook to display download progress.
    """
    if d['status'] == 'downloading':
        # Extract the current video number and total videos from the filename
        filename = d['filename']
        video_number = int(d['info_dict'].get('playlist_index', 0))
        total_videos = int(d['info_dict'].get('n_entries', 0))
        
        # Display progress
        if video_number and total_videos:
            print(f"Downloading video {video_number} of {total_videos}: {filename}")