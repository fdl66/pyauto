import smtplib
import string
 
HOST = "smtp.163.com"
SUBJECT = "Test email from Python"
TO = "1213886356@qq.com"
FROM = "fan0816fan@163.com"
text = "Python rules them all!"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("fan0816fan@163.com","******")
server.sendmail(FROM, [TO], BODY)
server.quit()
