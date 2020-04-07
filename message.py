import sender
import smtplib
import sheets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def runEmail():
    for user in sheets.oldUsers:
        subject = "NuevaHacks III"
        body = """\
        <html>
          <body>
            <p>Hi,</p>
           <p> Thank you for signing up for NuevaHacks III. We’re so excited to have you participating, and can’t wait to see what you create!</p>

           <p>Unfortunately, you filled out an outdated (pre-coronavirus) form.</p>
           <p>Since transfering to an online hackathon, we would like you to fill out this <a href="https://forms.gle/4MXYTfQ5ptW54wSK6">form</a> to participate in our event next week.</p>

           <p>Our team will be sending you more details including the schedule for the event in the coming days. For any questions, feel free to reach out!</p>

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
        msg.attach(MIMEText(body,'html'))
        message = msg.as_string()
        server = smtplib.SMTP(sender.mailFromGmail)
        server.starttls()
        server.login(sender.mailFromAddress,sender.password)

        server.sendmail(sender.mailFromAddress,user,message)
        print(user)
        server.quit()

runEmail()