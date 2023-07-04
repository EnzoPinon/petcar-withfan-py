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
        if not type(new_speed) is int:
            return print("Input must be an integer between 1-3.")
        if new_speed is 1:
            self.__speed = Slow
            return print("Speed changed to SLOW!")
        if new_speed is 2:
            self.__speed = Medium
            return print("Speed changed to MEDIUM!")
        if new_speed is 3:
            self.__speed = Fast
            return print("Speed changed to FAST!")
        else:
            return print("Input must be an integer between 1-3.")
    
    def get_color(self):
        return self.__color
    
    def set_color(self, new_color):
        if not type(new_color) is str:
            return print("Please give a valid color. Color should be a string.")
        self.__color = new_color
        return print("You have changed the color of your fan to: ", new_color)
    
    def get_status(self):
        return self.__is_on
    
    def set_status(self, new_status):
        if not type(new_status) is str:
            return print("This function 'set_status' only accepts string inputs.")
        if new_status is 'on':
            self.__is_on = True
            return print("This fan has been switched on!")
        if new_status is 'off':
            self.__is_on = False
            return print("This fan has been switched off!")
        else:
            return print("Please say if this fan will be switched 'on' or 'off'.")
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, new_radius):
        try:
            setting = float(new_radius)
        except TypeError:
            return print("This function 'set_radius' only accepts integers and decimals.")
        self.__radius = setting
        return print("The fan's radius has been set to: ", setting)
    
    def fan_construct(self):
        new_fan = Fan(Slow, 5, False, "blue")
        print("New fan made!")
        return new_fan

    def fan_view(self):
        print("--------------------Fan Info--------------------")
        print("Fan color: ", self.__color, '\nFan radius: ', self.__radius)
        if self.__speed is Slow:
            print("Fan speed: Slow")
        if self.__speed is Medium:
            print("Fan speed: Medium")
        if self.__speed is Fast:
            print("Fan speed: Fast")
        print("Is the fan on: ", self.__is_on)
        print('------------------------------------------------')