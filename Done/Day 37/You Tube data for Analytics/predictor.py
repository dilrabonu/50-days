import joblib
import numpy as np
from utils.embedding import get_title_embedding

classifier = joblib.load('models/youtube_rf_classifier.pkl')

DAY_MAP = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2, 
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6}

def _build_feature_vector(title, duration, hour, day):
    emb = get_title_embedding(title)
    features = np.concatenate([
        np.array([duration, hour, DAY_MAP[day]]), emb
    ])
    return features.reshape(1, -1)

def predict_view_count(title, duration, hour, day):
    X = _build_feature_vector(title, duration, hour, day)
    return classifier.predict(X)[0]

def predict_view_class(title, duration, hour, day):
    X = _build_feature_vector(title, duration, hour, day)
    probs = classifier.predict_proba(X)[0]
    classes = classifier.classes_
    class_index = np.argmax(probs)
    class_labels = ['low', 'medium', 'high']
    return class_labels[class_index], dict(zip(classes, probs))