import requests

COIN_EMAIL = 'coin.project.serch.engine@gmail.com'

import smtplib

from email.mime.text import MIMEText


def sendEmail(to, content):
    msg = MIMEText("We are searching for result for your search: " + content + "\n"
                   + "An email with our algorithm's results will be send to your email address : " + to + " soon.")
    msg['Subject'] = "Search request submitted"
    msg['From'] = "coin.project@sandboxcf29099671c7490eb8f0475d59ba01a7.mailgun.org"
    msg['To'] = to

    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login('postmaster@sandboxcf29099671c7490eb8f0475d59ba01a7.mailgun.org',
            '06622845eb4a6500758ff47bf996cf19-060550c6-e56db87b')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
