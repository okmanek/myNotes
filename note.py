#!/usr/bin/python
from sys import argv
import os

argc = len(argv)
availableOperators = ('+', '-', '/', '?')#needed?
searchResultNeighbours = 1 #how many surrounding lines is shown while searching

filePaths = {
	'note' : '/home/i/.myNotes/note.txt',
	'song' : '/home/i/.myNotes/song.txt',
	'film' : '/home/i/.myNotes/film.txt',
	'book' : '/home/i/.myNotes/book.txt',
}

#http://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file
def prependLine(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

if( argc < 2 ):#too few args
	print 'za malo argumentow'

else:#if number of args is 2 or more, choose appropriate filepath
	if( argv[1] == 'note' ):
		filePath = filePaths['note']
	elif( argv[1] == 'song' ):
		filePath = filePaths['song']
	elif( argv[1] == 'film' ):
		filePath = filePaths['film']
	elif( argv[1] == 'book' ):
		filePath = filePaths['book']
		#note that there cannot be bad parameter because of the aliases system

	#> note #just show content	
	if( argc == 2 ):#just show content
		file = open(filePath, 'r')
		fileContent = file.read()
		print fileContent
		file.close()

	#>note "text to add"
	if( argc == 3 ):#just for now
		prependLine(filePath, "")
		prependLine( filePath, argv[2] )
		print 'added text: ' + argv[2]

	#>note + "text to process" # where '+' can be any operator
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


	# 
	# 	print '+'
	# elif( argv[2] == '-' ):#usuniecie wpisu
	# 	print '- not handled yet'
	# elif( argv[2] == '/' ) or ( argv[2] == '?' ):
	# 	print 'searching not handled yet'


# else:
#   if(sys.argv[1] == "+"):
#     #kod dodania do note.txt
#     #otworz plik z notes
#     #open(notePath, "w").write("#test firstline\n" + open(notePath).read())
#     prepend_line(notePath, "");#bcs we want an empty line between lines
#     prepend_line(notePath, sys.argv[2])
#     print 'added text: ' + sys.argv[2]
#     #
#     #
