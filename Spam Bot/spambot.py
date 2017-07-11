# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:09:40 2017

@author: Pranav yadav

Email Spammer
"""

#import the simple mail transfer protocol module
import smtplib

content = input("What would you like to send?  ")
fromadd = input("What is your email address (must be a gmail account)?  ")
password = input("What is your password?  ")
toadd = input("Who do you want to send the email to?  ")
amount = input("How manay times do you want to send the email?  ")
amount = int(amount) #convert string to integer

def sendspam(content, fromadd, password, toadd, amount):
    success = 0
    #connect to smtp server and port(465 or 587)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
        
    #identify yourself to the server
    mail.ehlo()
    
    #start tranport layer security mode
    mail.starttls()
        
    #login credentials
    mail.login(fromadd, password)
    
    #iterate through the number of emails you wish to send
    for i in range(amount):
        #send the email
        mail.sendmail(fromadd, toadd, content)
        
        success += 1
        print(success, " email(s) sent!")
        
    #close communication with the server    
    mail.close()
    
#call the function
sendspam(content, fromadd, password, toadd, amount)