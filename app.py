from flask import Flask
app = Flask(__name__)
import processor
import constants
from flask import request
import os


def init():
    if not os.path.isdir(constants.VIDEO_DIRECTORY):
        os.mkdir(constants.VIDEO_DIRECTORY)


@app.route('/get_blocked_timestamps', methods=['POST'])
def getBlockedTimestamps():
    youtubeUrl = request.args.get('url')
    result = processor.processVideo(youtubeUrl)
    return {
        "result": result
    }


init()