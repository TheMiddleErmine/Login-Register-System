from argparse import _MutuallyExclusiveGroup
from ipaddress import ip_address
import ipaddress
import os
from os import system
from platform import machine
import pyfiglet, threading
from pyfiglet import *
import colorama
from colorama import Fore, Back, Style
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
import time
import webbrowser
import socket
import mysql.connector
import mysql
import pymysql
from config import *
import getpass
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox


system('cls')

def start_func():

    system('cls')
    host_name = socket.gethostname()    
    IPAddress = socket.gethostbyname(host_name)
    print(pyfiglet.figlet_format(communityname))
    print('This program is for authorized users of ' + communityname + ' and its subsiduaries. For security purposes your IP is being recorded: ' + IPAddress)
    print('\n1. Login\n2. Register')

    login_register_input = input('\n>> ')

    if login_register_input == '1':

        system('cls')
        print('NOTE: Password wont be shown while typing.')

        global username_login_entry 
        username_login_entry = input('\nUsername: ')  

        global password_login_entry
        password_login_entry = getpass.getpass('Password: ')
       
        system('cls')

        if username_login_entry=="" or password_login_entry=="":

            print('All fields are required, please try again. You will be re-directed shortly...')
            time.sleep(5)
            system('cls')
            start_func()
            
        else:
            system('cls')
            print('Processing, Please Wait...')
            db = mysql.connector.connect(host= machineip, user= dbusername, passwd= dbpassword, database= dbname)
            mycursor =  db.cursor()
            tuple1 = (username_login_entry,)
            username = ("SELECT username FROM user_register WHERE username =%s")
            mycursor.execute(username, tuple1)
            usernamecheck=mycursor.fetchone()

            if usernamecheck == None:
                system('cls')
                print('Username and password do not match you will be re-directed shortly...')
                time.sleep(5)
                start_func()

            else:
                password = ("SELECT password FROM user_register WHERE password =%s")
                tuple2 = (password_login_entry,)
                mycursor.execute(password, tuple2)
                passwordcheck =mycursor.fetchone()
                ipdb = ("SELECT registered_ip FROM user_register WHERE registered_ip =%s")
                record = (IPAddress,)
                mycursor.execute(ipdb, record)
                ipauth=mycursor.fetchone()
               
                if ipauth == None:
                    system('cls')
                    print('ERROR: Your current IP address ('+IPAddress+') does not match your IP registered at account creation.')
                    os.system('pause')

                if passwordcheck == None:
                    system('cls')
                    print('Username and password do not match you will be re-directed shortly...')
                    time.sleep(5)
                    start_func()
                else: 
                    system('cls')
                    tools_menu()
    if login_register_input == '2':

        system('cls')
        regkeyauth = input('Registration Key: ')
        if regkeyauth == registrationkey:

            system('cls')
            print('NOTE: Password wont be shown while typing.')

            global registered_email
            registered_email = input('\nEnter your email address: ')

            global registered_username
            registered_username = input('Create a username: ')

            global registered_password
            registered_password = getpass.getpass('Create a password: ')      

            confirmpass = getpass.getpass('Confirm Password:')   

            if confirmpass != registered_password:

                system('cls')
                print('Processing, please wait')
                time.sleep(2)
                system('cls')
                print('The paswords entered do not match. You will be redirected shortly.')
                time.sleep(5)
                start_func()
            host_name = socket.gethostname()     
            IPAddress = socket.gethostbyname(host_name)
            global registered_ip     
            registered_ip = IPAddress
            registration_func()

        else:

            print("Registration key is invalid, contact your system administrator. You will be re-directed shortly...")
            time.sleep(5)
            system('cls')
            start_func()

def ipauth():

    host_name = socket.gethostname()    
    IPAddress = socket.gethostbyname(host_name)
    db = mysql.connector.connect(host= machineip, user= dbusername, passwd= dbpassword, database= dbname)
    mycursor =  db.cursor()
    regip= ("SELECT registered_ip FROM user_register WHERE registered_ip =%s")
    query= (IPAddress,)
    mycursor.execute(regip, query)
    ipauthentication =mycursor.fetchone()

def registration_func():

    if registered_username==""or registered_password=="":

        print('All fields are required, please try again. You will be re-directed shortly...')
        time.sleep(5)
        system('cls')
        start_func()

    else:
        system('cls')
        print('Processing, Please Wait.')
        db = mysql.connector.connect(host= machineip, user= dbusername, passwd= dbpassword, database= dbname)
        mycursor =  db.cursor()
        record = (registered_username, registered_password, registered_email, registered_ip)
        query = ("INSERT INTO user_register (username, password, email, registered_ip) VALUES (%s, %s, %s, %s) ")
        mycursor.execute(query, record)
        db.commit()
        db.close()
        system('cls')
        print('Account successfully created! Accounts are usually activated immediately. In rare occasions they may take up to 5 minutes.\nYou will be redirected shortly...')
        time.sleep(8)
        system('cls')
        start_func()


def tools_menu():

    print(pyfiglet.figlet_format('Tools'))
    list = print('1. FTP Server\n2. Password Registry')
    userinput = input('>> ')

    if userinput == '1':
        ftp_func()

def ftp_func():

    print('Coming soon!')


start_func()
def login_func():

    if username_login_entry=="" or password_login_entry=="":

        print('All fields are required, please try again. You will be re-directed shortly...')
        time.sleep(5)
        system('cls')
        start_func()

    else:

        system('cls')
        print('Processing, Please Wait...')
        db = mysql.connector.connect(host= machineip, user= dbusername, passwd= dbpassword, database= dbname)
        mycursor =  db.cursor()
        tuple1 = (username_login_entry,)
        username = ("SELECT username FROM user_register WHERE username =%s")
        mycursor.execute(username, tuple1)
        usernamecheck=mycursor.fetchone()

        if usernamecheck == None:

            system('cls')
            print('Incorrect Username')

        else:

            password = ("SELECT password FROM user_register WHERE password =%s")
            tuple2 = (password_login_entry,)
            mycursor.execute(password, tuple2)
            passwordcheck =mycursor.fetchone()
            db.close()
            tools_menu()

def susacct():
    print(f'ACCOUNT SUSPENDED: Conatact your system administrator!')
