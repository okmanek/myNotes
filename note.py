#!/usr/bin/env python

#----------------------------------------------------------------------------
#"THE BEER-WARE LICENSE" (Revision 42):
#<phk@FreeBSD.ORG> wrote this file.  As long as you retain this notice you
#can do whatever you want with this stuff. If we meet some day, and you think
#this stuff is worth it, you can buy me a beer in return.   okmanek
#----------------------------------------------------------------------------

#https://github.com/okmanek/myNotes

############ imports ############
from sys import argv
import os
import subprocess

#arguments:
#>note
#['/home/i/code/github-okmanek/myNotes/note.py', 'book']

############ variables ############
argc = len(argv)
searchResultNeighbours = 1#how many surrounding lines is shown while searching
opers = [ '+', '/', '?' ]#available operators
filePath = '/home/i/.myNotes/note.txt'

############ functions ############
#http://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file
def prependLine(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def showContent():
  file = open(filePath, 'r')
  fileContent = file.read()
  print(fileContent)
  file.close()

############ code itself ############
if( argc < 1 ):#only happens when you execute script without using alias
  print('za malo argumentow')

else:#if number of args is 2 or more, choose appropriate filepath

  #> note
  if( argc == 1 ):#just show content
    showContent()
  else:
    if(argc == 2):#>note arg1
      if argv[1] in opers:#>note +
        print('blad, podales operator bez zadnych danych')
        #so you cannot note for example plus sign. I doubt it is a problem though
      else:#note dupa
        prependLine(filePath, "")
        prependLine( filePath, argv[1] )#file opened twice. TODO: fix it
        print('added text: ' + argv[1])
    else:#>note arg1 arg2 (...)
      
      if argv[1] in opers:#>note + "text to process"
        if argv[1] == '+':
          textToSave = " ".join(argv[2:])
          prependLine(filePath, "")
          prependLine( filePath, textToSave )#file opened twice. TODO: fix it
          print('text added: ' + textToSave)
        elif argv[1] == '-':
          print('code for minus. not existing yet')
          print('odejmowanie')
          #not tested yet!!!
          lineNum = os.system('grep -nr %s %s | head -c 1' % (searchedText, fileName))
          with open(fileName, "r") as textObj:
            list = list(textObj)
          del list[ lineNum - 1 ]#add neighbours
          with open("a.txt", "w") as textObj:
            for n in list:
              textObj.write(n)
        elif argv[1] == '/' or argv[1] == '?':
          
          print('this is what i found:')
          cmd = "grep -C " + str(searchResultNeighbours) + " -n " + argv[2] + " " + filePath
          process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          stdout, stderr = process.communicate()
          print(stdout)
        #save to file argv[3:] (i think so)

      else:#>note dupa1 dupa2 dupa3
        textToSave = " ".join(argv[1:])
        prependLine(filePath, "")
        prependLine( filePath, textToSave )#file opened twice. TODO: fix it
        print('added text: ' + textToSave)
        #save to file argv[2:] (i think so)
