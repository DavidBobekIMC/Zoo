import json
from tkinter.messagebox import NO, RETRY
from unittest import result
from flask import Flask, jsonify
from flask_restx import Api, reqparse, Resource
from caretaker import Caretaker
from zoo_json_utils import ZooJsonEncoder 
from zoo import Zoo 

from animal import Animal
from animal import Child
from enclosure import Enclosure

my_zoo = Zoo()

zooma_app = Flask(__name__)
# need to extend this class for custom objects, so that they can be jsonified
zooma_app.json_encoder = ZooJsonEncoder 
zooma_api = Api(zooma_app)

animal_parser = reqparse.RequestParser()
animal_parser.add_argument('species', type=str, required=True, help='The scientific name of the animal, e,g. Panthera tigris')
animal_parser.add_argument('name', type=str, required=True, help='The common name of the animal, e.g., Tiger')
animal_parser.add_argument('age', type=int, required=True, help='The age of the animal, e.g., 12')

@zooma_api.route('/animal')
class AddAnimalAPI(Resource):
    @zooma_api.doc(parser=animal_parser)
    def post(self):
        # get the post parameters 
        args = animal_parser.parse_args()
        name = args['name']
        species = args['species']
        age = args['age']
        
        # create a new animal object 
        for x in name:
            try:
                x = int(x)
                return jsonify(f"Invalid input {name}")
            except:
                pass

        for x in species:
            try:
                x = int(x)
                return jsonify(f"Invalid input {species}")
            except:
                pass

        new_animal = Animal (species, name, age) 
        #add the animal to the zoo
        my_zoo.addAnimal (new_animal) 
        return jsonify(new_animal) 
    

@zooma_api.route('/animal/<animal_id>')
class Animal_ID(Resource):
     def get(self, animal_id):
        search_result  = my_zoo.getAnimal(animal_id)
        if search_result == None:
            return jsonify("Animal not found")
        return search_result # this is automatically jsonified by flask-restx
    
     def delete(self, animal_id):
        targeted_animal  = my_zoo.getAnimal(animal_id)
        if not targeted_animal: 
            return jsonify(f"Animal with ID {animal_id} was not found")
        my_zoo.removeAnimal(targeted_animal)
        return jsonify(f"Animal with ID {animal_id} was removed") 
@zooma_api.route('/animals')
class AllAnimals(Resource):
     def get(self):
        if len(my_zoo.animals) ==0:
            return jsonify("There are no animals")
        return jsonify( my_zoo.animals)  
    

@zooma_api.route('/animals/<animal_id>/feed')
class FeedAnimal(Resource):
     def post(self, animal_id):
        targeted_animal  = my_zoo.getAnimal(animal_id)
        if not targeted_animal: 
            return jsonify(f"Animal with ID {animal_id} was not found") 
        targeted_animal.feed()
        return jsonify(targeted_animal)

@zooma_api.route('/animals/<animal_id>/vet')
class VetAnimal(Resource):
     def post(self, animal_id):
        targeted_animal  = my_zoo.getAnimal(animal_id)
        if not targeted_animal: 
            return jsonify(f"Animal with ID {animal_id} was not found") 
        targeted_animal.vet()
        return jsonify(targeted_animal)


homie = reqparse.RequestParser()
homie.add_argument('Enclosure ID', type=str, required=True)
@zooma_api.route('/animals/<animal_id>/home')
class HomeAnimal(Resource):
    @zooma_api.doc(parser=homie)
    def post(self, animal_id):
        targeted_animal  = my_zoo.getAnimal(animal_id)
        
        args = homie.parse_args()
        enclosure_id = args['Enclosure ID']
        targetedEnclosure = my_zoo.getEnclosure(enclosure_id)

        if targeted_animal not in my_zoo.animals:
            return jsonify(f"Animal with id {animal_id} was not found")

        if targetedEnclosure not in my_zoo.all_Enclosures:
            return jsonify(f"Animal with id {enclosure_id} was not found")
        

        if targeted_animal.enclosure == None:
            #checking if animal is without an enclosure
            targeted_animal.enclosure = enclosure_id
            targetedEnclosure = my_zoo.getEnclosure(enclosure_id)
            targetedEnclosure.animals.append(targeted_animal)
        
        else:
            #getting the current enclosure
            presentEnclosure = my_zoo.getEnclosure(targeted_animal.enclosureID)
            #deleting the ID of animal form the enclosure
            presentEnclosure.animals.remove(targeted_animal)
            #finding where I want to add animal
            targeted_animal.enclosure = enclosure_id
            targetedEnclosure = my_zoo.getEnclosure(enclosure_id)

            #adding it to the enclosure
            targetedEnclosure.animals.append(targeted_animal)
        
        if not targeted_animal or not targetedEnclosure: 
            return jsonify(f"Animal with ID {animal_id} was not found")
        
        
        return jsonify(targeted_animal)

kokot = reqparse.RequestParser()
kokot.add_argument('Mother_ID', type=str, required=True)       
@zooma_api.route('/animals/birth')
class AnimalBirth(Resource):
    @zooma_api.doc(parser=kokot)
    def post(self):
        args = kokot.parse_args()
        mother_id = args["Mother_ID"]         
        motherAnimal  = my_zoo.getAnimal(mother_id)
        if not motherAnimal: 
            return jsonify(f"Animal with ID {mother_id} was not found") 
        
        #need to return the child not parent = find a way


        #adding Instance of a subclass Animal called child into the enclosure where is mother
        AnimalChild = motherAnimal.birth()

        motherEnclosure = my_zoo.getEnclosure(motherAnimal.enclosure)

        if motherEnclosure == None:
            pass
        else:
            motherEnclosure.animals.append(AnimalChild)
            
        my_zoo.addAnimal (AnimalChild)
        return jsonify(AnimalChild)


hello = reqparse.RequestParser()
hello.add_argument('animal_id', type=str, required=True)       
@zooma_api.route('/animal/death')
class AnimalDie(Resource):
    @zooma_api.doc(parser=hello)
    def post(self):
        args = hello.parse_args()
        animal_id = args["animal_id"]         
        animalobj  = my_zoo.getAnimal(animal_id)
        if animalobj not in my_zoo.animals: 
            return jsonify(f"Animal with ID {animal_id} was not found") 
        
        #need to return the child not parent = find a way
        my_zoo.animal_die(animalobj)
        animalobj.die()
        return jsonify(animalobj)

enclosures = reqparse.RequestParser()
enclosures.add_argument('Enclosure ID', type=str, required=True)     
enclosures.add_argument('Area', type=str, required=True)   
@zooma_api.route('/enclosure')
class CreateEnclosure(Resource):
    @zooma_api.doc(parser=enclosures)
    def post(self):
        args = enclosures.parse_args()
        Enclosure_ID = args["Enclosure ID"]
        area = args["Area"]         
        for x in area:
            try:
                x = int(x)
            except:
               return jsonify(f"Input {area} must be a number")
        if int(area)<1:
            return jsonify(f"Input {area} is too small")
        Enclosure_ID = Enclosure(Enclosure_ID,area)
        if not Enclosure_ID: 
            return jsonify(f"Enclosure with ID {Enclosure_ID} was not found") 
        
        #need to return the child not parent = find a way
        my_zoo.add_enclosure(Enclosure_ID)   
        return jsonify(Enclosure_ID)

@zooma_api.route('/enclosures')
class AllAnimals(Resource):
     def get(self):
        return jsonify(my_zoo.all_Enclosures)  
    

@zooma_api.route('/enclosures/<enclosure_id>/clean')
class CleanEnclosrue(Resource):
     def post(self, enclosure_id):
        targeted_enclosure  = my_zoo.getEnclosure(enclosure_id)
        if targeted_enclosure == None: 

            return jsonify(f"Enclosure with ID {enclosure_id} was not found") 
        my_zoo.clean_enclosure(enclosure_id)
        return jsonify(targeted_enclosure)


@zooma_api.route('/enclosures/<enclosure_id>/animals')
class AllEnclosures(Resource):
     def get(self,enclosure_id):
        targeted_enclosure  = my_zoo.getEnclosure(enclosure_id)
        if targeted_enclosure == None: 

            return jsonify(f"Enclosure with ID {enclosure_id} was not found") 
        return jsonify(targeted_enclosure.animals)  
    
caretaker_parser = reqparse.RequestParser()
caretaker_parser.add_argument('name', type=str, required=True, help='The scientific name of the animal, e,g. Panthera tigris')
caretaker_parser.add_argument('address', type=str, required=True, help='The common name of the animal, e.g., Tiger')

@zooma_api.route('/enclosure/<enclosure_id>')
class deleteEnclosure(Resource):
    
    def delete(self,enclosure_id):
        if len(my_zoo.all_Enclosures)<1:
            return jsonify({f"Add some more enclosures before deleting"})
        
        Enclosure_That_will_be_kicked  = my_zoo.getEnclosure(enclosure_id)
        if Enclosure_That_will_be_kicked == None: 
            return (f"Caretaker with ID {enclosure_id} was not found") 
        new_Enclosure =my_zoo.getRandomEnclosure(Enclosure_That_will_be_kicked)
        

        if len(Enclosure_That_will_be_kicked.animals) == 0:
            pass
        else:
            oldAnimals = Enclosure_That_will_be_kicked.animals
            new_Enclosure.takeResponsibility(oldAnimals)
            for x in oldAnimals:
                x.assign_enclosure(new_Enclosure.name)
        

        
        my_zoo.deleteEnclosure(Enclosure_That_will_be_kicked)
        return jsonify(my_zoo.all_Enclosures)


@zooma_api.route('/employee')
class AddCaretaker(Resource):
    @zooma_api.doc(parser=caretaker_parser)
    def post(self):
        # get the post parameters 
        args = caretaker_parser.parse_args()
        address = args['address']
        name = args['name']
        for x in name:
            try:
                x = int(x)
                return jsonify(f"Invalid input {name}")
            except:
                pass
        
        
        # create a new animal object 
        newCaretaker = Caretaker(name, address) 
        #add the animal to the zoo
        my_zoo.add_Caretaker (newCaretaker) 
        return jsonify(newCaretaker) 

caretaker_animal = reqparse.RequestParser()
@zooma_api.route('/employee/<employee_id>/care/<animal_id>/')
class CaretakerAnimal(Resource):
    
    def post(self,animal_id,employee_id):
        
        targeted_animal  = my_zoo.getAnimal(animal_id) 
        if targeted_animal == None: 
            return jsonify(f"Animal with ID {animal_id} was not found")
        
        targeted_caretaker = my_zoo.getCaretaker(employee_id)
        
        if targeted_animal in targeted_caretaker.animals: 
            return jsonify(f"Animal with ID {animal_id} is already being took care of")
         
        if targeted_caretaker == None: 
            return jsonify(f"Animal with ID {employee_id} was not found") 
        targeted_caretaker.care(targeted_animal)
        targeted_animal.care_taker = targeted_caretaker.name
        return jsonify(targeted_caretaker)






@zooma_api.route('/employee/<employee_id>/care/animals')
class Allemployees(Resource):
     def get(self,employee_id):
        target_caretaker  = my_zoo.getCaretaker(employee_id)
        if target_caretaker == None: 
            return jsonify(f"Enclosure with ID {employee_id} was not found") 
        return jsonify(target_caretaker.animals)  




@zooma_api.route('/employee/<employee_id>')
class deleteEmployee(Resource):
    
    def delete(self,employee_id):
        if len(my_zoo.caretakers)<2:
            return jsonify(f"Add some more caretakers before deleting")
        Guy_That_will_be_kicked  = my_zoo.getCaretaker(employee_id)
        new_employee =my_zoo.getRandomCaretaker(Guy_That_will_be_kicked)
        #my_zoo.getCaretaker(new_employee)
        oldAnimals = Guy_That_will_be_kicked.animals
        if Guy_That_will_be_kicked == None: 
            return jsonify(f"Caretaker with ID {employee_id} was not found") 

        new_employee.takeResponsibility(oldAnimals)
        for x in oldAnimals:
            x.assign_caretaker(new_employee.name)
        my_zoo.kick(Guy_That_will_be_kicked)
        return jsonify(new_employee)

@zooma_api.route('/employees/stats')
class EmployeeStats(Resource):
     def get(self):
        return jsonify(my_zoo.stats())  

@zooma_api.route('/tasks/medical/')
class Medical_plan(Resource):
     def get(self):

        return jsonify(my_zoo.medical())  
    

@zooma_api.route('/tasks/cleaning/')
class CleaningPlan(Resource):
     def get(self):

        return jsonify(my_zoo.cleaning())  

@zooma_api.route('/tasks/feeding/')
class FeedingPlan(Resource):
     def get(self):

        return jsonify(my_zoo.feeding())  

@zooma_api.route('/animals/stat')
class AnimalStats(Resource):
    def get(self):
        
        return jsonify(my_zoo.stat())


 
if __name__ == '__main__':
    zooma_app.run(debug = True, port = 7000)


    