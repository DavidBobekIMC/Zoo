from unicodedata import name
import pytest

from zooma import *
from animal import *
from caretaker import *
from zoo import *
from enclosure import *



def testAnimalToZoo():
    current_number_animals = len(my_zoo.animals)
    new_animal = Animal ("Lion", "David", 2) 
    my_zoo.addAnimal (new_animal)
    assert len(my_zoo.animals) != current_number_animals
    
    
def testAnimalMakeHome():
    new_animal = Animal ("Lion", "David", 2) 
    new_enclosure = Enclosure("Cage",250)
    new_animal.assign_enclosure(new_enclosure.name)
    assert new_animal.enclosure == new_enclosure.name
    
