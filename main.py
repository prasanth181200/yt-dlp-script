import yt_dlp
from functools import lru_cache

@lru_cache(maxsize=5)
def list_formats(url):
    ydl_opts = {
        'listformats': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        for f in formats:
            if f.get('ext') in ['mp4', 'mp3', 'webm'] and not f.get('vcodec') == 'none':
                print(f"ID: {f['format_id']}, Extension: {f['ext']}, Resolution: {f.get('resolution', 'N/A')}, Note: {f.get('format_note', 'N/A')}")

def download_video(url, format_id, output_path):
    ydl_opts = {
        'format': format_id,     # Specify the format ID
        'outtmpl': output_path,  # Specify the output path
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    url = input("Enter the YouTube video URL: ")
    print("Available formats:")
    list_formats(url)
    
    format_id = input("Enter the format ID to download: ")
    output_path = input("Enter the output file path (e.g., '/path/to/video.mp4'): ")
    download_video(url, format_id, output_path)
    print("Download completed!")

if __name__ == "__main__":
    main()
