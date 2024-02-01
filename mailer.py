import os
import dotenv
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()
password = os.getenv('EMAIL_PASS')


def MailCreds(name, receiver, log_pass):
    email_sender = 'nexsynchelpdesk@gmail.com'
    email_password = password
    link = "https://www.rockstargames.com/gta-v"

    email_receiver = receiver

    subject = "You are invited to NexSync"

    body = """Dear """ + name + """,\n\nWe would like to inform you that the HR Department of your company has signed up on the NexSync Platform.\nFrom now on, NexSync will be the platform used for project assignments, work-related notifications, discussions, and insights.""" + """\n\nYour Login Credentials:\n\nEmail: """ + receiver + """\nPassword: """ + log_pass + """\n\nDownload the NexSync app from this link:\n""" + link + """\n\nBest regards,\nNexSync Support"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        try:
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            return 1
        except Exception as e:
            return -1


def MailRep(project_name, receiver, file):


    email_sender = 'nexsynchelpdesk@gmail.com'
    email_password = password

    email_receiver = receiver

    subject = "Project Report"

    body = """Dear HR,\n\nHere is the report that you requested for the Project """+ project_name+""".\n\nBest regards,\nNexSync Support"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with open(file, 'rb') as f:
        file_data = f.read()

    em.add_attachment(file_data, maintype='application', subtype = 'octet-stream', filename=file)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        try:
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            return 1
        except Exception as e:
            return -1

def MailTaskComp(reporting_manager, emp_name, emp_id, receiver, task_details, skills, projects):
    email_sender = 'nexsynchelpdesk@gmail.com'
    email_password = password

    email_receiver = receiver

    subject = "Employee needs to be utilised!"

    body = """Dear """ + reporting_manager + """,\n\nAn Employee just finished a task assigned to them\n\nEmployee Name: """+emp_name+"""\nEmployee ID: """+emp_id+"""\nTask Finished: """+task_details+"""\nSkills: """+skills+"""\n\nUtilise them in ongoing projects:\n"""+projects+"""\n\nBest regards,\nNexSync Support"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        try:
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            return 1
        except Exception as e:
            return -1