from VirtualCopernicus.VirtualCopernicusNG import TkCircuit
import pyowm
# initialize the circuit inside the

configuration = {
    "name": "CopernicusNG Weather Forecast",
    "sheet": "sheet_forecast.png",
    "width": 343,
    "height": 267,

    "servos": [
        {"x": 170, "y": 150, "length": 90, "name": "Servo 1", "pin": 17}
    ],
    "buttons": [
        {"x": 295, "y": 200, "name": "Button 1", "pin": 11},
        {"x": 295, "y": 170, "name": "Button 2", "pin": 12},
    ]
}

circuit = TkCircuit(configuration)

KEY = "4526d487f12ef78b82b7a7d113faea64"
OWM = pyowm.OWM(KEY)

status_to_angle = {
    'Thunderstorm': 70,
    'Drizzle': 40,
    'Rain': 50,
    'Snow': 60,
    'Clouds': 20,
    'Mist': 10,
    'Smoke': 10,
    'Dust': 10,
    'Haze': 10,
    'Fog': 10,
    'Ash': 10,
    'Squall': 70,
    'Tornado': 80,
    'Clear': -70
}

location_map = {
    'Krakow': 'Istanbul',
    'Istanbul': 'Stockholm',
    'Stockholm': 'Madrid',
    'Madrid': 'Krakow'
}

current_location = 'Krakow'


def set_angle(location):
    weather_status = OWM.weather_manager().weather_at_place(location).weather.status
    return status_to_angle[weather_status]


def change_location():
    global current_location
    current_location = location_map[current_location]
    print("Current location: " + current_location)


@circuit.run
def main():
    from time import sleep
    from gpiozero import AngularServo, Button

    servo1 = AngularServo(17, min_angle=-90, max_angle=90)
    button1 = Button(12)

    button1.when_activated = change_location

    while True:
        servo1.angle = set_angle(current_location)
        sleep(0.1)