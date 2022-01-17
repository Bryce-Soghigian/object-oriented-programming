# Object Oriented Fundementals

Object oriented programming is a style of programming using objects to design and build applications. Contrary to procedure-oriented programming where programs are designed as blocks of statements to manipulate data, OOP organizes the program to combine data and functionality, and wrap it inside an object.





## The Four Principles of Object Oriented Programming

1. Encapsulation
2. inheritance
3. abscraction
4. polymorphism

## Encapsulation

Encapsulation is the mechanism of binding data together and hiding it from the outside world. Encapsulation is acheived when each object keeps its state private so the other objects don't have access to its state. Instead they can access this state only through public functions.

```python
class Product:
  def __init__(self):
    self.__maxprice = 900
  
  def sell(self):
    print(f'Selling Price:{self.__maxprice}')
  
  def set_max_price(self, price):
    self.__maxprice = price
    
product = Product()
product.sell()

# change the price
product.__maxprice = 1000
product.sell()

# using setter function
product.set_max_price(1000)
product.sell()

```

## Abscraction

Abscraction can be thought of as a natural extension of encapsulation. It means hiding all but the relevant data about an object in order to reduce the complexity of a system. In a large system, objects talk to each other, which makes it difficult to maintain a large system. Abscraction helps by hiding internal implementation details of objects and only revealing operations that are relevant to other objects.

```python
from abc import ABC, abstractmethod

class Parent(ABC):
  def common(self):
    print('In common method of Parent')

  @abstractmethod
  def vary(self):
    pass

class Child1(Parent):
  def vary(self):
    print('In vary method of Child1')

class Child2(Parent):
  def vary(self):
    print('In vary method of Child2')

# object of Child1 class
child1 = Child1()
child1.common()
child1.vary()

# object of Child2 class
child2 = Child2()
child2.common()
child2.vary()
```

 ## Inheritance

Inheritance can be used to create new objects using existing objects. Often paired with abscraction where we have a base class that can be used by multiple pieces of a system.

```python
class Person(object): 

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False
   

class Employee(Person):

    def is_employee(self): 
        return True
   
# Driver code
emp = Person("Person 1")
print("{} is employee: {}".format(emp.get_name(), emp.is_employee()))

emp = Employee("Employee 1")
print("{} is employee: {}".format(emp.get_name(), emp.is_employee()))
```

## Polymorphism

Polymorphism is the ability of an object to take different forms and thus depending on the context, to repsond to the same message in different ways. Take the example of a chess game. Each piece has the same responsibility to make moves, but the behavior of that move is different piece to piece.

```python
class Bishops:

    def move(self):
        print("Bishops can move diagonally")

class Knights:

    def move(self):
        print("Knights can move two squares vertically and one square horizontally, or two squares horizontally and one square vertically")

# common interface
def move_test(chess_piece):
    chess_piece.move()
# Driver code

#instantiate objects
bishop = Bishops()
knight = Knights()

# passing the object
move_test(bishop)
move_test(knight)
```

