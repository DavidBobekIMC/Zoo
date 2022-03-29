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
    

def testAnimalDie():
    new_zoo = Zoo()
    new_animal = Animal ("Lion", "David", 2)
    animalid = new_animal.animal_id 
    print(animalid)
    new_enclosure = Enclosure("Cage",250)
    new_zoo.addAnimal (new_animal)
    new_animal.assign_enclosure(new_enclosure)
    
    new_enclosure.removeAnimal(new_animal)
    
    new_zoo.animal_die(new_animal)
    assert new_animal not in new_zoo.animals
    

testAnimalMakeHome()