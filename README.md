## Steps to setup the API
1. Steps to setup the API
2. Firsty, install the packages using the following command: "pip install requirements.txt"
3. Start the server : python app.py
4. Schedule an email by making a POST request to the API by using curl as: 
>> >>     curl -X POST http://localhost:5000/schedule
>> >>     -email -H "Content-Type: application/json" -d '{ 
>> >>     "recipient": "sample-mail@example.com",
>> >>     "subject": "Test Subject",
>> >>     "body": "This is a test email.",
>> >>     "schedule_time": "2024-08-02T14:00:00",
>> >>     "recurrence": null,
>> >>     "attachments": []
>> >>     }

5. To get the list of the scheduled email:
>> >>     curl -X GET http://localhost:5000/scheduled-emails

6. To retrieve a Specific Scheduled Email
>> >>     curl -X GET http://localhost:5000/scheduled-emails/1



