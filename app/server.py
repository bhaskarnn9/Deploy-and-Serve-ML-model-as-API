from fastapi import FastAPI
import joblib
import numpy as np
import uvicorn

model = joblib.load('app/model.joblib')

class_names = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI()


@app.get('/')
def reed_root():
    return {'message': 'Iris model API'}


@app.post('/predict')
def predict(data: dict):
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'prediction_class': class_name}


# run the API with uvicorn, it will run on http://127.0.0.1:8000
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
    