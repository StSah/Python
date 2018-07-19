from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib #sets up a server

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('sah.swati93@gmail.com','swati1234!!@@')

def sendmail(row,hashed_password):
    fromaddr='swati.sah93@gmail.com'
    toaddr=row[3]
    msg=MIMEMultipart()
    msg['From']=fromaddr
    msg['To']= toaddr 
    msg['Subject']="Forget Password"
    body= "To change your password  click on the link" + 'http://127.0.0.1:4999/updatepassword?uname='+row[2]+'&password='+hashed_password
    msg.attach(MIMEText(body, 'plain'))
    text=msg.as_string()
    server.sendmail(fromaddr,toaddr,text)
