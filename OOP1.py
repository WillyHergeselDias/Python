class Animal:
 def __init__(self,name,age):
  self.name = name
  self.age = age
class Cat(Animal):
 def __init__(self,name,age,species):
  super().__init__(name,age)
  self.species = species
  print(f'Name : {self.name}\nAge: {self.age}\nSpecies: {self.species}')

##Insert stuff here
name = input()
age = int(input())
species = input()
cat = Cat(name,age,species)