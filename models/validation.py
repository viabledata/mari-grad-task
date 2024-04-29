from datetime import datetime, date, time

from pydantic import BaseModel


class Person(BaseModel):
    id: int
    name: str
    dob: date
    time_in: time
    membership_no: int
    valid_from: date
    valid_to: date
    gender: str
    researcher: str

