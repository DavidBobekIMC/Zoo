class Caretaker:
    def __init__(self,name,address):
        self.name = name 
        self.address =address
        self.animals = []
        

    def care(self,animal):
        self.animals.append(animal)
