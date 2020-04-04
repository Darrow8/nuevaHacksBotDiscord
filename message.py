import sender
import smtplib
import sheets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def runEmail():
    for user in sheets.usersWithoutDiscord:
        subject = "NuevaHacks III"
        body = """\
        <html>
          <body>
            <p>Hi """+ user.name +""",</p>
           <p> Thank you for signing up for NuevaHacks III. We’re so excited to have you participating, and can’t wait to see what you create!</p>
    
            <p>We’ll be using Discord for communication throughout the hackathon and need your username now so that we can start creating channels based on the interests you listed when you signed up. If you don’t have a discord, you can make one here: <a href="https://discordapp.com/">Discord Link</a>.</p>
    
            <p>Once you have created one, <b>please submit your username and discord tag on this form: <a href="https://forms.gle/JhRxtCmrFnfhtJNdA">Form<a>.</b> You can find your discord tag by navigating to "User Settings" and on the tab "My Account" you should see your tag next to your username. If you have any more questions, please email me back, I’m happy to help.</p>
    
            <p>Our team will be sending you more details including the schedule for the event in the coming days.</p>
    
            <p style="margin-bottom: 0em;">Yours,</p>
             <p style="margin-top: 0em;margin-bottom: 0em;"> Darrow</p>
            <p style="margin-top: 0em;">Head of Tech @ NuevaHacks</p>
          </body>
        </html>
        """
        msg = MIMEMultipart()
        msg['To'] = user.email
        msg['From'] = sender.mailFromAddress
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'html'))
        message = msg.as_string()
        server = smtplib.SMTP(sender.mailFromGmail)
        server.starttls()
        server.login(sender.mailFromAddress,sender.password)

        server.sendmail(sender.mailFromAddress,user.email,message)
        user.returnAll()
        server.quit()

runEmail()