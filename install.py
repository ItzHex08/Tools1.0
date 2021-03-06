import os
import sys
import time
import json
import urllib2
import base64
from termcolor import colored, cprint
from base64 import *
from datetime import datetime, timedelta
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
        code_log_1 = (datetime.now() + timedelta()).strftime('[%H:%M:%S]')+" Installing Packages ...\n"
        time.sleep(1)
        file_log.write(code_log_1)
        code_log_2 = (datetime.now() + timedelta()).strftime('[%H:%M:%S]')+" Installing File requirements.txt ...\n"
        time.sleep(1)
        file_log.write(code_log_2)
        code_log_3 = (datetime.now() + timedelta()).strftime('[%H:%M:%S]')+" Installing Folder data ...\n"
        time.sleep(1)
        file_log.write(code_log_3)
        code_log_4 = (datetime.now() + timedelta()).strftime('[%H:%M:%S]')+" Installing Folder log ...\n"
        time.sleep(1)
        file_log.write(code_log_4)
        file_log.close()
def main_start():
        file_start = open("start.py", "w")
        code_start = "import os\nimport sys\nimport time\nimport json\import utllib2\nimport base64\nfrom datetime import datetime, timedelta\nfrom termcolor import colored, cprint\nfrom base64 import *"
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