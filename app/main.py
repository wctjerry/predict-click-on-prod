from fastapi import FastAPI, Depends
from app.models.prediction import Output
from app.ml_models.email_click_prediction import PredictionModel


app = FastAPI()
model = PredictionModel()

@app.post("/predict")
def predict(output: Output = Depends(model.predict)):
    return output


@app.on_event("startup")
def startup():
    model.load_model()
