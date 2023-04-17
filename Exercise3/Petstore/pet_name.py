class PetName():
    def check_identical_pet_names(pet_list):
        pet_names = []
        repeated_pet_names = []
        count_repetition = 0
        amount_of_repetition = []

        #Creo una lista solo de nombres
        for pet in pet_list:
            pet_name = pet['name']
            pet_names.append(pet_name)
            
        #Ordeno la lista
        pet_names.sort()
        print("sorted pet names", pet_names)

        #Se verifica si el nombre ya se agregó a la lista de repetidos y se suman las repeticiones
        for name in pet_names:
            if pet_names.count(name) > 1 and name not in repeated_pet_names:
                repeated_pet_names.append(name)
                count_repetition = pet_names.count(name)
                #Incluyo en una nueva lista el nombre y su cantidad
                amount_of_repetition.append({name, count_repetition})
 
        if repeated_pet_names:
            print("There are repeated names: ",amount_of_repetition)
            return amount_of_repetition
        else:
            return "There are no repeated pet names in the pet store"
