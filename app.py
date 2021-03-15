from flask import Flask
import processor
import constants
from flask import request
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


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



if __name__ == "__main__":
    init()
    app.run(ssl_context='adhoc')
