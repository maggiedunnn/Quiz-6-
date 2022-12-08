class Ambulance:
    """This class will take these attributes

    attributes: priority (is there a patient in the ambulance), speed(maximum speed), capacity(how many people are in it)"""

MyAmbulance = Ambulance()

MyAmbulance.priority = 1
MyAmbulance.speed = 100
MyAmbulance.capacity = 2

import math

def controled_velocity(priority, speed, capacity):
    a = -10*(1 - priority)
    b = 2.37*((speed/10))**3.98
    c = 30*(capacity +1.2)
    result = a + b + c
    print(result)

controled_velocity(MyAmbulance.priority, MyAmbulance.speed, MyAmbulance.capacity)
