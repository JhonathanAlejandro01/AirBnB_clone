# AirBnB clone
![python](https://miro.medium.com/max/2560/0*8aY8pX5CoNGImZU4.png)
## The console :computer:

The command interpreter is used to manage your AirBnB objects.

**Installation**
Use the git clone command:
`git clone https://github.com/JhonathanAlejandro01/AirBnB_clone`

**Interface**
Your shell should work like this in interactive mode:
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
```
But also in non-interactive mode: (like the Shell project in C)
```
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
**Execution**
```
$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) quit 
$
```

## Directory and Files :file_folder:

 - `console.py`
 - **tests/**
	 - `__init__.py`
	 - **test_models/**
		 - `test_base_model.py`
		 - `__init__.py`
		 - **test_engine/**
			 - `__init__.py`
			 - `test_file_storage.py`
 - **models/**
	 - `base_model.py`
	 - `__init__.py`
	 - `user.py`
	 - `amenity.py`
	 - `state.py`
	 - `city.py`
	 - `place.py`
	 - `review.py`
	 - **engine/**
		 - `__init__.py`
		 - `file_storage.py`

## *Questions?*
write to us [@Alejandro_Angar](https://twitter.com/Alejandro_Angar) or [@Diego35710808](https://twitter.com/Diego35710808)

