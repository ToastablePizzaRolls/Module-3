"""
File: Module 3 Lab CS.py
Author: Antonio Garcia Hernandez
Date: September 16, 2025
Description: This script creates a super class called vehicle() which has different vehicle typpes
It presets the vehicle type as "car" then takes user imput for specified details. after
user input it displays the details entered in a vertical easy to read format.
"""



###Super duper class
class Vehicle():
    def __init__(self, vehicle_type = "vehicle"):
        self.vehicle_type = vehicle_type

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type
##Vehicle type attributes
vtype = Vehicle("Vehicle Types")
vtype.car = "car"
vtype.truck = "truck"
vtype.boat = "boat"
vtype.plane = "plane" 
vtype.broomstick = "broomstick"

###Creating Da Automobile Class
class Automobile():
    def __init__(self):
        super().__init__()
        self.vehicle_type = vtype.car
        self.year = None
        self.make = None
        self.model = None
        self.doors = None
        self.roof = None

    def set_attributes(self, year, make, model, doors, roof):
        ##Attributions
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

 ###Displaying the deats
    def display_usr_Info(self):
        print("---Car Details---")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Doors: {self.doors}")
        print(f"Roof: {self.roof}")

def main():

    da_car = Automobile()

###Getting the deats
    print("Please Provide the following info:")
    da_car.year = input("Please input the year: ")
    da_car.make = input("Please input the Make: ")
    da_car.model = input("Please input the Model: ")
    da_car.doors = input("Does the car have 2 or 4 doors? ")
    da_car.roof = input("Does the car have a solid or sun roof? ")

    da_car.display_usr_Info()


main()

