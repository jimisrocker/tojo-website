import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Replace sender@example.com with your "From" address. 
# This address must be verified.
SENDER = 'tojo@tojoanalytics.com'  
SENDERNAME = 'Tojo Analytics'

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
RECIPIENT  = 'aposarga@gmail.com'

# Replace smtp_username with your Amazon SES SMTP user name.
USERNAME_SMTP = "AKIA2D7DHW2YQAIBJEEW"

# Replace smtp_password with your Amazon SES SMTP password.
PASSWORD_SMTP = "BDoPIp3zPUBqyVT8XkK+AcS71gr91ZEfPWMc2QzgP9dV"

# (Optional) the name of a configuration set to use for this message.
# If you comment out this line, you also need to remove or comment out
# the "X-SES-CONFIGURATION-SET:" header below.
#CONFIGURATION_SET = "ConfigSet"

# If you're using Amazon SES in an AWS Region other than US West (Oregon), 
# replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP  
# endpoint in the appropriate region.
HOST = "email-smtp.us-east-1.amazonaws.com"
PORT = 587



def reply_to_sender(recipient_email):
    # The subject line of the email.
    SUBJECT = 'Thank you for your interest!'

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("A representative of Tojo analytics will contact you shortly\r\n"
             "This email was sent because of your interest in our company"
             "tojoanalytics.com"
            )

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>Thank you for your interest in Tojo Analytics</h1>
    <p>A representative of Tojo analytics will contact you shortly.<br> 
    This email was sent because of your interest in our company
        <a href='tojoanalytics.com'>
        Tojo Analytics</a>.</p>
    </body>
    </html>
            """

# Create message container - the correct MIME type is multipart/alternative.


    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
    msg['To'] = recipient_email
# Comment or delete the next line if you are not using a configuration set
#msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

# Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(BODY_TEXT, 'plain')
    part2 = MIMEText(BODY_HTML, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

# Try to send the message.

    try:  
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        #stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
    # Display an error message if something goes wrong.
    except Exception as e:
        print ("Error: ", e)
    else:
        print ("Email sent!")


def notify_people(name, dudes_email,phone,message):
    # The subject line of the email.
    SUBJECT = 'Yo malakes some guy named '+name+' is interested in us' 

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("The guy is called "+name+" his email is "+dudes_email+
             "his phone if any is --> "+phone+"<-- and he says "+ message
            )

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>Name: """+ name + """</h1>
    <p>Email: """+ dudes_email+"""<br>His phone if any is: """+phone+"""<br>
    And he says:<br> """ + message + """</p>
    </body>
    </html>"""

# Create message container - the correct MIME type is multipart/alternative.
    to='tolis@tojoanalytics.com'
    cc="john@tojoanalytics.com, jimmy@tojoanalytics.com"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
    msg['To'] = to
    msg['Cc']=cc
# Comment or delete the next line if you are not using a configuration set
#msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

# Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(BODY_TEXT, 'plain')
    part2 = MIMEText(BODY_HTML, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

# Try to send the message.
    rcpt=cc.split(",") + [to]
    try:  
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        #stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, rcpt, msg.as_string())
        server.close()
    # Display an error message if something goes wrong.
    except Exception as e:
        print ("Error: ", e)
    else:
        print ("Email sent!")