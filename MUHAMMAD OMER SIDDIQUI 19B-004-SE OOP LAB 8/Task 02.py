# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 03:07:29 2020

@author: Muhammad Omer
"""

from abc import ABC, abstractmethod

class Bank(ABC):
    def AccountName(self):
        pass
    def RateOfInterest(self):
        pass
    def Deposit(self):
        pass
    def Withdraw(self):
        pass
    
class Habib(Bank):
    def Name(self):
        print("Habib Bank Limited")
    def AccountName(self):
        print("Account Name: 7883-98765432")
    def RateOfInterest(self):
        print("Interest Rate: 25%")
    def Deposit(self):
        print("Deposit: 27000")
    def Withdraw(self):
        print("Withdraw: 3000")
        
class Metro(Bank):
    def Name(self):
        print("Metro Bank Limited")
    def AccountName(self):
        print("Account Name: 8772-09876373")
    def RateOfInterest(self):
        print("Interest Rate: 15%")
    def Deposit(self):
        print("Deposit: 13000")
    def Withdraw(self):
        print("Withdraw: 3500")
        
class National(Bank):
    def Name(self):
        print("National Bank")
    def AccountName(self):
        print("Account Name: 8877-091122445")
    def RateOfInterest(self):
        print("Interest Rate: 30%")
    def Deposit(self):
        print("Deposit: 220000")
    def Withdraw(self):
        print("Withdraw: 45000")
        
        
        
m1= Habib()
m1.Name()
m1.AccountName()
m1.RateOfInterest()
m1.Deposit()
m1.Withdraw()   
print(36*'_')
a1= Metro()
a1.Name()
a1.AccountName()
a1.RateOfInterest()
a1.Deposit()
a1.Withdraw()   
"\n""\n"
a2= National()
a2.Name()
a2.AccountName()
a2.RateOfInterest()
a2.Deposit()
a2.Withdraw()  