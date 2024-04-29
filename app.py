import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy()
db.init_app(app)

from models.person import Person

with app.app_context():
    db.drop_all()
    db.create_all()


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!"


@app.route('/read', methods=['POST'])
def read_file():
    people_added = 0
    df = pd.read_excel(r"./Library_register_data (1).xlsx")
    columns = df.columns
    df = df.reset_index()
    df_dict = df.T.to_dict('list')
    #print(df[1])
    # ['Name', 'Date of birth', 'Time in', 'Membership', 'Valid from', 'Valid to', 'Librarian', 'Gender', 'Researcher']
    # name = row[1], dob = row[2], time_in = row[3], membership_no = row[4], valid_from = row[5],
    # valid_to = row[6], gender = row[7], researcher = row[8]

    for item in df_dict.items():
        row = item[1]
        new_person = Person(name=row[1], dob=row[2], time_in=row[3], membership_no=row[4], valid_from=row[5],
                            valid_to=row[6], gender=row[7], researcher=row[8])
        db.session.add(new_person)
        db.session.commit()
        people_added += 1
    return f" {people_added} people added"


@app.route('/check', methods=['GET'])
def check():
    person_query = Person.query.all()
    people = []
    for person in person_query:
        people.append(person)
    return people


if __name__ == '__main__':
    app.run()
