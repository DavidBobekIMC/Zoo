import uuid
import datetime


class Animal:
    def __init__(self, species_name, common_name, age):
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
        self.feeding_record.append(datetime.datetime.now())

    def vet(self):
        self.medical_checkup.append(datetime.datetime.now())

    def assign_caretaker(self, caretakerobj):
        if self.care_taker == None:
            self.care_taker = caretakerobj
            caretakerobj.animals.append(self)

        else:
            pass

    def assign_enclosure(self, enclosure_):
        self.enclosure = enclosure_

    def birth(self):
        child = Child(self)

        return child

    def die(self):
        self.enclosure = None


class Child(Animal):
    def __init__(self, motherAnimal):
        self.animal_id = str(uuid.uuid4())
        self.age = 0
        self.feeding_record = []
        self.care_taker = None
        self.medical_checkup = []
        self.common_name = motherAnimal.common_name
        self.species_name = motherAnimal.species_name
        self.enclosure = motherAnimal.enclosure
        self.motherID = motherAnimal.animal_id
