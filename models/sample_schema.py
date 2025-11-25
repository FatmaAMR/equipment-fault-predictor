from pydantic import BaseModel

class Sample(BaseModel):
    temperature: float
    pressure: float
    vibration: float
    humidity: float
    equipment: str