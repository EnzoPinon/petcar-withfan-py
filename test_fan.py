from fan import Fan
Slow = 1
Medium = 2
Fast = 3

#Making a random fan, which will be fan 01.
fan_01 = Fan(Slow, 5, False, 'white')

# update the info of the fan to the default.
fan_01.fan_construct
# assign the requested fan settings
# ASSIGN FAST 10 YELLOW ON
fan_01.get_speed 
fan_01.set_speed(Fast)
fan_01.get_color
fan_01.set_color('Yellow')
fan_01.get_radius
fan_01.set_radius(10)
fan_01.get_status
fan_01.set_status('on')

# let's make the same fan, but this time we update it to the settings of fan 02.

fan_02 = Fan(Slow, 5, False, 'white')

fan_02.fan_construct

# ASSIGN MEDIUM 5 BLUE OFF
fan_02.get_speed 
fan_02.set_speed(Medium)
fan_02.get_color
fan_02.set_color('Blue')
fan_02.get_radius
fan_02.set_radius(5)
fan_02.get_status
fan_02.set_status('off')

#Display the details of both fans.
fan_01.fan_view()
fan_02.fan_view()