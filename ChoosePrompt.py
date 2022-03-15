import numpy as np
import pandas as pd
import smtplib
import ssl
import datetime

emailU = 'deliveredemailprompts@gmail.com'
emailPass = 'DeliveredPrompts'
sendTo = ['johnsen.danny42@gmail.com', 'lizzy.johnsen@gmail.com']


for u in sendTo:
    file = pd.read_csv('https://raw.githubusercontent.com/johnsendanny/JournalProj/master/Questions.csv')
    choice = np.random.choice(file['Question'])
    split = str.split(choice,';')

    subject = 'Your Journal Prompt for ' + datetime.date.today().strftime("%m/%d/%Y")
    content = ''
    for x in split:
        content = content + x + '\n'

    print(content)
    subject.encode('utf-8')
    content.encode('utf-8')
    port = 465
    smtp_server_domain_name = "smtp.gmail.com"

    ssl_context = ssl.create_default_context()
    service = smtplib.SMTP_SSL(smtp_server_domain_name, port, context=ssl_context)
    service.login(emailU, emailPass)
    result = service.sendmail(emailU, u, f"Subject: {subject}\n{content}")
    service.quit()

