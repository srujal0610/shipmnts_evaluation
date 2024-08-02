from celery import Celery
from flask_mail import Message
from extensions import mail, db
from app import app, make_celery
from models import Email

celery = make_celery(app)

@celery.task
def send_email_task(email_id):
    with app.app_context():
        email = Email.query.get(email_id)
        if email:
            msg = Message(
                subject=email.subject,
                recipients=[email.recipient],
                body=email.body
            )
            mail.send(msg)
            db.session.delete(email)
            db.session.commit()
