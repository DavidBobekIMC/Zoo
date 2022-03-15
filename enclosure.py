from ctypes import addressof
from select import select



class Enclosure:
    def __init__(self,name,area):
        self.animals = []
        self.name = name
        self.area = area
        self.cleaning_records = []

    def removeAnimal(self,animal_id):
        self.animals.remove(animal_id)

    def takeResponsibility(self,list_of_animals):
        for x in list_of_animals:
            self.animals.append(x)


    

        
        



    
    

