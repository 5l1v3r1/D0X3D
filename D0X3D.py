#!/usr/bin/python
#----------------------------------------------------------------------------------------------------------
#This is a Python tool made by D04k3r D3v1l                                                               \  
#It takes user-submitted personal details and saves them to a .txt file                                   \
#It can be useful for saving the details of your target quickly after you have finished doxing him..      \
#--------------------------------------------------------------------------------------------------------\

print """                                                                          
_______                                         ..-'''-.    _______       
\  ___ `'.                                      \.-'''\ \   \  ___ `'.    
 ' |--.\  \                                            | |   ' |--.\  \   
 | |    \  '     .-''` ''-.                         __/ /    | |    \  '  
 | |     |  '  .'          '.  ____     _____      |_  '.    | |     |  ' 
 | |     |  | /              ``.   \  .'    /         `.  \  | |     |  | 
 | |     ' .''                ' `.  `'    .'            \ '. | |     ' .' 
 | |___.' /' |         .-.    |   '.    .'               , | | |___.' /'  
/_______.'/  .        |   |   .   .'     `.              | |/_______.'/   
\_______|/    .       '._.'  /  .'  .'`.   `.           / ,'\_______|/    
               '._         .' .'   /    `.   `. -....--'  /               
                  '-....-'`  '----'       '----'`.. __..-'                
"""
import os
import time
from datetime import datetime

print "Personal details saver by D04k3r D3v1l"
print "This is a simple details saver tool made in Python"
print "Your details will be saved in personal_details.txt" 
print "Now lets enter all the juicy info you have found"

name = raw_input("First and last name: ")
email = raw_input("Email: ")
phone = raw_input("Phone number: ")
address = raw_input("Address: ")
username = raw_input("Username(s): ")
ip = raw_input("IP address: ")
isp = raw_input("ISP: ")
password = raw_input("Password(s): ")

text_file = open("personal_details.txt", "w")
text_file.write("Name: %s\n" % name)
text_file.write("Email: %s\n" % email)
text_file.write("Phone: %s\n" % phone)
text_file.write("Address: %s\n" % address)
text_file.write("Username(s): %s\n" % username)
text_file.write("IP address: %s\n" % ip)
text_file.write("ISP: %s\n" % isp)
text_file.write("Password(s): %s" % password) 
text_file.close()

date = datetime.now()

print "The details you submitted have been saved in personal_details.txt on %s" % date
print "Thank you for using my program!"
print "The program will close automatically in 10 seconds"

time.sleep(10)
