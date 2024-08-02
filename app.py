from flask import Flask, jsonify, request 
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models import Email
from extensions import db, mail
from config import Config
import json


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
mail.init_app(app)

 
@app.route('/schedule-email', methods=['POST'])
def schedule_email():
    data = request.get_json()
    message = "The post request is accepting the schedules"
    email = Email(
        recipient=data['recipient'],
        subject=data['subject'],
        body=data['body'],
        schedule_time=datetime.fromisoformat(data['schedule_time']),
        attachments=json.dumps(data.get('attachments'))
    )
    db.session.add(email)
    db.session.commit()

    return jsonify({'id': email.id, 'message': 'Email scheduled successfully'}), 201
    # return jsonify({'mesage': message})


@app.route('/schedule-emails', methods=['GET'])
def get_scheduled_emails():
    emails = Email.query.all()
    return jsonify([email.to_dict() for email in emails])


@app.route('/schedule-emails/<int:id>', methods=['GET'])
def get_scheduled_email(id):
    email = Email.query.get_or_404(id)
    return jsonify(email.to_dict())


if __name__ == '__main__': 
  
    app.run(debug = True) 