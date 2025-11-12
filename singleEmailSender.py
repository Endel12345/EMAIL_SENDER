import smtplib #SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#sender details
SENDER_EMAIL ="endeldeepshika@gamil.com"
PASSKEY ="odye fnuq juvd ppst"
SMTP_SERVER = "stmp.gmail.com"
SMTP_PORT = 587

#single email sender function def
def single_email_send(to_email :str ,subject :str, body :str):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = SENDER_EMAIL
    msg["Subject"] = subject
    msg .attach(MIMEText(body, 'plain'))

    #create server
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, PASSKEY)
        server.sendmail(SENDER_EMAIL,to_email , msg.as_string())
        server.quit()
        print(f"Succesfully email send to {to_email}")
    except Exception as e:
        print(f"sending mail is failed to {to_email}")
