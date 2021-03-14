from pytube import YouTube
import constants
import hashlib
import os

def processVideo(url):
    downloadVideo(url)
    return None

def downloadVideo(url): 
    filename = getHash(url)
    filepath = constants.VIDEO_DIRECTORY + "/" + filename
    
    if os.path.exists(filepath + ".mp4"):
        return filepath

    yt = YouTube(url)
    stream = yt.streams.first()
    stream.download(constants.VIDEO_DIRECTORY, filename)
    return filepath

def getHash(s):
    hash_object = hashlib.md5(s.encode())
    return hash_object.hexdigest()