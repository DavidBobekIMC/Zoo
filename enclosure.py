from ctypes import addressof
from select import select



class Enclosure:
    def __init__(self,name,area):
        self.animals = []
        self.name = name
        self.area = area

    def removeAnimal(self,animal_id):
        self.animals.remove(animal_id)

        
        



    
    

