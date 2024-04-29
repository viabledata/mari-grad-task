from datetime import datetime, date, time

from pydantic import BaseModel, field_validator, Field


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

    @field_validator("dob", "valid_from", "valid_to")
    def check_valid_date(cls, input_date):
        if not isinstance(input_date, date):
            raise ValueError("Must be a valid date")
        return input_date

    @field_validator("time_in")
    def check_valid_time(cls, input_time):
        if not isinstance(input_time, time):
            raise ValueError("Must be a valid time")
        return input_time
