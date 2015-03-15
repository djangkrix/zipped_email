import tempfile
from os import getcwd,pardir
from os.path import join,abspath
from shutil import make_archive,rmtree
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import Encoders

def send_zipped_email():
	gmail_user = "your.email@gmail.com"
  	gmail_pwd = "emailpassword123"
  	FROM = 'your.email@gmail.com'
  	TO = 'your.friend@gmail.com'
  	SUBJECT = 'This is Email with zip attachment'
  	TEXT = "This email can create zip file from multiple file"
  	tmpdir=tempfile.mkdtemp() #create temporary direktory
  	try:
    	tmparcv=join(tmpdir,'logs')
    	root_dir= abspath(join(getcwd(),pardir,pardir,'tmp','logs'))
    	data=open(make_archive(tmparcv,'zip',root_dir),'rb').read() #create zip and read file
    	msg = MIMEMultipart()
    	msg['From']=FROM
    	msg['To']=TO
    	msg['Subject']=SUBJECT
    	msg.attach(MIMEText(TEXT))
    	part = MIMEBase('application', 'zip')
    	part.set_payload(data)
    	Encoders.encode_base64(part)
    	part.add_header('Content-Disposition', 'attachment', filename='logs.zip') #files compressed to file zip named 'logs.zip'
    	msg.attach(part)
    	try:
      		server = smtplib.SMTP("smtp.gmail.com", 587)
      		server.ehlo()
      		server.starttls()
      		server.login(gmail_user, gmail_pwd)
      		server.sendmail(FROM, TO, msg.as_string())
      		server.close()
      		print 'successfully sent the mail'
      	except:
      		print "failed to send mail"
  	finally:
    	rmtree(tmpdir) #remove zip file from directory

if __name__ == '__main__':
  	send_zipped_email()
