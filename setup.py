import time 
import config
import os
from os import system
from platform import machine
import pyfiglet, threading
from pyfiglet import *
import colorama
from colorama import Fore, Back, Style
import socket
import mysql
import mysql.connector
import pymysql
import getpass


print(pyfiglet.figlet_format('Setup'))
print('\nThis file will set-up your KeepSafe and configure all files inside. Follow directions exactly...')
system('cls')
print(pyfiglet.figlet_format('Database Connections'))
machineip = input('Enter your machine IP: ')
dbusername = input('Enter your database username: ')
print('NOTE: Your password will not be shown while typing.')
dbpassword = getpass.getpass('Enter your database password: ')
dbname = input('Enter the name of your database (Defaulted to KeepSafe): ')
#misc
system('cls')
print('Processing, please wait...')
time.sleep(5)
system('cls')
print(pyfiglet.figlet_format('Misc.'))
communityname = input('Enter the name of your community: ')
registrationkey = input('Set your registration key: ')

system('cls')
print('Verifing database information')

db = mysql.connector.connect(host= machineip, user= dbusername, passwd= dbpassword, database= dbname)
mycursor =  db.cursor()
record = (registrationkey, dbusername, dbpassword,dbname,communityname)
query = ("INSERT INTO config (reg_key, dbusername, dbpassword, dbname, communityname) VALUES (%s, %s, %s, %s, %s) ")
mycursor.execute(query, record)
db.commit()
db.close()
system('cls')
print('Submitting data to the database... \n(This may take awhile)')
time.sleep(10)
fp = open('config.py', 'w')
fp.write('machineip = "'+machineip+'"')
fp.write('dbusername = "'+dbusername+'"')
fp.write('dbpassword = "'+dbpassword+'"')
fp.write('dbname = "'+dbname+'"')
fp.close()