import pandas as pd
from flask import request
from flask_restful import Resource
from models.validation import Person_model
from models.person import Person
from route.db_extension import db


class ReadFile(Resource):

    def post(self, **kwargs):
        params = request.get_json()
        people = []

        worksheet = pd.read_excel(params['file_path'])

        # Iterate over the rows of people and append each one to the dictionary of people
        for row_number, record in worksheet.iterrows():
            try:
                model = Person_model.parse_obj(record.dropna())
                people.append(model.dict())
            except Exception as e:
                print(e)

        print(f"All people: {people}")

        # Add all people to the database
        for person in people:
            db.session.add(person)
            db.session.commit()
