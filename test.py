from signal import default_int_handler
from unicodedata import name
import pytest

from zooma import *
from animal import *
from caretaker import *
from zoo import *
from enclosure import *
import random

#testing if animal was added into the zoo
def testAnimalToZoo():
    new_zoo = Zoo()
    new_animal = Animal ("Lion", "David", 2) 
    new_zoo.addAnimal (new_animal)
    assert new_animal in new_zoo.animals
    

#testing if we create an animal and enclosure,the animal is capable of haivng a home and vice versa 
def testAnimalMakeHome():
    new_animal = Animal ("Lion", "David", 2) 
    new_enclosure = Enclosure("Cage",250)
    new_animal.assign_enclosure(new_enclosure)
    assert new_animal.enclosure == new_enclosure
    assert new_animal in new_enclosure.animals
    

# basic testing that record of a medical checkup is being added to the record
def testAnimalVet():
    new_animal = Animal ("Lion", "David", 2) 
    number_of_medical_checkups = len(new_animal.medical_checkup)
    new_animal.vet()
    assert number_of_medical_checkups + 1 == len(new_animal.medical_checkup)
    
#Similiar function as vet
def testFeeding():
    new_animal = Animal("Lion","David",2)
    defaultNumFeeds = len(new_animal.feeding_record)
    new_animal.feed()
    assert defaultNumFeeds+1 == len(new_animal.feeding_record) 
    

#testing that if animal dies it is removed from the zoo and enclosure
def testAnimalDie():
    new_zoo = Zoo()
    new_animal = Animal ("Lion", "David", 2)
    animalid = new_animal.animal_id 
    print(animalid)
    new_enclosure = Enclosure("Cage",250)
    new_zoo.addAnimal (new_animal)
    new_animal.assign_enclosure(new_enclosure)
    new_zoo.animal_die(new_animal,new_enclosure)   
    assert new_animal not in new_zoo.animals
    assert new_animal not in new_enclosure.animals
    

#testing that the Enclosure can be cleaned and the record is being added into the records
def testCleaningEnclosure():
    new_zoo = Zoo()
    new_enclosure = Enclosure("Cage",250)
    new_zoo.add_enclosure(new_enclosure)
    num_of_cleanups = len(new_enclosure.cleaning_records)
    new_zoo.clean_enclosure(new_enclosure.name)
    assert num_of_cleanups +1 == len(new_enclosure.cleaning_records)


#testing that if an animal already has an caretaker it can not have anyother
def testEmployeeTakesCare():
    new_caretaker1 = Caretaker("John","21/11045")
    new_caretaker2 = Caretaker("Patrick","56/78224")
    new_animal = Animal ("Lion", "David", 2)
    new_animal.assign_caretaker(new_caretaker1)
    new_animal.assign_caretaker(new_caretaker2)
    assert new_animal.care_taker == new_caretaker1
    assert new_animal in new_caretaker1.animals
    assert new_animal not in new_caretaker2.animals
    

#Testing that new animal is not only created bu created into the same enclosure as its mother

def testBirth():
    new_animal = Animal("Lion","David",2)
    new_enclosure = Enclosure("Cage",1000)
    new_animal.assign_enclosure(new_enclosure)
    new_child = new_animal.birth()
    assert new_animal.enclosure ==new_child.enclosure
    assert new_animal.species_name == new_child.species_name
    assert new_animal.animal_id != new_child.animal_id


#testing that if we delete the enclosure that animals from the enclosure being transferred into a new one 

def testDeleteEnclosure():
    new_zoo = Zoo()
    new_enclosure = Enclosure("Cage",55)
    new_enclosure2 = Enclosure("Cage2",77)
    new_Animal1 = Animal("Lion","David",2)
    new_Animal2 = Animal("Rhino","John",5)
    
    
    new_zoo.add_enclosure(new_enclosure)
    new_zoo.add_enclosure(new_enclosure2)
    
    
    new_Animal1.assign_enclosure(new_enclosure)
    new_Animal2.assign_enclosure(new_enclosure)
    
    
    targeted_new_enclosure = new_zoo.getRandomEnclosure(new_enclosure)
    list_of_animals = new_enclosure.animals
    new_zoo.deleteEnclosure(new_enclosure)
    
    targeted_new_enclosure.takeResponsibility(list_of_animals)
    assert new_Animal1 in new_enclosure2.animals
    assert new_Animal2 in new_enclosure2.animals
    assert new_enclosure not in my_zoo.all_Enclosures
    
    
def testLifeCycle():
    #creation of zoo animals and assigning encslosures to zoo and animals to enclosures
    new_zoo = Zoo()
    new_animal1 = Animal("Lion","David",1)
    new_animal2 = Animal("Fish","Matt",2)
    new_animal3 = Animal("Cat","Max",3)
    new_animal4 = Animal("Rat","Lewis",4)
    new_animal5 = Animal("Rhino","Alex",5)
    new_animal6 = Animal("Rhino","Sam",1)
    new_animal7 = Animal("Fish","Sergei",2)
    new_animal8 = Animal("Cat","Steph",3)
    new_animal9 = Animal("Rat","Leo",4)
    new_animal10 = Animal("Rhino","Boris",5)
    
    new_zoo.addAnimal(new_animal1)
    new_zoo.addAnimal(new_animal2)
    new_zoo.addAnimal(new_animal3)
    new_zoo.addAnimal(new_animal4)
    new_zoo.addAnimal(new_animal5)
    new_zoo.addAnimal(new_animal6)
    new_zoo.addAnimal(new_animal7)
    new_zoo.addAnimal(new_animal8)
    new_zoo.addAnimal(new_animal9)
    new_zoo.addAnimal(new_animal10)
    
    
    new_enclosure1 = Enclosure("Cage1",50)
    new_enclosure2 = Enclosure("Cage2",500)
    new_enclosure3 = Enclosure("Cage3",1000)
    
    new_caretaker1 = Caretaker("David",1)
    new_caretaker2 = Caretaker("Dinu",2)
    new_caretaker3 = Caretaker("Mike",3)
    

    new_caretaker1.care(new_animal1)
    new_caretaker1.care(new_animal2)
    new_caretaker2.care(new_animal3)
    new_caretaker2.care(new_animal4)
    new_caretaker2.care(new_animal5)
    new_caretaker3.care(new_animal6)
    new_caretaker3.care(new_animal7)
    new_caretaker3.care(new_animal8)
    new_caretaker3.care(new_animal9)
    new_caretaker3.care(new_animal10)
   
    
    assert new_animal1 in new_caretaker1.animals and new_animal2 in new_caretaker1.animals and new_animal3 in new_caretaker2.animals and new_animal4 in new_caretaker2.animals and new_animal5 in new_caretaker2.animals and new_animal6 in new_caretaker3.animals and new_animal7 in new_caretaker3.animals and new_animal8 in new_caretaker3.animals and new_animal9 in new_caretaker3.animals and new_animal10 in new_caretaker3.animals
    assert new_animal1.care_taker == new_caretaker1 and new_animal2.care_taker == new_caretaker1 and new_animal3.care_taker == new_caretaker2
    
    new_zoo.add_enclosure(new_enclosure1)
    new_zoo.add_enclosure(new_enclosure2)
    new_zoo.add_enclosure(new_enclosure3)
    
    
    
    new_animal1.assign_enclosure(new_enclosure1) 
    new_animal2.assign_enclosure(new_enclosure1) 
    new_animal3.assign_enclosure(new_enclosure1) 
    new_animal4.assign_enclosure(new_enclosure1) 
    new_animal5.assign_enclosure(new_enclosure1)
    new_animal6.assign_enclosure(new_enclosure2) 
    new_animal7.assign_enclosure(new_enclosure2) 
    new_animal8.assign_enclosure(new_enclosure2) 
    new_animal9.assign_enclosure(new_enclosure3) 
    new_animal10.assign_enclosure(new_enclosure3) 
    
    new_animal1.assign_enclosure(new_enclosure1) 
    new_animal2.assign_enclosure(new_enclosure1) 
    new_animal3.assign_enclosure(new_enclosure1) 
    new_animal4.assign_enclosure(new_enclosure1) 
    new_animal5.assign_enclosure(new_enclosure1)
    new_animal6.assign_enclosure(new_enclosure2) 
    new_animal7.assign_enclosure(new_enclosure2) 
    new_animal8.assign_enclosure(new_enclosure2) 
    new_animal9.assign_enclosure(new_enclosure3) 
    new_animal10.assign_enclosure(new_enclosure3) 
    
    
    assert new_enclosure1 in new_zoo.all_Enclosures and new_enclosure2 in new_zoo.all_Enclosures and new_enclosure2 in new_zoo.all_Enclosures
    
    #Animals 1 to 4 are giving birth
    new_animal11 =new_animal1.birth()
    new_animal12 =new_animal2.birth()
    new_animal13 =new_animal3.birth()
    new_animal14 =new_animal4.birth()
    
    new_zoo.addAnimal(new_animal11)
    new_zoo.addAnimal(new_animal12)
    new_zoo.addAnimal(new_animal13)
    new_zoo.addAnimal(new_animal14)
    
    assert new_animal11 in new_zoo.animals 
    assert new_animal12 in new_zoo.animals  
    assert new_animal13 in new_zoo.animals 
    
    new_zoo.removeAnimal(new_animal11)
    assert new_animal11 not in my_zoo.animals
    
    
    
    #delete an employee
    
    
testLifeCycle()
    
    