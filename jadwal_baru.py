#!/usr/bin/python3

import subprocess
import time
import os
def check_date():
 skarang = time.ctime().replace(":", " ").split()
 date_file = "jadwal/date"
 hasil = False
 if not os.access(date_file, os.W_OK):
  open(date_file, "w+")
 with open(date_file, "r") as baca:
  baca = baca.read().split()
 with open("jadwal/what", "r+") as bacaa:
  bacaa = int(bacaa.read())
  if baca[2] != skarang[2]:
   with open(date_file, "w+") as nulis1:
     nulis1.write(str(time.ctime()).replace(":", " "))
   bacaa+=1
   print("different day, showing message %s %s" %(baca[2], skarang[2]))
   if bacaa >= 7:
     bacaa = 0
     hasil = True
  with open("jadwal/what", "w+") as nulis:
    nulis.write(str(bacaa))
 return hasil
def main():
 jadwal = ["C++", "Python"]
 with open("jadwal/what0", "r+") as baca:
  baca = baca.read()
 if check_date():
  with open("jadwal/what0", "w") as nulis:
   baca = str(int(baca) + 1)
   if not int(baca) < len(jadwal):
    baca = "0"
   nulis.write(str(int(baca)))
  os.system("zenity --error --text 'its now for try hard\n%s'" %(jadwal[int(baca)]))
 else:
  print("still on the same day, not showing message...")
 #with open("jadwal/what0", "r+") as baca:
 # baca = baca.read()


main()
