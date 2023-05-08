### AirBnB clone - The Console
The AirBNB project is the first full web application project for Software 
engineering student in ALX. This project is about creating a minishell which 
works in an interactive and non-interactive mode.

## Command Interpreter or console ##
The first step in the Project is to be able to maniuplate a powerful storage
system (Storage engine), that will give an abstraction between "object" and
how these object are stored and persisted.

## How to start the Console
Use the command to start the console ./console.py

## How it can be Used: 
- Manage (create, update, destroy, e.t.c) objects via a console.
- Store and persist objects to a file (JSON file).
- Commands: create, show, destroy, all, update, help and quit

## Examples in an Interactive and non-interactive mode
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
