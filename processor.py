from pytube import YouTube
import constants
import hashlib
import os
import cv2
from PIL import Image, ImageStat
import numpy as np


def processVideo(url):
    filepath = downloadVideo(url)
    lums = analyseVideoLuminance(filepath)
    lums = postProcessLuminance(lums)
    anomalies = getAnomalies(lums)
    anomalies = postProcessAnomalies(anomalies)
    changes = getChanges(anomalies)
    changes = getChangesInVideoTime(changes, 60)
    return changes


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


def postProcessLuminance(lums):
    lums_grad = np.gradient(lums)
    lums_absgrad = abs(lums_grad)
    
    sliding_window_size = 60
    num_points = len(lums_absgrad)
    
    lums_absgrad_movingsum = []
    for i in range(num_points):
        moving_sum = sum(lums_absgrad[max(0, i - sliding_window_size) : i])
        lums_absgrad_movingsum.append(moving_sum)
    return lums_absgrad_movingsum


def getAnomalies(lums):
    pass


def postProcessAnomalies(anomalies):
    anomalies_bucketed = []
    sliding_window_size = 30
    num_points = len(anomalies)
    
    for i in range(num_points):
        bucket_val = any(anomalies[max(0, i - sliding_window_size) : i])
        anomalies_bucketed.append(bucket_val)
    return anomalies_bucketed


def getChanges(anomalies):
    changes = []
    prev = None
    for indx, val in enumerate(anomalies):
        if prev != val:
            changes.append([indx, val])
            prev = val
    return changes


def getChangesInVideoTime(changes, fps):
    timePerFrame = 1.0/fps
    return [[change[0]*timePerFrame, change[1]] for change in changes]
