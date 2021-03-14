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
        timestamps.append(datetime.datetime.fromtimestamp(i).isoformat()+"Z")

    for timestamp, lum in zip(timestamps, lums):
        series.append(TimeSeriesPoint(timestamp=timestamp, value=lum))
    request = DetectRequest(series=series, granularity='secondly', max_anomaly_ratio=0.25, sensitivity=95)

    response = None
    try:
        response = client.detect_entire_series(request)
    # except AnomalyDetectorError as e:
    #     print('Error code: {}'.format(e.error.code), 'Error message: {}'.format(e.error.message))
    except Exception as e:
        print(e)    
    except BaseException as e:
        print (e)

    if response is None or not response.is_anomaly:
        print('No anomalies were detected in the time series.')
        return []

    return response.is_anomaly