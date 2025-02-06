from pytube import Playlist

def list_playlist_video_urls(playlist_url):
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        print(video_url)

# Example usage
playlist_url = 'https://www.youtube.com/playlist?list=PLZ2ps__7DhBbim4oKfdSdOpLyUwNd8UQL'
list_playlist_video_urls(playlist_url)

