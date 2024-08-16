import pywhatkit
phone_number ='+5555996595524'
message='teste'
hours= 23
minutes=00
pywhatkit.sendwhatmsg_instantly(phone_number,message,hours,minutes)
print('MSG OK')