% Facts about rooms
room(room1, 2, true, 14, true).
room(room2, 0, true, 25, false).
room(room3, 0, false, 15, false).

% Rules for room status
% Rule for artificial light
is_artificial_light_on(Room) :-
    room(Room, _, _, _, ArtificialLight),
    ArtificialLight = true.

% Rule for ventilation
is_ventilation_on(Room) :-
    room(Room, _, _, _, _, Ventilation),
    Ventilation = true.

% Rule for air conditioning
is_air_conditioning_on(Room) :-
    room(Room, _, _, _, _, _, AirConditioning),
    AirConditioning = true.

% Rule for heating
is_heating_on(Room) :-
    room(Room, _, _, _, _, _, _, Heating),
    Heating = true.

% Rule for window status
is_window_open(Room) :-
    room(Room, _, _, _, _, _, _, _, _, Window),
    Window = true.

% Rule for room temperature
room_temperature(Room, Temperature) :-
    room(Room, _, _, _, _, _, _, Temperature, _).

% Rule for determining if a room alarm is triggered
is_room_alarm_triggered(Room) :-
    is_window_open(Room),
    room_temperature(Room, Temperature),
    Temperature > 20.
