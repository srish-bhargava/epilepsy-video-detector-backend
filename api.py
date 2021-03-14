import os
import datetime
from azure.ai.anomalydetector import AnomalyDetectorClient
from azure.ai.anomalydetector.models import DetectRequest, TimeSeriesPoint, TimeGranularity, AnomalyDetectorError
from azure.core.credentials import AzureKeyCredential
import pandas as pd


SUBSCRIPTION_KEY = os.environ["ANOMALY_DETECTOR_KEY"]
ANOMALY_DETECTOR_ENDPOINT = os.environ["ANOMALY_DETECTOR_ENDPOINT"]

client = AnomalyDetectorClient(AzureKeyCredential(SUBSCRIPTION_KEY), ANOMALY_DETECTOR_ENDPOINT)

def getAnomalies(lums):
    series = []
    timestamps = []
    for i in range(1,len(lums)+1):
        timestamps.append(datetime.datetime.fromtimestamp(i).isoformat()+",")

    for timestamp, lum in zip(timestamps, lums):
        series.append(TimeSeriesPoint(timestamp=timestamp, value=lum))
    request = DetectRequest(series=series, granularity=TimeGranularity.secondly)
    print('Detecting anomalies in the entire time series.')

    try:
        response = client.detect_entire_series(request)
    except AnomalyDetectorError as e:
        print('Error code: {}'.format(e.error.code), 'Error message: {}'.format(e.error.message))
    except Exception as e:
        print(e)

    if any(response.is_anomaly):
        print('An anomaly was detected at index:')
        for i, value in enumerate(response.is_anomaly):
            if value:
                print(i)
    else:
        print('No anomalies were detected in the time series.')
        pass


def preprocessAnomalyDetectorJson():
    pass