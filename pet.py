class Pet:

    def __init__(self):
        self.__type = 'type'
        self.__name = 'name'
        self.__age = 0
    
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if not type(new_age) is int:
            return print("Your pet's new age must be an integer variable.")
        self.__age = new_age
        print ("Your pet's age has been changed to: ", new_age)
    
    def get_type(self):
        return self.__type
    
    def set_type(self, new_type):
        if not type(new_type) is str:
            return print("Thus method 'set_type' only accepts string variables.")
        self.__type = new_type
        return print("Your pet's species is now a: ", new_type)
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        if not type(new_name) is str:
            return print("Thus method 'set_type' only accepts string variables.")
        self.__name = new_name
        return print("Your pet's name is now: ", new_name)
