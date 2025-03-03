import os

# Default download path
DOWNLOAD_PATH = os.path.join(os.getcwd(), "downloads")

# Create downloads folder if it doesn't exist
os.makedirs(DOWNLOAD_PATH, exist_ok=True)