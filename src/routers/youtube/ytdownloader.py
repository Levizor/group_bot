import os
import yt_dlp
from pathlib import Path
import asyncio


class YTDownloadException(Exception):
    """Custom exception to unify all YouTube download-related errors."""
    def __init__(self, message, original_exception=None):
        super().__init__(f"{message}\nOriginal Exception: {original_exception}")
        self.original_exception = original_exception


class DownloadedVideo:
    """Represents a downloaded YouTube video."""
    def __init__(self, path: Path):
        self._path = path

    def get_path(self) -> Path:
        """Returns the path to the downloaded video."""
        return self._path

    def delete(self):
        """Deletes the downloaded video file."""
        try:
            os.remove(self._path)
        except Exception as e:
            raise YTDownloadException("Failed to delete the video file.", e)


class YTDownloader:
    """Handles downloading YouTube videos using yt-dlp asynchronously."""
    
    # Static variable for the default download directory

    def __init__(self, output_dir: str = "downloads"):
        """Initialize the downloader. Use the static download_dir by default, or custom directory."""
        self.output_dir = Path(output_dir) 
        self.output_dir.mkdir(parents=True, exist_ok=True)

    async def download(self, video_url: str, format: str = 'best') -> DownloadedVideo:
        """Asynchronously downloads the YouTube video and returns a DownloadedVideo object."""

        ydl_opts = {
            'cookiefile': 'cookies.txt',
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),  # Save video with title as filename
            'format': format,  # Use the format provided (default is a balanced 720p video)
            'max_filesize': 50*1024*1024,
        }
        try:

            # Try to download using the provided format
            video_path = await asyncio.to_thread(self._download_video, video_url, ydl_opts)
            return DownloadedVideo(video_path)
            
        except yt_dlp.utils.DownloadError as e:
            # If the requested format is not available, fallback to the best format
            print(f"Requested format '{format}' is not available. Falling back to best format.")
            
            # Fallback format to best available video
            ydl_opts['format'] = 'best'
            
            # Try again with the best format
            video_path = await asyncio.to_thread(self._download_video, video_url, ydl_opts)
            return DownloadedVideo(video_path)

        except Exception as e:
            raise YTDownloadException("Failed to download the YouTube video using yt-dlp.", e)


    def _download_video(self, video_url: str, ydl_opts: dict) -> Path:
        """This method is used to run the blocking yt-dlp code in a separate thread."""
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            # Get the downloaded file path
            return Path(ydl.prepare_filename(info_dict))
