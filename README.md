myNotes is my attempt to create terminal-based notes-storing tool.
I'll start with aliases-based simple python script.

motto of myNotes is:

"OSZCZĘDZAJ RAM GDZIEKOLWIEK JESTEŚ, DZIWKO"

To make it work you need to add an alias:
>alias note ~/note.py
where ~/note.py is path to python script
alias note ~/code/github-okmanek/myNotes/note.py

Example of usage:
  >note + "dupa"
  - adds note "dupa" to certain file.

Arguments:
-(p or +) - prepends text to the file
-P|A - removes first|last text in the file
-s - searches for a text and returns all occurences

toDo functionalities:
-no parenthesees needed
-using subprocesses
-removing notes
-backup - uploading to the server
-synchronising
-many platforms
-Firefox extension adding selected text to the file
-Tags mechanism
-Config file
-Storing other datatypes, e.g. mp3, video
opis idei

wzorowac sie na:
https://github.com/prodicus/tnote




"""
zmiana sys.os np. na subprocess:

You shouldn't use os.system to run commands. You should use subprocess instead, for example:

from sys import argv
import subprocess

cmd = 's.py'
args = [cmd] + argv[2:]
subprocess.call(args)
"""
