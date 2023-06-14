# import smtplib

# # Password='vqve jjha gzyw gkqs'

# email = 'uma08cse49@gmail.com' # Your email
# # password = 'vqvejjhagzywgkqs' # Your email account password
# password='ubrnpmzrhfhgtjak'
# send_to_email = 'uma@sandeza-inc.com' # Who you are sending the message to
# message = 'This is a test message for email notification' # The message in the email

# server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
# server.starttls() # Use TLS
# server.login(email, password) # Login to the email server
# server.sendmail(email, send_to_email , message) # Send the email
# server.quit() # Logout of the email server


# =========================================================================================================

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart


# def send_email(sender_email, sender_password, receiver_email, subject, message):
#     # Set up the SMTP server
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587

#     # Create a multipart message
#     msg = MIMEMultipart()
#     msg['From'] = 'no-reply@gmail.com'
#     msg['To'] = receiver_email
#     msg['Subject'] = subject

#     # Add the message body
#     msg.attach(MIMEText(message, 'plain'))

#     try:
#         # Create a secure connection with the SMTP server
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()

#         # Log in to the sender's email account
#         server.login(sender_email, sender_password)

#         # Send the email
#         server.send_message(msg)
#         print('Email sent successfully!')

#     except Exception as e:
#         print('An error occurred while sending the email:', str(e))

#     finally:
#         # Close the SMTP server connection
#         server.quit()

# # Example usage
# sender_email = 'uma08cse49@gmail.com'
# # sender_password = 'ubrnpmzrhfhgtjak'
# sender_password = 'uwcbjnejptgupbvo'
# receiver_email = 'uma@sandeza-inc.com'
# subject = 'Test Email'
# message = 'This is a test email sent from a no-reply address.'

# send_email(sender_email, sender_password, receiver_email, subject, message)


# ==================================================================================================================


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "uma08cse49@gmail.com"
receiver_email = "uma@sandeza-inc.com"
# password = input("Type your password and press enter:")
password="uwcbjnejptgupbvo"

message = MIMEMultipart("alternative")
message["Subject"] = "alert message"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Dear Subscription owner,
We have observed some changes on the alert/NSG rule for the subscription that you own. In order to meet the approved NSG rules, the below changes are made"""
html = """\
<html>
  <body>
    <p>Dear Subscription owner,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )



