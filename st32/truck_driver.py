# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:48:00 2018

@author: Владимир
"""

from .truck import Truck

class Truck_driver(Truck):

    def __init__(self):
        Truck.__init__(self)

    
    def input_data(self):
        Truck.input_data(self)
        print("Insert information about driver")
        self.firstname = input("Insert firsntame: ",)
        self.lastname = input("Insert lastname: ",)
        self.age = input("Insert age: ",)
        self.category = input("Insert category: ",)
        self.phone_number = input("Insert phone number: ",)
    def show_data(self):
        print("\nModel of truck: {}\nSerial number: {}\nCarrying: {}\nMileage: {}\nDriver's info:\nFirstname: {}\nLastname: {}\nAge: {}\nCategory: {}\nPhone number:{}\n".format(self.truck_model,self.serial_number,self.carrying,self.mileage,self.firstname,self.lastname,self.age,self.category,self.phone_number))
