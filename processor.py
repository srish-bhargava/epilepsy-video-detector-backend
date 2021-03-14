from pytube import YouTube

def processVideo(url):
    downloadVideo(url)
    return None

def downloadVideo(url):
    SAVE_PATH = "./" 
    yt = YouTube(url)
    stream = yt.streams.first()
    stream.download(SAVE_PATH)

