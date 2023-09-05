import smtplib,ssl

port = 465
context=ssl.create_default_context()

sender_email="noreply@trulloy.com"
receiver_email="allyamit@gmail.com"
message="""\
    Subject: hii there
    
    this is test messege

"""
with smtplib.SMTP_SSL("trulloy.com",port,context=context) as server:
    server.login("noreply@trulloy.com","trulloy@2012")
    server.sendmail(sender_email,receiver_email,message)

