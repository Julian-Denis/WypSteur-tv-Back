from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
load_dotenv()

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    subject = f"FIX10 : {data['itemToRepair']}"
    body = f"Name : {data['name']} \nEmail : {data['email']} \nBien à réparer: {data['itemToRepair']}\nDétails du problème : \n{data['problemDetails']}"

    msg = Message(subject, sender=data['email'], recipients=['WypSteur.tv@gmail.com'])
    msg.body = body
    mail.send(msg)

    return jsonify({"message": "Email sent"}), 200


if __name__ == '__main__':
    app.run(debug=True)
