from ctypes import addressof
from select import select


class Enclosure:
    def __init__(self,enclosureID,animal_ID):
        self.house= {}
        self.house[enclosureID] = animal_ID
        



    
    

