#Expert-System

import datetime

def building_open(day,hour): 
#building is open: Monday- Friday and between 8 and 20
    if day.weekday() < 5 and 8 <= hour <= 20:
        return True 
    else: 
        return False 
    
def weather_outside(grados):
    if grados <= 17:
        return "cold"
    elif 17 < grados < 31:
        return "mild"
    else:
        return "hot"


class room_settings():
    def __init__(self,window_number =0, window_open=False, lights_on=False, room_occupied=False, ventilation_activated = False, room_temperature = 0, conditioning_activated = False, weather = 0, heating_activated = False):
        self.window_number = window_number
        self.window_open = window_open
        self.lights_on = lights_on 
        self.room_occupied = room_occupied
        self.ventilation_activated = ventilation_activated
        self.conditioning_activated = conditioning_activated
        self.room_temperature = room_temperature 
        self.heating_activated = heating_activated 

def ventilation_activated(self, day, hour):
    if building_open(day,hour) and self.room_occupied and (self.windows_number == 0 or weather_outside != "mild"):
        return True 
    else: 
        return False 

def conditioning_activated(self, day, hour):
    if building_open(day,hour) and self.room_occupied and self.room_temperature > 27 and weather_outside == "hot" :
        return True 
    else: 
        return False 


def heating_activated(self,day,hour): 
    if building_open(day,hour) and self.room_occupied and self.room_temperature < 19 and weather_outside == "cold" :
        return True 
    else: 
        return False 
