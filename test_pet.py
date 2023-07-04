from pet import Pet

my_pet = Pet()

print("Let's get you a pet!")
# ask new name
new_name = input("What will be the name of your pet: ")
#get and set name
my_pet.get_name()
my_pet.set_name(new_name)

# ask new typw
new_type = input("What will be your pet's species: ")

# get and set type
my_pet.get_type()
my_pet.set_type(new_type)

#ask the pet age
new_age = input("Lastly, how old will your pet be: ")

#get and set age
my_pet.get_age()

my_pet.set_age(int(new_age))

# show your pet's new name~

name = my_pet.get_name()
age = my_pet.get_age()
species = my_pet.get_type()

print("--------------------Pet Information--------------------")
print("Name of pet:", name, "\nSpecies of pet:", species, "\nAge of pet:", age)
print("-------------------------------------------------------")