from enum import Enum
from pydantic import BaseModel


class EmailText(str, Enum):
    long_email = "long_email"
    short_email = "short_email"


class EmailVersion(str, Enum):
    personalized = "personalized"
    generic = "generic"


class Weekday(str, Enum):
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"


class UserCountry(str, Enum):
    us = "US"
    uk = "UK"
    es = "ES"
    fr = "FR"


class Input(BaseModel):
    email_text: EmailText
    email_version: EmailVersion
    hour: int
    weekday: Weekday
    user_country: UserCountry
    user_past_purchases: int


class Output(BaseModel):
    predicted_results: int
