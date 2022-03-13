import re

myEmail = "menna@gmail.com"


def send_mail(to, subject, msg, receiver_name):
    global myEmail
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if isinstance(to, str) and isinstance(subject, str) and isinstance(msg, str) and isinstance(receiver_name, str) :
        if not re.fullmatch(regex, to):
            raise Exception("email is not valid")
        with open(f"{subject}to{to}.txt", 'w') as email:
            message = f"From: {myEmail}\n" \
                      f"To: {to}\n" \
                      f"Subject: {subject}\n" \
                      f"" \
                      f"Hi,{receiver_name}\n" \
                      f"{msg}\n" \
                      f"Thanks"
            email.write(message)


send_mail("to@g.com", "subject", "msfsdfsfs\nrsfsfsfsefsef ffe", "receiver_name")
