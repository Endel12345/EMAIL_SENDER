import singleEmailSender

#bulk email sender
def bulk_email_sender(emails: list[str] , subject: str, body: str):
    for email in emails:
        singleEmailSender.single_email_send(
            to_email=email,
            subject = subject,
            body = body
        )