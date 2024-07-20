import os
import pandas as pd
from sklearn.pipeline import Pipeline
from typing import Union
from app.models.prediction import Input, Output


class PredictionModel:
    model: Union[Pipeline, None] = None
    predicted_results: Union[int, None] = None

    def load_model(self):
        """
        Load the model into memory
        """
        import joblib
        current_path = os.path.dirname(__file__)

        self.model = joblib.load(os.path.join(current_path, "rf_email_click_prediction.joblib"))

    def predict(self, input: Input) -> Output:
        """
        Predict the target variable
        """
        if self.model is None:
            self.load_model()

        if input is None:
            raise ValueError("Input is required")

        input_df = pd.DataFrame([input.dict()])

        self.predicted_results = self.model.predict(input_df)[0]

        return Output(predicted_results=self.predicted_results)
