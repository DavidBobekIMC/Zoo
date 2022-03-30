from signal import default_int_handler
from unicodedata import name
import pytest

from zooma import *
from animal import *
from caretaker import *
from zoo import *
from enclosure import *
import random


def testAnimalToZoo():
    new_zoo = Zoo()
    current_number_animals = len(my_zoo.animals)
    new_animal = Animal ("Lion", "David", 2) 
    new_zoo.addAnimal (new_animal)
    assert len(new_zoo.animals) != current_number_animals
    
    
def testAnimalMakeHome():
    new_animal = Animal ("Lion", "David", 2) 
    new_enclosure = Enclosure("Cage",250)
    new_animal.assign_enclosure(new_enclosure)
    assert new_animal.enclosure == new_enclosure
    
    
def testAnimalVet():
    new_animal = Animal ("Lion", "David", 2) 
    number_of_medical_checkups = len(new_animal.medical_checkup)
    new_animal.vet()
    assert number_of_medical_checkups + 1 == len(new_animal.medical_checkup)
    

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
    
def testCleaningEnclosure():
    new_zoo = Zoo()
    new_enclosure = Enclosure("Cage",250)
    new_zoo.add_enclosure(new_enclosure)
    num_of_cleanups = len(new_enclosure.cleaning_records)
    new_zoo.clean_enclosure(new_enclosure.name)
    assert num_of_cleanups +1 == len(new_enclosure.cleaning_records)


def testEmployeeTakesCare():
    new_caretaker1 = Caretaker("John","21/11045")
    new_caretaker2 = Caretaker("Patrick","56/78224")
    new_animal = Animal ("Lion", "David", 2)
    new_animal.assign_caretaker(new_caretaker1)
    new_animal.assign_caretaker(new_caretaker2)
    assert new_animal.care_taker == new_caretaker1
    assert new_animal in new_caretaker1.animals
    
def testFeeding():
    new_animal = Animal("Lion","David",2)
    defaultNumFeeds = len(new_animal.feeding_record)
    new_animal.feed()
    assert defaultNumFeeds+1 == len(new_animal.feeding_record) 
    
def testBirth():
    new_animal = Animal("Lion","David",2)
    new_enclosure = Enclosure("Cage",1000)
    new_animal.assign_enclosure(new_enclosure)
    new_child = new_animal.birth()
    assert new_animal.enclosure ==new_child.enclosure
    assert new_animal.species_name == new_child.species_name
    assert new_animal.animal_id != new_child.animal_id


#delete enclosure

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
    
    

testDeleteEnclosure()

    
    