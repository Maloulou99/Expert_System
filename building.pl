%2. Implementation of the expert system algorithm in Prolog (1 points, optional) 
% Facts
is_building_open(Day, Hour) :- 
    between(1, 5, Day), 
    between(8, 20, Hour).

is_weather_outside(Weather, mild) :- Weather > 17, Weather < 31.
is_weather_outside(Weather, cold) :- Weather =< 17.
is_weather_outside(Weather, hot) :- Weather >= 31.

% Rules
is_light_switched(Day, Hour, WindowNumber, RoomOccupied, RoomTemperature, IsWindowOpen, WeatherOutside) :-
    is_building_open(Day, Hour),
    RoomOccupied == true,
    \+ is_neutral_light(Hour, WindowNumber),
    is_weather_outside(WeatherOutside, _).

is_neutral_light(Hour, WindowNumber) :-
    between(9, 16, Hour),
    WindowNumber >= 1.

is_ventilation_activated(Day, Hour, WindowNumber, RoomOccupied, WeatherOutside) :-
    is_building_open(Day, Hour),
    RoomOccupied == true,
    (WindowNumber == 0 ; \+ is_weather_outside(WeatherOutside, mild)).

is_conditioning_activated(Day, Hour, RoomOccupied, WeatherOutside, RoomTemperature) :-
    is_building_open(Day, Hour),
    RoomOccupied == true,
    is_weather_outside(WeatherOutside, hot),
    RoomTemperature >= 27.

is_heating_activated(Day, Hour, RoomOccupied, WeatherOutside, RoomTemperature) :-
    is_building_open(Day, Hour),
    RoomOccupied == true,
    is_weather_outside(WeatherOutside, cold),
    RoomTemperature < 19.

is_floor_alarm_triggered(Day, Hour, IsBuildingOpen, IsWindowOpen, RoomNumber) :-
    \+ IsBuildingOpen,
    IsWindowOpen == true,
    RoomNumber >= 1.

is_building_alarm_triggered(Day, Hour, IsBuildingOpen, RoomOccupied) :-
    \+ IsBuildingOpen,
    RoomOccupied == true.
