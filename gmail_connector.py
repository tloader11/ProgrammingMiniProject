"""
This is the gmail_connector module.

This module sends a mail message to the user
"""

# Imports
import smtplib


def SendMessage(to, text):

    # Vars
    gmail_user = "ns.404.notfound@gmail.com"
    gmail_pwd = "123456789AA"
    FROM = "NS 404"
    TO = to if type(to) is list else [to]
    SUBJECT = "Melding fietsenstalling"
    TEXT = text

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print("successfully sent the mail")
    except:
        print("failed to send mail")
