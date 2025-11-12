#import modules
import singleEmailSender
import bulkEmailSender


#main
if __name__ == "__main__":
    print("Welcome to email sender")
    choice = int(input("Select your email send type\n 1.single email send \n 2.bulk eamil send"))
    subject = input("Enter subject of an email:")
    body = input("Enter body of an email:")

    if choice == 1:
        email = input("Enter email:")
        singleEmailSender.single_email_send(
            to_email=email,
            subject = subject,
            body = body
        )
    elif choice == 2:
        email = input("Enter emails separated by comma:").split(",")
        bulkEmailSender.bulk_email_send(
            email = email,
            subject = subject,
            body = body
            )
    else:
        print("select either 1 or 2")

        



        
