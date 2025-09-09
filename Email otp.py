import os
import math
import random
import smtplib
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
msg= OTP + " is your OTP"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls() # in(#)enter your details
s.login("Your email id", "Your app password security key")
emailid = input("Enter your email…")
s.sendmail("your email id", To-email, msg)
s.quit()
print("otp sent successfully")
otp=input("enter your otp")
if(otp==OTP):
    print("otp correct")


