class Car:

    def __init__(self, make, year_model):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed = self.__speed + 5
        return
    
    def brake(self):
        self.__speed = self.__speed - 5
        return
    
    def get_speed(self):
        return self.__speed, self.__year_model, self.__make