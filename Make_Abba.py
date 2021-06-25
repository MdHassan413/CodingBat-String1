# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".


# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

name_a = input("Enter Your Name : ")
name_b = input("Enter Your Name : ")
print(name_a + " " + name_b + " " + name_b + " "  +name_a)