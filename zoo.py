class Zoo: 
    def __init__ (self): 
        self.animals = []
        self.deadanimals = []
        
    def addAnimal(self, animal): 
        self.animals.append (animal) 
        
    def removeAnimal(self, animal): 
        self.animals.remove(animal) 
    
    def getAnimal(self, animal_id): 
        for animal in self.animals: 
            if animal.animal_id == animal_id: 
                return animal 

    def animal_die(self,animal):
        self.deadanimals.append(animal)
        self.animals.remove(animal)

  