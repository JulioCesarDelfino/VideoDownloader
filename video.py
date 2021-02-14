from pytube import YouTube
import time
link = input("Link do Video:")
yt = YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('videos')
print(yt.title," | Video baixado com sucesso!")
time.sleep(1)
