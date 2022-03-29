from unicodedata import name
import pytest

from zooma import *
from animal import *
from caretaker import *
from zoo import *
from enclosure import *



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
    

    

    
    