import pandas as pd
from flask import request
from flask_restful import Resource

from models.validation import Person_model
from models.person import Person


class ReadFile(Resource):
    def post(self, **kwargs):
        params = request.get_json()
        people = []

        people_added = 0
        worksheet = pd.read_excel(params['file_path'])

        # TODO: I don't know if below commented code is needed
        '''
        columns = df.columns
        df = df.reset_index()
        df_dict = df.T.to_dict('list')
        print(df[1])
        ['Name', 'Date of birth', 'Time in', 'Membership', 'Valid from', 'Valid to', 'Librarian', 'Gender', 'Researcher']
        name = row[1], dob = row[2], time_in = row[3], membership_no = row[4], valid_from = row[5],
        valid_to = row[6], gender = row[7], researcher = row[8]
        '''

        for row_number, record in worksheet.iterrows():
            print(f"number: {row_number}")
            try:
                model = Person_model.parse_obj(record.dropna())
                people.append(model.dict())
            except Exception as e:
                print(e)

        print(f"All people: {people}")

        # TODO: now do the db insertions.
        # db.session.add(new_person)
        #     db.session.commit()
        #     people_added += 1
        # return f" {people_added} people added"
