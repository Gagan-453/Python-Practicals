# Sending a simple mail
import smtplib # to send mail we need SMTP class of smtplib module
from email.mime.text import MIMEText

# Type the body text for our mail
body = '''<H1>Hi this is Gagan</H1>
<P>Your Flash chat registration code is <B>123456</B></P>'''

# Create MIMEText class object with body text
# msg is represented as an object of MIMEText class which belongs to email.mime.text
msg = MIMEText(body, 'html')

# from which address the mail is sent
fromaddr = "gaganreddy2705@gmail.com"

# to which address the mail is sent
toaddr = "gaganadithyareddy9@gmail.com"

# store the addresses into msg object
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Hi Advith'

# connect to gmail.com server using 587 port number
server = smtplib.SMTP('smtp.gmail.com', 587)

# put the smtp connection in TLS mode
server.starttls()

# login to the server with your correct password
server.login(fromaddr, "Password")

# send the message to the server
server.send_message(msg)
print('Mail sent...')

# close connection with server
server.quit()


# To avoid 'SMTPAuthenticationError', which means that gmail.com does not allow the program to communicate...login into your gmail account and visit  'https://www.google.com/settings/security/lesssecureapps' and turn on option against 'Access for less secure apps'
