import os
import sys
import time
import json
import urllib2
import base64
from termcolor import colored, cprint
from base64 import *
red = "\33[31;1m"
green = "\33[32;1m"
yellow = "\33[33;1m"
white = "\33[37;1m"
def main_write(a):
        for b in a + '\n':
                sys.stdout.write(b)
                sys.stdout.flush()
                time.sleep(2./100)
def main_packages():
        os.system("pkg install python2 -y && pkg install python -y && pkg install git -y && pkg install nano -y && pkg install curl")
def main_requirements():
        file_requirements = open("requirements.txt", "w")
        code_requirements = "termcolor\ncolored\ncprint\n"
        file_requirements.write(code_requirements)
        file_requirements.close
def main_data():
        os.system("mkdir data")
        file_credits = open("data/credits.txt", "w")
        code_credits = "Author : ItzHex08\nContact : +62 8997-1679-090\nScript Version : 1.0.0\n"
        file_credits.write(code_credits)
        file_credits.close()
def main_log():
        os.system("mkdir log")
        file_log = open("log/log.txt", "a")
        code_log = (datetime.now() + timedelta(hours=9)).strftime('[%H:%M:%S]')+" Installing Packages ...\nInstalling File requirements.txt ...\nInstalling Folder data ...\nInstalling Folder log ...\n"
        file_log.write(code_log)
        file_log.close()
def main_start():
        file_start = open("start.py", "w")
        code_start = ""
        file_start.write(code_start)
        file_start.close()
def main_script():
        time.sleep(1)
        main_write(yellow+"Installing "+green+"Packages "+yellow+"...")
        time.sleep(5)
        print("")
        main_packages()
        print("")
        main_write(green+"Packages "+yellow+"Installed ...")
        print("")
        main_write(yellow+"Installing File "+green+"requirements.txt "+yellow+"...")
        time.sleep(5)
        print("")
        main_requirements()
        main_write(green+"requirements.txt "+yellow+"Installed ...")
        print("")
        main_write(yellow+"Installing Folder "+green+"data "+yellow+"...")
        time.sleep(5)
        print("")
        main_data()
        main_write(green+"data "+yellow+"Installed ...")
        print("")
        main_write(yellow+"Installing Folder "+green+"log "+yellow+"...")
        time.sleep(5)
        print("")
        main_log()
        main_write(green+"log "+yellow+"Installed ...")
        print("")
        main_write(yellow+"Installing File "+green+"start.py "+yellow+"...")
        time.sleep(5)
        print("")
        main_start()
        main_write(green+"start.py "+yellow+"Installed ...")
        print("")
        main_write(yellow+"Please Write ")
main_script()