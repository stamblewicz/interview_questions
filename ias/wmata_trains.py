# wmata_trains.py
'''
This script was created by Karolina as per the requested interview task for IAS
'''

import requests
import os

API_KEY = os.getenv('WMATA_API_KEY')
URL = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/C15"

def get_trains():
    headers = {
        'api_key': API_KEY
    }
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        trains = [train for train in data['Trains'] if train['Line'] == 'YL']
        return trains
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    trains = get_trains()
    for train in trains:
        print(f"Train to {train['DestinationName']} arriving in {train['Min']} minutes")

