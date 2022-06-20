from typing import Any, List, Optional

from pydantic import BaseModel
from heartdisease_model.processing.validation import HeartDiseaseInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    preds: Optional[List[int]]
    probs: Optional[List[float]]


class MultipleHeartDiseaseInputs(BaseModel):
    inputs: List[HeartDiseaseInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        'Smoking': 'Yes',
                        'AlcoholDrinking': 'No',
                        'Stroke': 'No',
                        'DiffWalking': 'No',
                        'AgeCategory': '55 - 59',
                        'Race': 'White',
                        'Diabetic': 'Yes',
                        'PhysicalActivity': 'Yes',
                        'GenHealth': 'Very good',
                        'Asthma': 'Yes',
                        'KidneyDisease': 'No',
                        'SkinCancer': 'Yes',
                        'BMI': 'No',
                        'PhysicalHealth': 'Yes',
                        'MentalHealth': 'Yes',
                        'SleepTime': 'No',
                        'Sex': 'Yes',
                    }
                ]
            }
        }
