import smtplib
import ssl
import random
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.config import dbPerfENERGIE


def sendResetPasswordCode(email_receiver):
    try :
        email_sender = "noreply.visionstrategie@gmail.com"
        email_password = "auxgmidsvcdaulfg"
        email_receiver = email_receiver

        subject = "Demande de réinitialisation de votre mot de passe"

        code = generateCode()

        resetPasswordBody = f"""\
            <html>
              <head></head>
              <body>
                <p>Un code de vérification vous a été fourni afin de réinitialiser le mot de passe de votre compte Performance du RSE.</p>
                <p>Si vous n'avez pas fait cette demande, vous pouvez ignorer ce courriel.</p>
                <p><b>Votre code est : {code}.</b> Ce code va expirer dans 30 minutes.</p>
                <p>Ne répondez pas à ce message. Si vous avez des questions, écrivez-nous à aide-perf-rse@visionstrategie.com .</p>
              </body>
            </html>
            """

        message = MIMEMultipart('alternative')
        message["From"] = email_sender
        message["To"] = email_receiver
        message["Subject"] = subject
        message.attach(MIMEText(resetPasswordBody, 'html'))

        context = ssl.create_default_context()

        ############# mise à jour du code dans la BBD #######

        userCollection = dbPerfRSE["users"]

        query = {"email": email_receiver}
        dt = datetime.now() + timedelta(minutes=30)
        expiration_time = dt.strftime("%Y-%m-%d %H:%M:%S")
        newvalues = {"$set": {"token_code": f"{code}","expiration_time":expiration_time}}
        userCollection.update_one(query, newvalues)

        #### Envoi du code par mail #########################
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, message.as_string())

        return {"result":True,"code":code}

    except :
        return  {"result":False}


def generateCode():
    code1 = random.randint(0,9)
    code2 = random.randint(0, 9)
    code3 = random.randint(0, 9)
    code4 = random.randint(0, 9)
    code4 = random.randint(0, 9)
    code5 = random.randint(0, 9)
    code6 = random.randint(0, 9)

    code = f"{code1}{code2}{code3}{code4}{code5}{code6}"

    return code
