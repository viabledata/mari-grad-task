from datetime import datetime, date, time
from typing import Optional
from pydantic import BaseModel, validator, Field


class Person_model(BaseModel):
    name: Optional[str] = None
    dob: Optional[date] = None
    time_in: Optional[time] = None
    membership_no: Optional[int] = None
    valid_from: Optional[date] = None
    valid_to: Optional[date] = None
    librarian: Optional[str] = None
    gender: Optional[str] = None
    researcher: Optional[str] = None

    @validator("dob")
    def check_valid_date(cls, input_date):
        if not isinstance(input_date, date):
            raise ValueError("Must be a valid date")
        # print(f"valdation dob: {input_date}")
        return input_date

    @validator("time_in")
    def check_valid_time(cls, input_time):
        if not isinstance(input_time, time):
            raise ValueError("Must be a valid time")
        # print(f"validation time_in: {input_time}")
        return input_time


class Config:
    title = "Person_model"
    # allow_population_by_field_name = True
    orm_mode = True
