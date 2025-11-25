import joblib

class failure_detector:
    def __init__(self):
        
        self.classifier = joblib.load("models/rf_pipeline.pkl")
        
    def predict_failure(self, df):
        return self.classifier.predict(df)

    def predict_failure_proba(self, df):
        return self.classifier.predict_proba(df)[:, 1]
