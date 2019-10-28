import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Ammar Alim"
email["to"] = "ammar.osman.ali@gmail.com"
email["subject"] = "You have got a python email"


email.set_content("I am a python Master")


with smtplib.SMTP(host="smpt.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("ammar.osman.ali@gmail.com", "Iowa1985")
    smtp.send_message(email)
    print("it's all good boss")

