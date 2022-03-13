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
        new_animal = Animal (species, name, age) 
        #add the animal to the zoo
        my_zoo.addAnimal (new_animal) 
        return jsonify(new_animal) 
    

@zooma_api.route('/animal/<animal_id>')
class Animal_ID(Resource):
     def get(self, animal_id):
        search_result  = my_zoo.getAnimal(animal_id)
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
        
        targeted_animal.home(enclosure_id)
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
hello.add_argument('Animal_ID', type=str, required=True)       
@zooma_api.route('/animal/death')
class AnimalDie(Resource):
    @zooma_api.doc(parser=hello)
    def post(self):
        args = hello.parse_args()
        animal_id = args["Animal_ID"]         
        animal_id  = my_zoo.getAnimal(animal_id)
        if not animal_id: 
            return jsonify(f"Animal with ID {animal_id} was not found") 
        
        #need to return the child not parent = find a way
        my_zoo.animal_die(animal_id)
        animal_id.die()
        return jsonify(animal_id)

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


@zooma_api.route('/employee')
class AddCaretaker(Resource):
    @zooma_api.doc(parser=caretaker_parser)
    def post(self):
        # get the post parameters 
        args = caretaker_parser.parse_args()
        address = args['address']
        name = args['name']
        
        
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
        targeted_caretaker = my_zoo.getCaretaker(employee_id)
        if targeted_animal == None: 
            return jsonify(f"Animal with ID {animal_id} was not found") 
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
    

     
if __name__ == '__main__':
    zooma_app.run(debug = True, port = 7000)


    