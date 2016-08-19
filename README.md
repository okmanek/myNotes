Idea
myNotes is my attempt to create terminal-based notes-storing tool.
It's supposed to be as simple and quick to use as possible.

Motto of myNotes is:
"OSZCZĘDZAJ RAM GDZIEKOLWIEK JESTEŚ, DZIWKO"

History
It started as alias-based project. then I switched to just putting script file
in /usr/bin/
it has some ups and downs:

pros:
  -simplicity
  -don't need to create aliases for each file
  -don't need to use maps to store file paths
cons:
  -need to create different script for each note file

instalation guide:
1. copy 'note' to /usr/bin/
2. change 'filePath' variable to match you path of a file

installer will be created in the future

Example of usage:
>note         #shows content of a file
>note + dupa  #adds 'dupa' to a file. adding is a default behaviour, so...
>note dupa    #also adds 'dupa' to a file

>note / dupa  #searches for 'dupa'
>note

wzorowac sie na:
https://github.com/prodicus/tnote
