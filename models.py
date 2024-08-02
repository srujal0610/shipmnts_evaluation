from extensions import db

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    schedule_time = db.Column(db.DateTime, nullable=False)
    recurrence = db.Column(db.Text, nullable=True)
    attachments = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'recipient': self.recipient,
            'subject': self.subject,
            'body': self.body,
            'schedule_time': self.schedule_time.isoformat(),
            'recurrence': self.recurrence,
            'attachments': self.attachments
        }


