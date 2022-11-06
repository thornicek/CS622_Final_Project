from __future__ import unicode_literals
import youtube_dl
from main import links

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=9hJ8lLNWrM4'])

def download_videos(list):
    ydl_opts = {}
    for i in range(len(links)):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([i])

