## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## make a class named Dog that is-a Animal
class Dog(Animal):
    ## class Dog has-a __init__ that takes self and name parameters
    def __init__(self, name):
        ## from self get the name attribute and set it to name
        self.name = name

## make a class named Cat that is-a Animal
class Cat(Animal):
    ## class Cat has-a __init__ that takes self and name parameters
    def __init__(self, name):
        ## from self get the name attribute and set it to name
        self.name = name

## make a class named Person that is-a object
class Person(object):
    ## class Person has-a __init__ that takes self and name parameters
    def __init__(self, name):
        ## from self get the name attribute and set it to name
        self.name = name
        ## from sefl get the pet attribute and set it to None
        ## Person has-a pet of some kind
        self.pet = None

## make a class named Employee that is-a Person
class Employee(Person):
    ## class Employee has-a __init__ that takes self, name and salary parameters
    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        ## from self get the salary attribute and set it to salary
        self.salary = salary

## make a class named Fish that is-a object
class Fish(object):
    pass

## make a class named Salmon that is-a Fish
class Salmon(Fish):
    pass

## make a class named Halibut that is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog, set rover to an instance of class Dog
rover = Dog("Rover")

## set satan to an instance of class Cat
satan = Cat("Satan")

## set mary to an instance of class Person
mary = Person("Mary")

## set frank to an instance of class Employee, and call it with self = Frank, and parameters salary = 120000
frank = Employee("Frank", 120000)

## from frank get the pet attribute and set it to rover
frank.pet = rover

## set flipper to an instance of class Fish
flipper = Fish()

## set crouse to an instance of class Salmon
crouse = Salmon()

## set harry to an instance of class Halibut
harry = Halibut()
