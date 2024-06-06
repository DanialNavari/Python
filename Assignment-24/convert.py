import time
from threading import Thread
import requests
from pip import editor

# Threads list
threads = []

# List of videos
video_list = [
    "http://danielnv.ir/videos/1.mp4",
    "http://danielnv.ir/videos/2.mp4",
    "http://danielnv.ir/videos/3.mp4",
    "http://danielnv.ir/videos/4.mp4",
    "http://danielnv.ir/videos/5.mp4",
]


# List of audios
audio_list = []


# Download video from a url address and write into a file
def download(url, name):
    file = requests.get(url)
    f = open(f"{name}.mp4", "wb")
    f.write(file.content)
    f.close()


# This function convert video(mp4 format) to audio(mp3 format)
def VideoToAudio(i):
    vid = editor.VideoFileClip(f"videos/{i}.mp4")
    vid.audio.write_audiofile(f"audios/{i}.mp3")


# This function execute video to audio function whitout using threat and calculate duration seconds
def convert_without_threat():
    start_time = time.time()

    for i in range(1, 6):
        VideoToAudio(i, video_list[i])

    end_time = time.time()
    print(
        f"\n Duration whitout using Threat: {round(end_time - start_time,2)} seconds.\n"
    )


# This function execute video to audio function using threat and calculate duration seconds
def convert_with_threat():
    start_time = time.time()

    for i in range(1, 6):
        threads.append(Thread(target=VideoToAudio, args=[i]))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"\n Duration using Threat: {round(end_time - start_time,2)} seconds.\n")


for i in range(0, 5):
    download(video_list[i], i)


convert_without_threat()
convert_with_threat()
