import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

emailSender="asthas2018@gmail.com"
emailPassword= "google security code"
emailReceiver="user@gmail.com"
subject = "subject"
body= """
This is the body of the mail.

"""
msg = MIMEMultipart()
msg['From'] = emailSender
msg['To'] = emailReceiver
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))


try:
    #Gmail smtp server settings
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(emailSender, emailPassword)
    server.sendmail(emailSender, emailReceiver, msg.as_string())
    server.quit()
    
#if any error occurs this message will pop up
except Exception as e:
    print(f"Email to {emailReceiver} failed: {str(e)}")



 ####### ALTERNATIVE WAY TO SEND MAIL USING SMTP, SSL AND EM  #######

# import smtplib
# import ssl
# from email.message import EmailMessage  

# emailSender="asthas2018@gmail.com"
# emailPassword= "google security code"
# emailReceiver="user@gmail.com"
# subject = "subject"
# body= """
# This is the body of the mail.

# """

# em = EmailMessage()
# em['from']= emailSender
# em['to']= emailReceiver
# em['subject']= subject
# em.set_content(body)

# try:
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
#         smtp.login(emailSender,emailPassword)
#         smtp.sendmail(emailSender,emailReceiver, em.as_string())
#     return True

# except Exception as e:
#     print(f"Email to {emailReceiver} failed: {str(e)}")
#     return False