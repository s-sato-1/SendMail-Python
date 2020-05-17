# -*- coding: utf-8 -*-

# ====================================================

import smtplib
import configparser
from email.mime.text import MIMEText

# ====================================================

def Send(t, f, s, pw):
    """
    """
    message = "Body" # Message
    msg = MIMEText(message, "html")
    msg["Subject"] = "Subject"
    msg["To"] = t
    msg["From"] = f

    server = smtplib.SMTP(s, 587)
    server.starttls() # Tls
    server.login(f, pw) # Login
    server.send_message(msg) # Send
    server.quit() # Close

# ====================================================

if __name__=='__main__':
    """
    """
    inifile = configparser.ConfigParser()
    inifile.read("Mail.ini","utf-8")

    t_email = str(inifile["Mail"]["To-Email"])
    f_email = str(inifile["Mail"]["From-Email"])
    smtp = str(inifile["Mail"]["Smtp-Server"])
    pw = str(inifile["Mail"]["Password"])

    Send(t_email, f_email, smtp, pw)

