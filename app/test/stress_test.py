import random
from locust import HttpUser, task, between
from app.models.prediction import EmailText, EmailVersion, Weekday, UserCountry


class ClickPredictUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def predict(self):
        body = {
            "email_text": random.choice(list(EmailText)).value,
            "email_version": random.choice(list(EmailVersion)).value,
            "hour": random.randint(0, 23),
            "weekday": random.choice(list(Weekday)).value,
            "user_country": random.choice(list(UserCountry)).value,
            "user_past_purchases": random.randint(0, 100),
        }

        self.client.post("/predict", json=body)
