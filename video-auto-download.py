from pytube import YouTube
import time
import sys
import os
sys.path.append(os.path.abspath("SO_site-packages"))
import pyperclip

recent_value = ""
print('Estou pronto, pode começar a copiar os links!')
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        print("Link Copiado: %s" % str(recent_value))
        yt = YouTube(recent_value)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('videos')
        print(yt.title," | Video baixado com sucesso!")
    time.sleep(1)
