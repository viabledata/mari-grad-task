from datetime import datetime, date, time
from typing import Optional
import pandas
from pydantic import BaseModel, validator, Field
from dateutil import parser
from pydantic.class_validators import Union


class Person_model(BaseModel):
    name: Optional[str]
    dob: Union[datetime, str]
    time_in: Optional[time]
    membership_no: Optional[int]
    valid_from: Union[datetime, str]
    valid_to: Union[datetime, str]
    librarian: Optional[str]
    gender: Optional[str]
    researcher: Optional[str]

    @validator('dob', 'valid_from', 'valid_to')
    def check_valid_date(cls, input_date):
        if isinstance(input_date, str):
            new_date = parser.parse(input_date)
            print(type(new_date))
            return new_date
        if isinstance(input_date, pandas.Timestamp):
            new_date = input_date.to_pydatetime()
            print(type(new_date))
            return new_date
        print(type(input_date))
        return input_date

    @validator('time_in')
    def check_valid_time(cls, input_time):
        if not isinstance(input_time, time):
            raise ValueError("Must be a valid time")
        return input_time


class Config:
    title = "Person_model"
    # allow_population_by_field_name = True
    orm_mode = True
