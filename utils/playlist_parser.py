from yt_dlp import YoutubeDL
import logging

logging.basicConfig(level=logging.DEBUG)

def get_playlist_info(playlist_url):
    ydl_opts = {
        'extract_flat': True,  # Extract playlist metadata without downloading
        'quiet': True,         # Suppress output
        'ignoreerrors': True,  # Skip errors for individual videos
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            # Fetch playlist metadata
            info = ydl.extract_info(playlist_url, download=False)
            logging.debug(f"Playlist Info: {info}")
        except Exception as e:
            logging.error(f"Error fetching playlist: {str(e)}")
            raise Exception(f"Failed to fetch playlist: {str(e)}")
        
        videos = []
        resolutions = set()
        
        if 'entries' in info:
            for entry in info['entries']:
                if entry and entry.get('availability') != 'private':
                    video_title = entry.get('title', 'Untitled')
                    video_url = entry.get('url')
                    
                    # Fetch available resolutions for the video
                    video_resolutions = get_video_resolutions(video_url)
                    resolutions.update(video_resolutions)
                    
                    videos.append({
                        'title': video_title,
                        'resolutions': video_resolutions,
                        'url': video_url,
                    })
        
        logging.debug(f"Videos: {videos}")
        logging.debug(f"Resolutions: {resolutions}")
        return videos, sorted(resolutions, key=lambda x: int(x[:-1]), reverse=True)

def get_video_resolutions(video_url):
    """
    Fetch available resolutions for a single video.
    """
    ydl_opts = {
        'quiet': True,
        'ignoreerrors': True,
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video_url, download=False)
            formats = info.get('formats', [])
            resolutions = set()
            
            for fmt in formats:
                if fmt.get('height'):
                    resolutions.add(f"{fmt['height']}p")
            
            return sorted(resolutions, key=lambda x: int(x[:-1]), reverse=True)
        except Exception as e:
            logging.error(f"Error fetching resolutions for {video_url}: {str(e)}")
            return []