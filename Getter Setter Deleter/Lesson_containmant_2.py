class Person: 
    def __init__(self, name, age): 
        self.__name = name 
        self.__age = age

    @property 
    def name(self): 
        return self.__name

    @name.setter 
    def name(self, name): 
        self.__name = name 

    @name.deleter
    def name(self):
        del self.__name

    @property 
    def age(self): 
        return self.__age 

    @age.setter 
    def age(self, age): 
        if age <= 0: 
            raise ValueError("Не верное значение") 
        self.__age = age
    @age.deleter
    def age(self):
        del self.__age

person = Person('Ivan', 1) 
print (person.name) 
person.name = 'Danil'
print (person.name)
del person.name
del person.age

print(person.name, person.age)