# Python - Classes and Objects

## Requirements
### General
	Allowed editors: vi, vim, emacs
	All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	All your files should end with a new line
	The first line of all your files should be exactly #!/usr/bin/python3
	A README.md file, at the root of the folder of the project, is mandatory
	Your code should use the pycodestyle (version 2.8.*)
	All your files must be executable
	The length of your files will be tested using wc
	All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
	All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
	All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
	A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks
### 0. My first square
	Write an empty class "square" that defines a square:
		You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$ 
```


