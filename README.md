myNotes is my attempt to create terminal-based notes tool.
I'll start with using aliases and simple python script.

motto of myNotes is:
"OSZCZĘDZAJ RAM GDZIEKOLWIEK JESTEŚ"

To make it work you need to add an alias:
>alias note ~/note.py
where ~/note.py is path to python script
alias note ~/code/github-okmanek/myNotes/note.py

Example of usage:
  >note + "dupa"
  adds note "dupa" to certain file.

Arguments:
  p|a - prepends|appends text to the file
  P|A - removes first|last text in the file
  s - searches for a text and returns all occurences

toDo functionalities:
  >seeing notes
  >removing notes
  >backup - uploading to the server
  >synchronising
  >many platforms
  >Firefox extension adding selected text to the file
  >dictionary mapping zamiast tylu ifów
    http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
    http://www.pydanny.com/why-doesnt-python-have-switch-case.html