import uuid 
import datetime 
from enclosure import Enclosure
from zoo import Zoo
class Animal: 
    def __init__ (self, species_name, common_name, age): 
        self.animal_id = str(uuid.uuid4())
        self.species_name = species_name 
        self.common_name = common_name 
        self.age = age 
        self.feeding_record = [] 
        self.enclosure = {} 
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
        #add animal to the enclosure

        
    def birth(self):
        child = Child(self)
        return child
    def die(self):
        self.enclosure = None

""" 
zvieratko = Animal("A","A",4)
zvieratko.home(455) """
class Child(Animal):
    def __init__(self,motherAnimal):
        self.animal_id = str(uuid.uuid4())
        self.age = 0
        self.feeding_record = [] 
        self.care_taker = None 
        self.medical_checkup = []
        self.common_name = motherAnimal.common_name
        self.species_name = motherAnimal.species_name
        self.enclosure = motherAnimal.enclosure
        self.motherID = motherAnimal.animal_id


#print(babatko)

            