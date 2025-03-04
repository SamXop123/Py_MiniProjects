from pytube import YouTube

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
yt = YouTube(url)
yt.streams.get_highest_resolution().download()
print("Download Complete!")
