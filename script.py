import yt_dlp
import os


def download_playlist(url, downloadFolder):
    # Configure download directory
    DOWNLOAD_DIR = os.path.join(os.getcwd(), str(downloadFolder))
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    config = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [
            {   # Convert to MP3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {   # Embed metadata
                'key': 'FFmpegMetadata'
            },
            {   # Embed thumbnail
                'key': 'EmbedThumbnail'
            }
        ],
        'writethumbnail': True,
        'ignoreerrors': True,
        'quiet': False
    }

    with yt_dlp.YoutubeDL(config) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    print("YouTube Playlists to MP3 Downloader")
    url = input("Enter the playlist URL: ")
    downloadFolder = input("Enter the folder name: ")
    download_playlist(url, downloadFolder)
    print("\nDownload complete!")