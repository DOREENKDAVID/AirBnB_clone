# 0x00. AirBnB clone - The console

![AirBnB Clone](https://github.com/DOREENKDAVID/AirBnB_clone/assets/123072803/13bec8dd-2bc9-4112-8ce5-a01ee0bf20c9)


## Project Description

This team project is a key part of the ALX Africa Full-Stack Software Engineering program. It's the first step towards building a first full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## How To Start The Console

To start the console follow the following steps:

-```git clone https://github.com/DOREENKDAVID/AirBnB_clone```

-```cd AirBnB_clone```

-```./console.py```

## How To Use The Console

The console works both in interactive mode and non-interactive mode, just like a Unix shell. It prints a prompt **(hbnb)** and waits for the user for input.

Action | Command
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id)| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

## Non-interactive mode example

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

## Tests

All the code is tested with the **unittest** module.

## Authors 

- [DOREEN K DAVID](https://github.com/DOREENKDAVID)

- [Geofrey Ouma](https://github.com/i18nfoo)
