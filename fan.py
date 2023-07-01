Slow = 1
Medium = 2
Fast = 3

class Fan:

    def __init__(self, speed, radius, is_on, color):
        self.__speed = speed
        self.__is_on = is_on
        self.__color = color
        self.__radius = radius
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, new_speed):
        if new_speed.lower() is 'slow':
            self.__speed = Slow
            print("Your fan speed is set to 'SLOW'!")
        if new_speed.lower() is 'medium':
            self.__speed = Medium
            print("Your fan speed is set to 'MEDIUM'!")
        if new_speed.lower() is 'fast':
            self.__speed = Fast
            print("Your fan speed is set to 'FAST'!")
        else:
            print("Invalid input. Your input must be 'slow', 'medium', or 'fast'.")
    
        