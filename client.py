import json
import requests

data = [[1.2, 4.5, 3.3, 2.7], [4.1, 1.9, 3.8, 2.4], [4.3, 1.6, 2.2, 3.5], [4.7, 1.4, 3.2, 4.9],
        [2.1, 3.6, 1.8, 2.5], [4.2, 1.7, 3.1, 2.6], [4.8, 1.3, 2.9, 3.7], [4.4, 1.5, 3.4, 2.8],
        [1.1, 3., 4.6, 2.3], [1., 3.9, 4., 2.]]

url = "http://0.0.0.0:8000/predict/"

predictions = []
for record in data:
    payload = {'features': record}
    payload = json.dumps(payload)
    response = requests.post(url, payload)
    predictions.append(response.json()['prediction_class'])

print(f'predictions: {predictions}')
