import uuid 
import datetime 
from enclosure import Enclosure


class Animal: 
    def __init__ (self, species_name, common_name, age): 
        self.animal_id = str(uuid.uuid4())
        self.species_name = species_name 
        self.common_name = common_name 
        self.age = age 
        self.feeding_record = [] 
        self.enclosure = None 
        self.care_taker = None 
        self.medical_checkup = []
        
        # add more as required here 
        
    # simply store the current system time when this method is called    
    def feed(self): 
        self.feeding_record.append ( datetime.datetime.now()) 

    def vet(self):
        self.medical_checkup.append( datetime.datetime.now())

    def home(self,enclosure_id):
        self.enclosureID = enclosure_id
        print("hey")
        #Enclosure Name

        self.enclosure = Enclosure(enclosure_id,self.animal_id)
        print(self.enclosure.house)
        """ self.enclosure[self] = enclosure_id """

        
    def birth(self):
        pass
""" 
zvieratko = Animal("A","A",4)
zvieratko.home(455) """
class Child(Animal):
    def __init__(self,species_name,common_name):
        self.animal_id = str(uuid.uuid4())
        self.species_name = species_name 
        self.common_name = common_name 
        self.age = 1
        self.feeding_record = [] 
        self.enclosure.house[self.animal_id] = self.enclosureID
        self.care_taker = None 
        self.medical_checkup = []
        

        super().__init__(self,species_name,common_name)

    


dospeli = Animal("a","a",1)
babatko = Child("a")
print(babatko)

            