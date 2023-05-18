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
## Installation :hammer_and_wrench:
Clone the repository and run the console.py
```
$ git clone https://github.com/------/AirBnB_clone.git
```

## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |


## Built with :gear:
python3 (3.4.3)

### Acknowledgements :raised_hands:
To all the peers that contribuited with their knowledge
