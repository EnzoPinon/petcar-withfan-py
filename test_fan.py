from fan import Fan
# CREATE DEFAULT FAN 01
# ASSIGN FAST 10 YELLOW ON
# CREATE DEFAULT FAN 02
# ASSIGN MEDIUM 5 BLUE OFF
# DISPLAY BOTH (need new function for this.)

fan_01 = Fan.fan_construct


# assign the requested fan settings
fan_01.get_speed 
fan_01.set_speed('fast')
fan_01.get_color
fan_01.set_color('Yellow')
fan_01.get_radius
fan_01.set_radius(10)
fan_01.get_status
fan_01.set_status('on')

#view first fan as test.
fan_01.fan_view()