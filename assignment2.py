#Expert-System

import datetime


    
def weather_outside(grados):
    if grados <= 17:
        return "cold"
    elif 17 < grados < 31:
        return "mild"
    else:
        return "hot"




class RoomSettings():
    def __init__(self, window_number=0, room_occupied=False, room_temperature=0, 
                 neutral_light=False, building_open=False, is_window_open=False, 
                 room_number=0, ventilation_activated=False):
        self.window_number = window_number
        self.room_occupied = room_occupied
        self.room_temperature = room_temperature
        self.neutral_light = neutral_light
        self.building_open = building_open
        self.is_window_open = is_window_open 
        self.room_number = room_number
        self.ventilation_activated = ventilation_activated


#Artificial light is switched on in a room when - 
#The building is open for the specified day and hour - 
#The room is occupied - There is no natural light in room at the specified hour 
def is_light_switched(self, day, hour):
    if self.building_open(day,hour) and self.room_occupied and self.netrual_light(day, hour) != "No netrual lights":
        return True
    else:
        return False


#Ventilation is activated in a room when - 
#The building is open for the specified day and hour - 
#The room is occupied - The room does not have windows or the weather is not mild
def is_ventilation_activated(self, day, hour):
        if self.building_open and self.room_occupied and (self.window_number == 0 or weather_outside(self.room_temperature) != "mild"):
            return True 
        else: 
            return False 

#Air conditioning is activated in a room when - 
#The building is open for the specified day and hour - The room is occupied - 
#The weather is hot - Room temperature is above 27 degrees Celsius 
def is_conditioning_activated(self, day, hour):
    if self.building_open(day,hour) and self.room_occupied and self.room_temperature > 27 and weather_outside == "hot" :
        return True 
    else: 
        return False 

#Heating is activated in a room when - The building is open for the specified day and hour - 
#The room is occupied - The weather is cold - 
#Room temperature is below 19 degrees Celsius 
def is_heating_activated(self,day,hour): 
    if self.building_open(day,hour) and self.room_occupied and self.room_temperature < 19 and weather_outside == "cold" :
        return True 
    else: 
        return False 
    
#There is natural light in a room when - 
#It is morning (hour is between 9 and 16) -
#The room has at least one window   
def is_natural_light(self, hour):
    if self.netrual_light(hour >= 9 and hour <= 16) and self.window_number >= 1:
        return True
    else:
        return False

#Building is open when - 
#It is work day (day is between Monday and Friday) - 
#It is work time (hour is between 8 and 20) 
def is_building_open(day,hour): 
    if day.weekday() < 5 and 8 <= hour <= 20:
        return True 
    else: 
        return False 

#Floor alarm is triggered when -
#The building is not open - There is a window open in any of the rooms 
def is_floor_alarm_triggered(self):
    if self.building_open == False and self.is_window_open == True and self.room_number >= 1:
        return True
    else:
        return False

#Building alarm is triggered when - 
#The building is not open - There is any room that it is occupied 
def is_building_alarm_triggered(self):
    if self.building_open == False and self.room_occupied == True:
        return True
    else:
        return False
    
# Example usage:
# Create a RoomSettings object
room1 = RoomSettings(window_number=1, room_temperature=20, room_occupied=True)

# Get the current date and time
now = datetime.datetime.now()

# Check if ventilation is activated for room1
ventilation_activated = room1.is_ventilation_activated(now, now.hour)
print("Ventilation activated:", ventilation_activated)

# Check if conditioning is activated for room1
conditioning_activated = room1.is_conditioning_activated(now, now.hour)
print("Conditioning activated:", conditioning_activated)

# Check if heating is activated for room1
heating_activated = room1.is_heating_activated(now, now.hour)
print("Heating activated:", heating_activated)