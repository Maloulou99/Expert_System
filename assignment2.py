#1. Implementation of the expert system algorithm in Python (7 points) 
class RoomSettings():
    def __init__(self, window_number=0, room_occupied=False, room_temperature=0, is_window_open=False, 
                 room_number=0, ventilation_activated=0,weather_outside=0 ):
        self.window_number = window_number
        self.room_occupied = room_occupied
        self.room_temperature = room_temperature
        self.is_window_open = is_window_open 
        self.room_number = room_number
        self.ventilation_activated = ventilation_activated
        self.weather_outside = weather_outside
             
    # Artificial light is switched on in a room when:
    # - The building is open for the specified day and hour
    # - The room is occupied
    # - There is no natural light in room at the specified hour
    def is_light_switched(self, day, hour):
       if self.is_building_open(day, hour) and self.room_occupied and not self.is_neutral_light(hour):
            return True
       else:
            return False
        
    # There is natural light in a room when:
    # - It is morning (hour is between 9 and 16)
    # - The room has at least one window
    def is_neutral_light(self, hour):
        if 9 <= hour <= 16 and self.window_number >= 1:
            return True
        else:
            return False

    # Ventilation is activated in a room when:
    # - The building is open for the specified day and hour
    # - The room is occupied
    # - The room does not have windows or the weather is not mild
    def is_ventilation_activated(self, day, hour):
        if self.is_building_open(day, hour) and self.room_occupied == True and (self.window_number == 0 or not self.is_weather_outside(self.weather_outside) == "mild"):
            return True
        else:
            return False
        
    # Air conditioning is activated in a room when:
    # - The building is open for the specified day and hour
    # - The room is occupied
    # - The weather is hot
    # - Room temperature is above 27 degrees Celsius
    def is_conditioning_activated(self, day, hour):
       if self.is_building_open(day, hour) and self.room_occupied == True and self.is_weather_outside(self.weather_outside) == "hot" and self.room_temperature >= 27:
            return True
       else:
            return False

        
    # Heating is activated in a room when:
    # - The building is open for the specified day and hour
    # - The room is occupied
    # - The weather is cold
    # - Room temperature is below 19 degrees Celsius
    def is_heating_activated(self, day, hour): 
        if self.is_building_open(day, hour) and (self.room_occupied == True) and (self.is_weather_outside(self.weather_outside) == "cold") and self.room_temperature < 19:
            return True
        else:
            return False
        
        
    # Building is open when:
    # - It is work day (day is between Monday and Friday)
    # - It is work time (hour is between 8 and 20)
    def is_building_open(self, day, hour): 
        if (1 <= day <= 5) and (8 <= hour <= 20):
            return True
        else:
            return False

    # Floor alarm is triggered when:
    # - The building is not open
    # - There is a window open in any of the rooms 
    def is_floor_alarm_triggered(self, day, hour):
        if not self.is_building_open(day, hour) and (self.is_window_open and self.room_number >= 1):
            return True
        else:
            return False

    # Building alarm is triggered when:
    # - The building is not open
    # - There is any room that it is occupied 
    def is_building_alarm_triggered(self, day, hour):
        if not self.is_building_open(day, hour) and self.room_occupied == True:
            return True
        else:
            return False

    #It is considered mild weather when temperature is greater than 17C and less than 31C. 
    #It is considered cold weather when temperature is less than or equal to 17C. 
    #It is considered hot weather when temperature is greater than or equal to 31C. 
    def is_weather_outside(self, temperature):
        if temperature <= 17:
            return "cold"
        elif 17 < temperature < 31:
            return "mild"
        else:
            return "hot"

#EXEMPLE 1
room1 = RoomSettings(window_number=2, room_occupied=True, room_temperature=14, is_window_open=True, room_number=1, weather_outside=23)
room2 = RoomSettings(window_number=0, room_occupied=True, room_temperature=25, is_window_open=False, room_number=2, weather_outside=23)
room3 = RoomSettings(window_number=0, room_occupied=False, room_temperature=15, is_window_open=False, room_number=3, weather_outside=23)  

print("Building status:")
print("room1: - Artificial light: {}, Ventilation: {}, Air conditioning: {}, Heating: {}".format(
    "on" if room1.is_light_switched(1, 10) else "off", 
    "on" if room1.is_ventilation_activated(1, 10) else "off", 
    "on" if room1.is_conditioning_activated(1, 10) else "off", 
    "on" if room1.is_heating_activated(1, 10) else "off"))

print("room2: - Artificial light: {}, Ventilation: {}, Air conditioning: {}, Heating: {}".format(
    "on" if room2.is_light_switched(1, 10) else "off", 
    "on" if room2.is_ventilation_activated(1, 10) else "off", 
    "on" if room2.is_conditioning_activated(1, 10) else "off", 
    "on" if room2.is_heating_activated(1, 10) else "off"))

print("room3: - Artificial light: {}, Ventilation: {}, Air conditioning: {}, Heating: {}".format(
    "on" if room3.is_light_switched(1, 10) else "off", 
    "on" if room3.is_ventilation_activated(1, 10) else "off", 
    "on" if room3.is_conditioning_activated(1, 10) else "off",
    "on" if room3.is_heating_activated(1, 10) else "off"))

print("floor1: - Floor alarm: {}".format("on" if room1.is_floor_alarm_triggered(1, 10) else "off"))
print("floor2: - Floor alarm: {}".format("on" if room3.is_floor_alarm_triggered(1, 10) else "off"))
print("Building alarm: - Building alarm: {}".format("on" if room1.is_building_alarm_triggered(1, 10) else "off"))

#EXEMPLE 2
room1 = RoomSettings(window_number=2, room_occupied=True, room_temperature=14, is_window_open=True, room_number=1, weather_outside=12)
room2 = RoomSettings(window_number=0, room_occupied=True, room_temperature=25, is_window_open=False, room_number=2, weather_outside=12)
room3 = RoomSettings(window_number=0, room_occupied=False, room_temperature=15, is_window_open=False, room_number=3, weather_outside=12)  

print("Building status:")
print("room1: - Artificial light: {}, Ventilation: {}, Air conditioning: {}, Heating: {}".format(
    "on" if room1.is_light_switched(1, 10) else "off", 
    "on" if room1.is_ventilation_activated(1, 10) else "off", 
    "on" if room1.is_conditioning_activated(1, 10) else "off", 
    "on" if room1.is_heating_activated(1, 10) else "off"))

print("room2: - Artificial light: {}, Ventilation: {}, Air conditioning: {}, Heating: {}".format(
    "on" if room2.is_light_switched(1, 10) else "off", 
    "on" if room2.is_ventilation_activated(1, 10) else "off", 
    "on" if room2.is_conditioning_activated(1, 10) else "off", 
    "on" if room2.is_heating_activated(1, 10) else "off"))

print("room3: - Artificial light: {}, Ventilation: {}, Air conditioning: {}, Heating: {}".format(
    "on" if room3.is_light_switched(1, 10) else "off", 
    "on" if room3.is_ventilation_activated(1, 10) else "off", 
    "on" if room3.is_conditioning_activated(1, 10) else "off",
    "on" if room3.is_heating_activated(1, 10) else "off"))

print("floor1: - Floor alarm: {}".format("on" if room1.is_floor_alarm_triggered(1, 10) else "off"))
print("floor2: - Floor alarm: {}".format("on" if room3.is_floor_alarm_triggered(1, 10) else "off"))
print("Building alarm: - Building alarm: {}".format("on" if room1.is_building_alarm_triggered(1, 10) else "off"))

#EXEMPLE 3
room1 = RoomSettings(window_number=2, room_occupied=True, room_temperature=14, is_window_open=True, room_number=1, weather_outside=12)
room2 = RoomSettings(window_number=0, room_occupied=True, room_temperature=25, is_window_open=False, room_number=2, weather_outside=25)
room3 = RoomSettings(window_number=0, room_occupied=False, room_temperature=15, is_window_open=False, room_number=3, weather_outside=15) 

print("Building status:")
print("room1: - Artificial light: {}, Ventilation: {}, Air conditioning: {}, Heating: {}".format(
    "on" if room1.is_light_switched(1, 22) else "off", 
    "on" if room1.is_ventilation_activated(1, 22) else "off", 
    "on" if room1.is_conditioning_activated(1, 22) else "off", 
    "on" if room1.is_heating_activated(1, 22) else "off"))

print("room2: - Artificial light: {}, Ventilation: {}, Air conditioning: {}, Heating: {}".format(
    "on" if room2.is_light_switched(1, 22) else "off", 
    "on" if room2.is_ventilation_activated(1, 22) else "off", 
    "on" if room2.is_conditioning_activated(1, 22) else "off", 
    "on" if room2.is_heating_activated(1, 22) else "off"))

print("room3: - Artificial light: {}, Ventilation: {}, Air conditioning: {}, Heating: {}".format(
    "on" if room3.is_light_switched(1, 22) else "off", 
    "on" if room3.is_ventilation_activated(1, 22) else "off", 
    "on" if room3.is_conditioning_activated(1, 22) else "off",
    "on" if room3.is_heating_activated(1, 22) else "off"))

print("floor1: - Floor alarm: {}".format("on" if room1.is_floor_alarm_triggered(1, 22) else "off"))
print("floor2: - Floor alarm: {}".format("on" if room3.is_floor_alarm_triggered(1, 22) else "off"))
print("Building alarm: - Building alarm: {}".format("on" if room1.is_building_alarm_triggered(1, 22) else "off"))


#3. Visualization (2 points, optional) 
class Building():
    def __init__(self, floors):
        self.floors = floors

    def visualize_building(self):
        print("Building Visualization:")
        for floor_num, floor in enumerate(self.floors, start=1):
            print(f"Floor {floor_num}:")
            for room_num, room in enumerate(floor, start=1):
                print(f"\tRoom {room_num}:")
                print(f"\t\tOccupied: {room.room_occupied}")
                print(f"\t\tWindow Count: {room.window_number}")
                print(f"\t\tWindow Status: {'Open' if room.is_window_open else 'Closed'}")
                print(f"\t\tRoom Temperature: {room.room_temperature}C")
                print(f"\t\tWeather Outside: {room.weather_outside}C")


#EXEMPLE 1

room1_1 = RoomSettings(window_number=2, room_occupied=True, room_temperature=14, is_window_open=True, room_number=1, weather_outside=23)
room2_1 = RoomSettings(window_number=0, room_occupied=True, room_temperature=25, is_window_open=False, room_number=2, weather_outside=23)
room3_1 = RoomSettings(window_number=0, room_occupied=False, room_temperature=15, is_window_open=False, room_number=3, weather_outside=23)

floors_1 = [
    [room1_1, room2_1],  # Floor 1
    [room3_1]            # Floor 2
]

building_1 = Building(floors_1)

building_1.visualize_building()
print()

#EXEMPLE 2
room1_2 = RoomSettings(window_number=2, room_occupied=True, room_temperature=14, is_window_open=True, room_number=1, weather_outside=12)
room2_2 = RoomSettings(window_number=0, room_occupied=True, room_temperature=25, is_window_open=False, room_number=2, weather_outside=12)
room3_2 = RoomSettings(window_number=0, room_occupied=False, room_temperature=15, is_window_open=False, room_number=3, weather_outside=12)

floors_2 = [
    [room1_2, room2_2], 
    [room3_2]            
]

building_2 = Building(floors_2)

building_2.visualize_building()
print()


#EXEMPLE 3
room1_3 = RoomSettings(window_number=2, room_occupied=True, room_temperature=14, is_window_open=True, room_number=1, weather_outside=12)
room2_3 = RoomSettings(window_number=0, room_occupied=True, room_temperature=25, is_window_open=False, room_number=2, weather_outside=25)
room3_3 = RoomSettings(window_number=0, room_occupied=False, room_temperature=15, is_window_open=False, room_number=3, weather_outside=15)

floors_3 = [
    [room1_3, room2_3],  
    [room3_3]             
]

building_3 = Building(floors_3)

building_3.visualize_building()


#Interaction with the User 
room_user = input("In which room are you?")
window_user = int(input("How many windows are in the room?"))

def is_window(window_user):
    if window_user >= 1: 
        return True
    else: 
        return False


def window_true(window_user):
    if window_user >= 0:
        window_user = input("How many windows are open?") 
        return int(window_user)
    else:
        window_user = False 
        return int(window_user)

print(window_true(window_user))

room_occupied_user = input("Is the room occupied? please answer with: Yes or No")

room_temperature_user = int(input("What is the temperature of the room?"))
change_room_temperature = input("Do you want to change the room temperature? please answer with: Yes or No")




    

