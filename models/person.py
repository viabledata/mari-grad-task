from route.db_extension import db
from sqlalchemy import Column, String, DateTime, Integer


class Person(db.Model):
    __tablename__ = 'people'
    id = Column("id", Integer, primary_key=True)
    name = Column("Name", String, nullable=False)
    dob = Column("Date of birth", DateTime, nullable=True)
    time_in = Column("Time in", DateTime, nullable=True)
    membership_no = Column("Membership number", String, nullable=True)
    valid_from = Column("Valid from", DateTime, nullable=True)
    valid_to = Column("Valid to", DateTime, nullable=True)
    gender = Column("Gender", String, nullable=True)
    researcher = Column("Researcher", String, nullable=True)
