import uuid 
import datetime 
import enclosure



class Animal: 
    def __init__ (self, species_name, common_name, age): 
        self.animal_id = str(uuid.uuid4())
        self.species_name = species_name 
        self.common_name = common_name 
        self.age = age 
        self.feeding_record = [] 
        self.enclosure = None 
        self.care_taker = None 
        self.medical_checkup = None
        
        # add more as required here 
        
    # simply store the current system time when this method is called    
    def feed(self): 
        self.feeding_record.append ( datetime.datetime.now()) 

    def vet(self):
        self.medical_checkup =  datetime.datetime.now()

    def home(self,enclosure_id):
        enclosure.enclosure[self]=enclosure_id
        self.enclosure = enclosure_id
        print(enclosure.enclosure)




            