from flask import Flask
app = Flask(__name__)
import processor
from flask import request


@app.route('/get_blocked_timestamps', methods=['POST'])
def getBlockedTimestamps():
    youtubeUrl = request.args.get('url')
    processor.processVideo(youtubeUrl)
    return 'Its working'