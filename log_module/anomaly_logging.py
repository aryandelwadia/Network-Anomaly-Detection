import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists("c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/logs"):
    os.makedirs("c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/logs")

logging.basicConfig(filename="c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/logs/anomaly_detection.log", level=logging.INFO)


# logging/anomaly_logging.py
def log_anomaly(message):
    #print("Log anomaly code")
    print(f"Anomaly Detected: {message}")
    # You can add code here to write the log to a file or send alerts

def get_logs():
    with open("c:/Users/aryan/Desktop/New folder/network-anomaly-new-main/logs/anomaly_detection.log", "r") as file:
        logs = file.read()
    return logs
