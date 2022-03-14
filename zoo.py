import datetime
import random
from random import *

from numpy import average
from caretaker import Caretaker
class Zoo: 
    def __init__ (self): 
        self.animals = []
        self.deadanimals = []
        self.all_Enclosures = []
        self.caretakers = []
        
    def addAnimal(self, animal): 
        self.animals.append (animal) 
        
    def removeAnimal(self, animal): 
        self.animals.remove(animal) 
    
    def getAnimal(self, animal_id): 
        for animal in self.animals: 
            if animal.animal_id == animal_id: 
                return animal 

    def getEnclosure(self,enclosure_id):
        print(self.all_Enclosures)
        for enclosure in self.all_Enclosures:
            print(enclosure) 
            if enclosure.name == enclosure_id: 
                print(enclosure)
                return enclosure 


    def animal_die(self,animal):
        self.deadanimals.append(animal)
        self.animals.remove(animal)

    def add_enclosure(self,enclosure):
        y = 1
        for x in self.all_Enclosures:
            if x.name == enclosure.name:
                y = 0
        if y == 1:
            self.all_Enclosures.append(enclosure)
    
    def clean_enclosure(self,enclosure_id):
        for enclosure in self.all_Enclosures:     
            if enclosure.name == enclosure_id:
                enclosure.cleaning_records.append(datetime.datetime.now())
                print(enclosure.cleaning_records)
    
    def add_Caretaker(self,caretaker):
        self.caretakers.append(caretaker)

    def getCaretaker(self,caretaker_name):
        for caretaker in self.caretakers: 
            if caretaker.name == caretaker_name: 
                return caretaker 
    
    def kick(self,thepoor_guy):
        self.caretakers.remove(thepoor_guy)

    def getRandomCaretaker(self,previousguy):
        randomguy = randrange(0,len(self.caretakers))
        
        if self.caretakers[randomguy] == previousguy:
            self.getRandomCaretaker(previousguy)
        else: 
            return self.caretakers[randomguy]

    def stats(self):
        num_animals = []
        for employee in self.caretakers:
            num_animals.append(len(employee.animals))

        smallest = min(num_animals)
        average_ = sum(num_animals)/len(num_animals)
        highest = max(num_animals)
        
        returning_object ={
            "Minimum":smallest,
            "Average":average_,
            "Highest":highest,
            
        }
        return returning_object
        




