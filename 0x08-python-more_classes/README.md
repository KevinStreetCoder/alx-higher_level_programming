
# 0x08. Python - More Classes
## Learning Objectives
At the end of this project, you are expected to be able to:
* Why Python programming is awesome
* What is OOP
* What is a class
* What is an object
* What is the difference between a class and an object
* What is encapsulation
* What is abstraction
* What is inheritance
* What is polymorphism
* What is a constructor
* What is a destructor
* What are attributes
* What are methods
* What is self
* What is a class attribute
* What is an instance attribute
* What is a property
* What is an is-a relationship
* What is a has-a relationship
* What is polymorphism
* How to use the `__str__` method
* How to use the `__repr__` method
* How to use decorators
* How to write unit tests
## Requirements
* Allowed editors: vi, vim, emacs, Sublime Text, Atom, Visual Studio Code
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* You are not allowed to use any module
* You are not allowed to import any module
## Tasks
0. Rectangle
Write a class named Rectangle that defines a rectangle by:
* A private instance attribute named `width`
* A private instance attribute named `height`
* A constructor that takes two arguments: `width` and `height`
* A public instance method named `area` that returns the area of the rectangle
* A public instance method named `perimeter` that returns the perimeter of the rectangle
1. Square
Write a class named Square that inherits from Rectangle, and defines a square by:
* A private instance attribute named `side`
* A constructor that takes one argument: `side`