from flask import Flask
app = Flask(__name__)
import processor


@app.route('/get_blocked_timestamps')
def getBlockedTimestamps():
    processor.processVideo()
    return 'Its working'