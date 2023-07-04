from fan import Fan
Slow = 1
Medium = 2
Fast = 3
# ASSIGN FAST 10 YELLOW ON
# CREATE DEFAULT FAN 02
# ASSIGN MEDIUM 5 BLUE OFF
# DISPLAY BOTH (need new function for this.)

#Making a random fan, which will be fan 01.
fan_01 = Fan(Slow, 5, False, 'white')

fan_01.fan_view()
# update the info of the fan to the default.
fan_01.fan_construct
# assign the requested fan settings
fan_01.get_speed 
fan_01.set_speed(Fast)
fan_01.get_color
fan_01.set_color('Yellow')
fan_01.get_radius
fan_01.set_radius(10)
fan_01.get_status
fan_01.set_status('on')

#view first fan as test.
fan_01.fan_view()