import time

from pytube import YouTube
from pytube.contrib.search import Search

def on_complete(stream, file_path):
    print(stream)
    print(file_path)


def on_progress(stream, chunk, bytes_remaining):
    print(100 - (bytes_remaining / stream.filesize * 100))


link = input('Enter the link of video :\t')
video_object = YouTube(link, on_complete_callback= on_complete, on_progress_callback= on_progress)
video_object.streams.get_highest_resolution().download(output_path='C:/Users/HP/Downloads')



