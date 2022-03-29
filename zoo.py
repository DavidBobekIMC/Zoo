import datetime
import random
from random import *
from matplotlib.style import available

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
        found = 0 
        for animal in self.animals: 
            if animal.animal_id == animal_id:
                found = 1 
                return animal
             
            
    def animal_home(self,targeted_animal,new_enclosure):
        if targeted_animal.enclosure == None:
            #checking if animal is without an enclosure
            targeted_animal.enclosure = new_enclosure.name
            targetedEnclosure = self.getEnclosure(new_enclosure.name)
            targetedEnclosure.animals.append(targeted_animal)
        
        else:
            #getting the current enclosure
            presentEnclosure = targeted_animal.getEnclosure(targeted_animal.enclosureID)
            #deleting the ID of animal form the enclosure
            presentEnclosure.animals.remove(targeted_animal)
            #finding where I want to add animal
            targeted_animal.enclosure = new_enclosure.name
            targetedEnclosure = self.getEnclosure(new_enclosure.name)

            #adding it to the enclosure
            targetedEnclosure.animals.append(targeted_animal)
    
        

    def getEnclosure(self,enclosure_id):
        print(self.all_Enclosures)
        for enclosure in self.all_Enclosures:
            print(enclosure) 
            if enclosure.name == enclosure_id: 
                print(enclosure)
                return enclosure 


    def animal_die(self,animal,animals_enclosure):
        animals_enclosure.animals.remove(animal)
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

    def deleteEnclosure(self,abouttoberemoved):
        self.all_Enclosures.remove(abouttoberemoved)

    def getRandomCaretaker(self,previousguy):
        randomguy = randrange(0,len(self.caretakers))
        
        if self.caretakers[randomguy] == previousguy:
            self.getRandomCaretaker(previousguy)
        else: 
            return self.caretakers[randomguy]

    def getRandomEnclosure(self,previousenclosure):
        randomEnclosure = randrange(0,len(self.all_Enclosures))
        
        if self.all_Enclosures[randomEnclosure] == previousenclosure:
            self.getRandomEnclosure(previousenclosure)
        else: 
            return self.all_Enclosures[randomEnclosure]
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

    def medical(self):
        returning_object ={
            
        }
       
        for animal in self.animals:
            if len(animal.medical_checkup)>0:
                last_one = animal.medical_checkup[-1]
            else:
                return "sorry"
            
            month =last_one.month
            day = last_one.day
            month_more = int(month)+1
            if day<(31-7):
                futureday = day+7
            else:
                month_more+=1
                futureday = 7-(31-day)
        
            returning_object[animal.animal_id] = f"Month:{month_more} Day:{futureday}"
        return returning_object

    
    def cleaning(self):
        returning_object ={
            
        }
        if len(self.all_Enclosures) ==0:
            return "there are no enclosures in the list"
        for  enclosure in self.all_Enclosures:
            if len(enclosure.cleaning_records)>0:
                last_one = enclosure.cleaning_records[-1]
            else:
                return "sorry"
            
            month =last_one.month
            day = last_one.day
            month_more = int(month)
            if day<(31-3):
                futureday = day+3
            else:
                month_more+=1
                futureday = 3-(31-day)

            person =randrange(0,len(self.caretakers))

            returning_object[enclosure.name] = f"Month:{month_more} Day:{futureday} Responsible person {self.caretakers[person].name}"
        return returning_object

    def feeding(self):
        returning_object ={
            
        }
        if len(self.animals) ==0:
            return "there are no animals in the list"
        for  animal in self.animals:
            if len(self.animals)>0:
                last_one = animal.feeding_record[-1]
            else:
                return "sorry"
            
            month =last_one.month
            day = last_one.day
            month_more = int(month)
            if day<(31-2):
                futureday = day+2
            else:
                month_more+=1
                futureday = 2-(31-day)

            #person =randrange(0,len(self.caretakers))

            returning_object[animal.animal_id] = f"Month:{month_more} Day:{futureday} Responsible person {animal.care_taker}"
        return returning_object

    def stat(self):
        total_number_per_species = {}
        if len(self.animals) ==0:
            return "there are no animals in the list"
        for x in self.animals:
            if x.species_name in total_number_per_species:
                total_number_per_species[x.species_name] +=1
            else:
                total_number_per_species[x.species_name] = 1
        
        all_animals_in_enclosures = []
        
        if len(self.all_Enclosures) ==0:
            return "there are no enclosures in the list"          
        for x in self.all_Enclosures:
            all_animals_in_enclosures.append(len(x.animals))

        average_animals_in_enclosure = sum(all_animals_in_enclosures)/len(self.all_Enclosures)
        available_space = {}
        for x in self.all_Enclosures:
            available_space[x.name] =(int(x.area))/(int(len(x.animals)))

        return f"{total_number_per_species} \n Average number of animals per Enclosure = {average_animals_in_enclosure} Average area per animal in each enclosure:{available_space}"




    



        




