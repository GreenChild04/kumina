from time import time
from pytube import YouTube, Playlist
from concurrent.futures import ThreadPoolExecutor, as_completed

playlist_link = input("playlist>")
video_links = Playlist(playlist_link).video_urls
start = time()


def get_video_title(link):
    title = YouTube(link).title
    return title

processes = []
with ThreadPoolExecutor(max_workers=10) as executor:
    for url in video_links:
        processes.append(executor.submit(get_video_title, url))

video_titles = []
for task in as_completed(processes):
    video_titles.append(task.result())
with open("titles.txt", "a+") as file:
        for i in video_titles:
           file.write(i + "\n")

print(f'Time taken: {time() - start}')