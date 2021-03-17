#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse
from recomendations import *
from functions import *

#username = input("Enter username:")
#print("Username is: " + username)
#a="""""";
#print(a)
dash = '---'
dash_n = 40

print("");
print(dash*dash_n)
print('\033[96m')
print("Welcome To The Security Recomendation Questionnaire.")
print("This Is The Self Assessment Guide Line For Web Application Vulnerability. Which Helps You To Take Further Actions.")
print("There are total " + str(len(recomendations))+ " Questions, Please Answer them in Y|N")
print("Version:1.0 March2021")
print('\033[96m')
print(dash*dash_n)
print("");
logstr("start")
print("\033[99m")
total_questions =len(recomendations)
number=1
sav_weightage = 0
toal_applicable =0
for recomendation in recomendations:
    print("{}Category        : {}{}".format('\033[97m','\033[97m',recomendation[0]))
    print("{}Question-{}      : {}{}".format('\033[97m',number,'\033[97m',recomendation[1]))
    print("{}Weightage       : {}{}".format('\033[97m','\033[97m',recomendation[4] + " Out Of 1000"))
    answer = input('\033[97m' + "Press Y or Enter to answer Yes or N for No?" + '\033[97m')
    
    if(answer == "Y" or answer == "y" or answer == ""):
        print("{}recomendation   : {}{}".format('\033[93m','\033[93m',recomendation[2]))
        print("{}Review          : {}{}".format('\033[93m','\033[93m',recomendation[5]))
        logstr("Review:"+recomendation[5])
        sav_weightage +=int(recomendation[4])
        toal_applicable +=1
        print("")
        logstr("[Q"+str(number)+"]"+recomendation[1]+"[A]Y")
    
    else:
        logstr("[Q"+str(number)+"]"+recomendation[1]+"[A]"+answer)
    
    number +=1

print("{}{}{}".format('\033[97m',dash*dash_n,'\033[97m'))
print("{}severity weighting is   : {}{}".format('\033[91m','\033[91m',sav_weightage))
print("{}Applicable recomendations are   : {}{}".format('\033[91m','\033[91m',toal_applicable))
print("{}{}{}".format('\033[97m',dash*dash_n,'\033[97m')) 
helpful = input('\033[97m' + "Is this helpful to you ?(Y|N|Type Your Suggation)" + '\033[97m')

while helpful == "":
  print("\033[97m"+"Please Submit the Answer."+"\033[97m")
  helpful = input('\033[97m' + "Is this helpful to you ?(Y|N|Type Your Suggation)" + '\033[97m')

print("\033[97m"+"Thanks For Your Answer, We Are Working Hard To Improve It."+"\033[97m")
logstr("helpful:"+helpful)

print(""); 
print("\033[97m"+"Thank you for your submission.Kindly Work on Recomendation."+"\033[97m")
print(""); 
print(""); 
