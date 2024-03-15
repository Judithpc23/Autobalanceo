
import os
import numpy as np 

from PIL import Image



print("VECTOR CON NOMBRES DE ")
Bike = 'Data/Bike'
with os.scandir(Bike) as Bikes:
    Bikes = [Bike.name for Bike in Bikes if Bike.is_file()]
print(Bikes)



Car = 'Data/cars'
with os.scandir(Car) as Cars:
    Cars = [Car.name for Car in Cars if Car.is_file()]
print(Cars)

