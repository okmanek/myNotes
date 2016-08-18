#!/usr/bin/python
############ imports ############
from sys import argv
import os
import argparse

############ variables ############
argc = len(argv)
availableOperators = ('+', '-', '/', '?')#needed?
searchResultNeighbours = 1 #how many surrounding lines is shown while searching
opers = [ '+', '/', '?' ]#available operators

filePaths = {
  'note' : '/home/i/.myNotes/note.txt',
  'song' : '/home/i/.myNotes/song.txt',
  'film' : '/home/i/.myNotes/film.txt',
  'book' : '/home/i/.myNotes/book.txt',
}

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
  print fileContent
  file.close()

############ code itself ############
if( argc < 2 ):#only happens when you execute script without using alias
  print 'za malo argumentow'

else:#if number of args is 2 or more, choose appropriate filepath
  for i in filePaths:
    if( argv[1] == i):
      filePath = filePaths[i]

  #> note
  #just show content  
  if( argc == 2 ):#just show content
    showContent()
  else:
    if(argc == 3):#>note arg1
      if argv[2] in opers:#>note +
        print 'blad, podales operator bez zadnych danych'
        #so you cannot note for example plus sign. I doubt it is a problem though
      else:#note dupa
        prependLine(filePath, "")
        prependLine( filePath, argv[2] )#file opened twice. TODO: fix it
        print 'added text: ' + argv[2]
    else:#>note arg1 arg2 (...)
      if argv in opers:#>note + "text to process"
        pass
        #zapisanie do pliku argv[2:] (chyba)
      else:#>note dupa1 dupa2 dupa3
        #pass
        textToSave = " ".join(argv[2:])
        prependLine(filePath, "")
        prependLine( filePath, textToSave )#file opened twice. TODO: fix it
        print 'added text: ' + textToSave
        #zapisanie do pliku argv[1:] (chyba)
  
"""
  #>note + "text to process"
  # where '+' can be any operator
  if( argc == 4):
    oper = argv[2]
    if( oper == '+' ):
      prependLine( filePath, "" )
      prependLine( filePath, argv[3] )
      print 'added text: ' + argv[3]
    elif( oper == '/' ) or (oper == '?' ):
      os.system('grep -C %d -n %r %r' % (searchResultNeighbours, argv[3], filePath))#-nr?
    elif( oper == '-' ):
      print 'odejmowanie'
      #not tested yet!!!
      lineNum = os.system('grep -nr %s %s | head -c 1' % (searchedText, fileName))
      with open(fileName, "r") as textObj:
        list = list(textObj)
      del list[ lineNum - 1 ]#sasiedzi - dodac
      with open("a.txt", "w") as textObj:
        for n in list:
          textObj.write(n)
"""