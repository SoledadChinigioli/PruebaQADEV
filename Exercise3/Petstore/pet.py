import requests
import json

class Pet():
    def get_sold_pets():

        URL = 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'
        response = requests.get(URL, verify=False) #Hack para problema con SSL

        if response.status_code == 200:
            data = json.loads(response.text)
            pets = []
            for pet in data:
                pet_id = pet['id']
                if 'name' not in pet:
                    pet_name = "made up name"
                else:
                    pet_name = pet['name']
                pets.append({"id": pet_id, "name": pet_name})

        else:
            print(f"Error on HTTP request. Code response: {response.status_code}")
            pets = []

        return pets


