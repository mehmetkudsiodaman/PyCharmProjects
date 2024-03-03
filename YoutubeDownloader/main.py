from pytube import YouTube


def download_video(download_link):
    youtube_object = YouTube(download_link)
    youtube_object = youtube_object.streams.get_by_resolution("720p").download(path)
    print(f"Download complete!")


path = "C:\\Users\\Kudsi\\Videos"
link = input("Enter the YouTube video URL: ")
# https://www.youtube.com/watch?v=rnEzNwaqgtU
download_video(link)
