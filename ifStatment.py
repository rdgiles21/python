"""
this function will return whether the heat or air conditioning is on based on the temperature outside (temp) and the temperature inside (thermo) and what the desired temp
is (thermo_set). based on what actual temperatures the heat or AC will display as on. if neither of these are on it will return "current temperature is ideal"
feel free to play with the temperature settings


"""
# here are the temperature variables to change
temp = 60
thermo = 70
thermo_set = 85


heat = False
cooling = False



if thermo_set <= temp >= thermo and heat == False:
    heat = True
    print("Heat is now on")
    print(heat)

elif thermo_set >= temp <= thermo and cooling == False:
    cooling = True
    print("AC is now on")
    print(cooling)
    
else:
    print("Current temperature is ideal")
        
