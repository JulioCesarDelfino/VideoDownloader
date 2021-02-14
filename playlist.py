from pytube import Playlist
from pytube import YouTube
import time
link = input("Link de um video da Playlist:")
p = Playlist(link)
print(f'Baixando: {p.title}')
for video in p.videos:
    for url in p.video_urls:
        yt = YouTube(url)
        print('Baixando: ', yt.title)
        yt.streams.first().download('videos')
    break
print(p.title," | Playlist baixada com sucesso!")
time.sleep(1)
