# import joblib
from joblib import load

# sample tweet text
text = ["hello, I hate"]

# load the saved pipleine model
pipeline = load("text_classification.joblib")

# predict on the sample tweet text
print(pipeline.predict(text))
