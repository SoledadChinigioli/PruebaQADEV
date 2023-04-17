from pet import Pet
from pet_name import PetName


def main():
    sold_pets = Pet.get_sold_pets()
    PetName.check_identical_pet_names(sold_pets)

if __name__ == '__main__':
    main()