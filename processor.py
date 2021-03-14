from pytube import YouTube
import constants

def processVideo(url):
    downloadVideo(url)
    return None

def downloadVideo(url): 
    yt = YouTube(url)
    stream = yt.streams.first()
    stream.download(constants.VIDEO_DIRECTORY)

