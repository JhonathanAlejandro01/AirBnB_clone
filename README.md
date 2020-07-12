# AirBnB clone
![hbnb](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png))
## The console :computer:

The command interpreter is used to manage your AirBnB objects.

**Installation** :page_facing_up:
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
 - **web_static/**
	 - 0-index.html
	 - 1-index.html
	 - 2-index.html
	 - 3-index.html
	 - 4-index.html
	 - 5-index.html
	 - 6-index.html
	 - 7-index.html
	 - **styles/**
		 - 2-common.css  
		 - 2-header.css
		 - 2-footer.css
		 - 3-common.css 
		 - 3-header.css 
		 - 3-footer.css
		 - 4-common.css  
		 - 4-filters.css
		 -  5-filters.css
		 -  6-filters.css
		 - 7-places.css
	 - **images/**
		 - icon.png
		 - logo.png

## *Questions?*
:+1: Write to us [@Alejandro_Angar](https://twitter.com/Alejandro_Angar) or [@Diego35710808](https://twitter.com/Diego35710808)

