# Download a YouTube Playlist Using Python

from pytube import Playlist

playlist_url = input('Enter Playlist: ')
playlist = Playlist(playlist_url)

for video in playlist.videos:
    video.streams.get_highest_resolutions().download()