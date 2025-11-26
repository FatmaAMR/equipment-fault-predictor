from fastapi import FastAPI

from api import base_router, fault_classifier_router

app = FastAPI(title="Failure classifier")
app.include_router(base_router)
app.include_router(fault_classifier_router)