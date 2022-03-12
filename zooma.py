from flask import Flask, jsonify
from flask_restx import Api, reqparse, Resource
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
        args = homie.parse_args()
        enclosure_id = args['Enclosure ID']
        

         
        targeted_animal  = my_zoo.getAnimal(animal_id)
        if not targeted_animal: 
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
        AnimalChild = motherAnimal.birth()
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


        

     
if __name__ == '__main__':
    zooma_app.run(debug = True, port = 7000)


    