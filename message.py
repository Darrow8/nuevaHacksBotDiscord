import sender
import smtplib
# import sheets3 as sheets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def runFormError(user,form):
    try:
        subject = "NuevaHacks III"
        body = """\
        <html>
          <body>
            <p>Hi,</p>  
            <p>You entered an incorrect form. for """+ form +"""</p>
            <p style="margin-bottom: 0em;">Yours,</p>
             <p style="margin-top: 0em;margin-bottom: 0em;"> Darrow</p>
            <p style="margin-top: 0em;">Head of Tech @ NuevaHacks</p>
          </body>
        </html>
        """
        msg = MIMEMultipart()
        msg['To'] = user
        msg['From'] = sender.mailFromAddress
        msg['Subject'] = subject
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'html'))
        message = msg.as_string()
        server = smtplib.SMTP(sender.mailFromGmail)
        server.starttls()
        server.login(sender.mailFromAddress,sender.password)

        server.sendmail(sender.mailFromAddress,user,message)
        server.quit()
    except:
        print("EXTREME ERROR")

def runTeamError(user):
    try:
        subject = "NuevaHacks III"
        body = """\
        <html>
          <body>
            <p>Hi,</p>  
            <p>There was an error when making your team. Please try again.</p>
            <p style="margin-bottom: 0em;">Yours,</p>
             <p style="margin-top: 0em;margin-bottom: 0em;"> Darrow</p>
            <p style="margin-top: 0em;">Head of Tech @ NuevaHacks</p>
          </body>
        </html>
        """
        msg = MIMEMultipart()
        msg['To'] = user
        msg['From'] = sender.mailFromAddress
        msg['Subject'] = subject
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'html'))
        message = msg.as_string()
        server = smtplib.SMTP(sender.mailFromGmail)
        server.starttls()
        server.login(sender.mailFromAddress,sender.password)

        server.sendmail(sender.mailFromAddress,user,message)
        server.quit()
    except:
        print("EXTREME ERROR")