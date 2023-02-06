#!/bin/python3

from pytube import YouTube
import os

#ask user to put youtube video link
yt = YouTube(str(input("Enter URL of youtube video: \n ")))

# stream filter audio only
video = yt.streams.filter(only_audio=True).first()

#ask user where to save the file
print("Enter the destination address (leave blank to save in current directory)")
destination = str(input(" ")) or '.'

# download file
out_file = video.download(output_path=destination)
base, ext = os.path.splitext(out_file)

# rename the file
new_file = base + '.mp3'
os.rename(out_file, new_file)

# acknowledge when download complete
print(yt.title + " has been successfully downloaded.")