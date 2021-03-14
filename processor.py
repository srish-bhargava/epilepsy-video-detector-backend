from pytube import YouTube
import constants
import hashlib
import os
import cv2
from PIL import Image, ImageStat

def processVideo(url):
    filepath = downloadVideo(url)
    lums = analyseVideoLuminance(filepath)
    return None


def downloadVideo(url): 
    filename = getHash(url)
    filepath = constants.VIDEO_DIRECTORY + "/" + filename
    
    if os.path.exists(filepath + ".mp4"):
        return filepath + ".mp4"

    yt = YouTube(url)
    stream = yt.streams.first()
    stream.download(constants.VIDEO_DIRECTORY, filename)
    return filepath+".mp4"


def getHash(s):
    hash_object = hashlib.md5(s.encode())
    return hash_object.hexdigest()


def analyseVideoLuminance(filepath):
    lums = []
    cap = cv2.VideoCapture(filepath)
   
    while (cap.isOpened()):
        ret, frame = cap.read()

        if not ret:
            break

        im_pil = Image.fromarray(frame).convert('L')
        lum = ImageStat.Stat(im_pil).mean[0]
        lums.append(lum)

    cap.release()
    cv2.destroyAllWindows()

    return lums

