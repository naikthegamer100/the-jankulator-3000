#!/usr/bin/env python3

#coments go here btw
#https://github.com/naikthegamer100/the-jankulator-3000
#i made a git hub
#how do you turn an string into an iteger

#string = int(string)


print("      main menu")
print("-------------------")
print("¦0= calc          ¦")
print("¦1= disclaimers   ¦")
print("¦2=exit           ¦")
print("¦                 ¦")
print("-------------------")
menu = input()

if menu == "0":
    print("welcome to the jankulator 300")

elif menu == "1":
    print("pree warning pleas do NOT use decimals.")
    print (" do NOT * or / by 10,100,1000...")
    print(" ")
    print(" ")
    print(" ")



print("Enter first number")
number = input()
# alows the abilty to add an imput
print(
    "You entered " + number +
    " What operation would you like to use 0 for addition 1 for subtraction 2 for multipcation 3 for division"
)

operation = input()
# alows to sulect the operation Type

print("You entered " + operation +
      ". What number should this term be applied to?")
num = input()

number = int(number)

number = int(num)

if operation == "0":
    # addition
    sum = int(number) + int(num)
    print(sum)

elif operation == "1":
    #subtraction
    sum = int(number) - int(num)
    print(sum)

elif operation == "2":
    #multipcation
    sum = int(number) * int(num)
    print(sum)

elif operation == "3":
    #division
    sum = int(number) / int(num)
    print(sum)
else:
    print("input error")
