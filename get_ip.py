import socket
import os

"""
This simple script fetches your IP as seen by web pages, and displays it.
Execute this script locally like that:
$ curl -s https://raw.github.com/gist/3389407/myip.py | python
"""
import requests
import urllib
import ezgmail
import html2text
import time

# use website http://ip.42.pl/raw for raw ip


def get_ip() -> str:
	original_ip = (urllib.request.urlopen('http://ip.42.pl/raw'))
	mybytes = original_ip.read()
	ORIGINAL_IP = mybytes.decode("utf8")
	original_ip.close
	return ORIGINAL_IP

def start():
	C_IP = get_ip()
	ezgmail.send('sharanshangar@gmail.com', 'IP Change', C_IP)
	print('Current IP: ', C_IP)
	print('start(y/n): ')
	start = input()
	while(start == 'y'):
		print("TRUE")
		ip = get_ip()
		print(ip)		
		if(ip != C_IP):
			ezgmail.send('sharanshangar@gmail.com', 'IP Change', ip)		
			print("Changed")
			C_IP = ip
		time.sleep(1800)
		
			

start()



