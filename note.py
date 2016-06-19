#!/usr/bin/python
import sys

argc = len(sys.argv)

notePath = '/home/i/iop/note.txt'
notePath2 = '/home/i/iop/note.txt'

#http://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file
def prepend_line(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

if(argc == 1):
  file = open(notePath, 'r')
  fileContent = file.read()
  print fileContent
  file.close()
else:
  if(sys.argv[1] == "+"):
    print "dodaje"
    #kod dodania do note.txt
    #otworz plik z notes
    #file = open(notePath, 'w')
    #open(notePath, "w").write("#test firstline\n" + open(notePath).read())
    prepend_line(notePath, "");#bcs we want an empty line between lines
    prepend_line(notePath, sys.argv[2])
    print 'dodano'
    #
    #


#print sys.argv
#print sys.argv
