import argparse
from utils.playlist_parser import get_playlist_info
from utils.downloader import download_playlist
from config.settings import DOWNLOAD_PATH
import os

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Download YouTube playlists from the command line.")
    parser.add_argument("playlist_url", help="URL of the YouTube playlist")
    parser.add_argument("--resolution", "-r", default="720p", help="Video resolution (e.g., 144p, 360p, 720p)")
    args = parser.parse_args()

    # Fetch playlist info
    print("Fetching playlist info...")
    videos, resolutions = get_playlist_info(args.playlist_url)
    
    if not videos:
        print("No videos found in the playlist or the playlist is private.")
        return
    
    # Display playlist info
    print(f"\nPlaylist contains {len(videos)} videos.")
    print(f"Available resolutions: {', '.join(resolutions)}")
    
    # Display video titles and resolutions
    print("\nVideos in the playlist:")
    for video in videos:
        print(f"- {video['title']} (Resolutions: {', '.join(video['resolutions'])})")
    
    # Confirm download
    confirm = input(f"\nDo you want to download the playlist in {args.resolution}? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Download canceled.")
        return
    
    # Download playlist
    print("\nStarting download...")
    download_playlist(args.playlist_url, args.resolution)
    
    # List downloaded files
    print("\nDownload complete. Files saved in the 'downloads' folder:")
    for file in os.listdir(DOWNLOAD_PATH):
        print(f"- {file}")

if __name__ == "__main__":
    main()