# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 03:11:51 2020

@author: Muhammad Omer
"""

from abc import ABC, abstractmethod

class SmartPhone(ABC):
    def Price(self):
        pass
    def YearOfInvention(self):
        pass
    def RefreshRate(self):
        pass

class Samsung(SmartPhone):
    def Name(self):
        print("Samsung S7")
    def Price(self):
        print("Price: 63000")
    def YearOfInvention(self):
        print("Year Of Invention: 2016")
    def RefreshRate(self):
        print("Refresh Rate: 120 Hz")
        
class Iphone(SmartPhone):
    def Name(self):
        print("Iphone 7 Plus")
    def Price(self):
        print("Price: 30000")
    def YearOfInvention(self):
        print("Year Of Invention: 2015")
    def RefreshRate(self):
        print("Refresh Rate:  60 Hz up to 240 Hz")
        
        
o1= Samsung()
o1.Name()
o1.Price()
o1.YearOfInvention()
o1.RefreshRate()
print(36*'_')
l1= Iphone()
l1.Name()
l1.Price()
l1.YearOfInvention()
l1.RefreshRate()