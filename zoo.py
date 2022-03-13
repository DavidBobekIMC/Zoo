class Zoo: 
    def __init__ (self): 
        self.animals = []
        self.deadanimals = []
        self.all_Enclosures = []
        
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


