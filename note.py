#!/usr/bin/python
from sys import argv

argc = len(argv)
availableOperators = ('+', '-', '/', '?')#needed?

filePaths = {
	'note' : '/home/i/.myNotes/note.txt',
	'muse' : '/home/i/.myNotes/muse.txt',
	'film' : '/home/i/.myNotes/film.txt',
	'book' : '/home/i/.myNotes/book.txt',
}

#http://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file
def prependLine(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

if( argc < 3 ):#too few args
	print 'za malo argumentow'

elif(argc == 3):#example: ">note dupa"
	#choosing right folder based on parameter from alias
	if( argv[1] == 'note' ):
		filePath = filePaths['note']
		print filePath
	elif( argv[1] == 'muse' ):
		filePath = filePaths['muse']
	elif( argv[1] == 'film' ):
		filePath = filePaths['film']
	elif( argv[1] == 'book' ):
		filePath = filePaths['book']

elif( argc == 4):#example: ">note + dupa"
	if( argv[2] == '+' ):#dodanie nowego wpisu
		#adding note to a file
		prependLine(notePath, "")
		prependLine( notePath, argv[3] )
		print 'added text: ' + argv[3]
	print '4'


	#print 'przy wyborze pliku: zly parametr'
	#nie bedzie przypadku podania zlego parametru bo aliasy mapuja bezposrednio do tylko 4 opcji

	# 
	# 	print '+'
	# elif( argv[2] == '-' ):#usuniecie wpisu
	# 	print '- not handled yet'
	# elif( argv[2] == '/' ) or ( argv[2] == '?' ):
	# 	print 'searching not handled yet'


# if(sys.argv[1] == "song"):
#   print "SONG"

# if(argc == 1):
#   file = open(notePath, 'r')
#   fileContent = file.read()
#   print fileContent
#   file.close()
# else:
#   if(sys.argv[1] == "+"):
#     #kod dodania do note.txt
#     #otworz plik z notes
#     #file = open(notePath, 'w')
#     #open(notePath, "w").write("#test firstline\n" + open(notePath).read())
#     prepend_line(notePath, "");#bcs we want an empty line between lines
#     prepend_line(notePath, sys.argv[2])
#     print 'added text: ' + sys.argv[2]
#     #
#     #


# #print sys.argv
# #print sys.argv
