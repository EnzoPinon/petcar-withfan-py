from car import Car

#create new car
my_car = Car("Isuzu Fuego", 2009)

##accelerate five times. To make it quick, make a loop.
first_loop = 0

while not first_loop is 5:
    my_car.accelerate()
    first_loop = first_loop + 1

#show speed
details = my_car.get_speed()
print("The speed of my", details[1], details[2], 'is currently at: ', details[0])