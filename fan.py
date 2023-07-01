Slow = 1
Medium = 2
Fast = 3

class Fan:

    def __init__(self, speed, radius, on, color):
        self.__speed = speed
        self.__is_on = on
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
    
    def get_color(self):
        return self.__color
    
    def set_color(self, new_color):
        if not type(new_color) is str:
            return print("Please give a valid color. Color should be a string.")
        self.__color = new_color
        return print("You have changed the color of your fan to: ", new_color)
        