# 0x00. AirBnB clone - The console
**Creating a simple command interpreter to manage AirBnB objects**

## <p align="center">![alt text](https://github.com/Omewah/AirBnB_clone/blob/main/web/images/hbnb.png?raw=true)</p>

## Background Context
This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration

Each task is linked and will help you to:
	* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
	* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
	* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
	* create the first abstracted storage engine of the project: File storage.
	* create all unittests to validate all our classes and storage engine

## Compilation
**To start up the interpreter, clone this repository, and run the console file on linux as follows:**
- Clone this repository: ```git clone "https://github.com/Omewah/AirBnB_clone.git"```
- Access AirBnb directory: ```cd AirBnB_clone```
- Run hbnb(interactively): ```./console``` and then press enter command
- Run hbnb(non-interactively): ```echo "<command>" | ./console.py```

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

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
```
##Authors
- Joel Omewah
- Precious Okolie
