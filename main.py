import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "{Your Email}"
receiver_email = "{Receiver Email}"
password = "{Youe email password}"
port = 587  #Server Port
smtp_server = "smtp.office365.com" #Host

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# message["Bcc"] = receiver_email  # Recommended for mass emails

message.attach(MIMEText(body, "plain"))

filename = "{Path of the file that you wish to attach}"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

print("Message Sent!")