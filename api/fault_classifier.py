from fastapi import APIRouter, HTTPException
import pandas as pd
from models import failure_detector, Sample

fault_classifier_router = APIRouter()
model = failure_detector()

@fault_classifier_router.post("/predict-failure")
def predict(sample:Sample):
    try:
        df = pd.DataFrame([sample.dict()]) 
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input format: {e}")

    try:
        flag = model.predict_failure(df)
        if not flag:
            status='Healthy'
            msg='Everything is Fine! 🎉!'
        else:
            status = 'Failed'
            msg='Call for Maintainence ⚠️!'
        propability_of_failure = (model.predict_failure_proba(df)[0])*100
        response = {
            "Status":f"{status}",
            "Probability of failure": f"{propability_of_failure}%",
            "msg":f"{msg}"
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
