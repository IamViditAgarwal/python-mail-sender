"""
This code works for sending E-mail from G-Mail account.
Read the README.md file carefully before executing this code.
"""
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)
server.connect('smtp.gmail.com', 587) , # Gmail SMTP port for TLS connections
server.ehlo()
server.starttls() # Gmail only accepts connections over SSL or TLS
server.ehlo()
server.login('<GMAIL COMPLETE EMAIL ADDRESS>', '<PASSWORD>')

msg = MIMEMultipart()
msg['From'] = '<GMAIL COMPLETE EMAIL ADDRESS>'
msg['To'] = 'pythonmail@spaml.de' # Put the destination e-mail address. it can be gmail, yahoo or anyother
msg['Subject'] = 'Python script mail'

msg.attach(MIMEText('It, Works !!!', 'plain'))

image = '../img/code.jpg' # Sending the iamge as an attachment to destination e-mail
attachment = open(image, 'rb')

img_msg = MIMEBase('application', 'octet-stream')
img_msg.set_payload(attachment.read())

encoders.encode_base64(img_msg)
img_msg.add_header('Content-Disposition', f'attachment; filename={image}')
msg.attach(img_msg)


text = msg.as_string()
server.sendmail('<GMAIL COMPLETE EMAIL ADDRESS>', 'pythonmail@spaml.de', text)
server.quit()
