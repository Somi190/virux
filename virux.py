#!/usr/bin/python
import os
import sys
import time
from time import sleep as out
import subprocess
def bersih():
    os.system("clear")
def kembali():
    ye = input("TRY AGAIN ? (y/t): ")
    if ye == "y":
       subprocess.call("python virux.py",shell=True)
    elif ye == "t":
         print ("STAR BOY")
         time.sleep(1)
         os.system("exit")
    else:
         print ("No Input!!")
         time.sleep(1)
         kembali()
def main(s):
  for c in s + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(1./12)

subprocess.call("VIRUS",shell=True)
banner = """

 \033[1;92m /    /~\  |\  /| | B 
 \033[1;91m/    /   \ | \/ | | R
\033[1;93m/____ \   / | /\ | | A
  \033[1;94m  /  \ /  |/  \| | N
 \033[1;95m  /   / \  |    | | D
\033[1;96m  /   /   \ |    | | BOY
"""
print (banner)
print ("\x1b[1;97m[\x1b[1;96m01\x1b[1;97m].\x1b[1;92mVIRUS ARAB")
time.sleep(0.2)
print ("\x1b[1;97m[\x1b[1;96m02\x1b[1;97m].\x1b[1;93mVIRUS BANAMAX")
time.sleep(0.2)
print ("\x1b[1;97m[\x1b[1;96m03\x1b[1;97m].\x1b[1;94mVIRPEN")
time.sleep(0.2)
print ("\x1b[1;97m[\x1b[1;96m04\x1b[1;97m].\x1b[1;95mVIRUS WOLF")
time.sleep(0.2)
print ("\x1b[1;97m[\x1b[1;96m05\x1b[1;97m].\x1b[1;96mVIRUS IDN")
time.sleep(0.2)
print ("\x1b[1;97m[\x1b[1;96m06\x1b[1;97m].\x1b[1;93mVIRUS ATTACKER ALONE")
time.sleep(0.2)
print ("\x1b[1;97m[\x1b[1;96m07\x1b[1;97m].\x1b[1;92mDOWNLOAD ALL VIRTEX")
time.sleep(0.2)
print ("\x1b[1;97m[\x1b[1;96m00\x1b[1;97m].\x1b[1;97mCLOSE PROGRAM")
time.sleep(0.2)
print ("\033[1;97m")
thex = input(">>>> ")
if thex == "01" or thex == "1":
    print ("Loading...")
    subprocess.call("cat virab.txt",shell=True)
elif thex == "02" or thex == "2":
      print ("Loading...")
      time.sleep(1)
      subprocess.call("cat banamex.txt",shell=True)
      kembali()
elif thex == "03" or thex == "3":
      print ("Loading...")
      time.sleep(1)
      subprocess.call("cat virpen.txt",shell=True)
      kembali()
elif thex == "04" or thex == "4":
      print ("Loading")
      main("..................")
      time.sleep(1)
      subprocess.call("cat wolf.txt",shell=True)
      kembali()
elif thex == "05" or thex == "5":
      print ("Loading...")
      main("..................")
      time.sleep(1)
      subprocess.call("cat idn.txt",shell=True)
      kembali()
elif thex == "06" or thex == "6":
      print ("Loading")
      main("...................")
      time.sleep(1)
      subprocess.call("cat alone.txt",shell=True)
      kembali()
elif thex == "07" or thex == "7":
      print ("Loading")
      main("...................")
      time.sleep(1)
      subprocess.call("unzip virus.zip",shell=True)
      time.sleep(2)
      print ("[\x1b[1;92mSUCCES\x1b[1;97m] DOWNLOADING COMPLETE..")
      time.sleep(1)
      print ("file stored in folder ")
      time.sleep(1)
      print ("TYPE cp -f -r filename or folder / sdcard to move the virtex ")
      time.sleep(2)
      kembali()
elif thex == "00" or thex == "0":
      print ("Close")
      time.sleep(0.3)
      os.system("exit")
else:
      print ("ENTER ")
      time.sleep(1)
      budek = input("CHECK BACK WHAT IS THE DIFFERENCE? (y/t): ")
      if budek == "y":
         subprocess.call("python virusx.py",shell=True)
      elif budek == "t":
           subprocess.call("exit",shell=True)
      else:
           print ("WRONG TYPE")
           subprocess.call("python virusx.py",shell=True)
      
 
