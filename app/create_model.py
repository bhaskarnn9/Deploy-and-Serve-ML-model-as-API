import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# load Iris dataset
iris = load_iris()
x, y = iris.data, iris.target

# train Random Forest classifier
model= RandomForestClassifier()
model.fit(x, y)

# save the trained model
joblib.dump(model, 'model.joblib')
