# x = 'Pluto is a Planet'
# y = "Pluto is a Planet"
# print(x==y)


# spam_amount=0
# print(spam_amount)
# spam_amount = spam_amount+4
# if spam_amount>0:
#     print("But i dont want any spam")
# viking_song = "spam "* spam_amount
# print(viking_song)


# hat_height_cm=25
# my_height_cm=190
# total_height_meters = (hat_height_cm + my_height_cm) /100
# print("Height in meters =",total_height_meters,"?")


# print(min(1,2,3))
# print(max(1,2,3))


# print(float(10))
# print(int(3.33))
# print(int('807')+1)


# x=True
# print(x)
# print(type(x))


# def can_run_for_president(age):
#     return age>=35
# print("Can a 19-year old run for president?", can_run_for_president(19))
# print("Can a 19-year old run for president?", can_run_for_president(45))


# def inspect(x):
#     if x==0:
#         print(x,"is zero")
#     elif x>0:
#         print(x,"is positive")
#     elif x<0:
#         print(x,"is negative")
#     else:
#         print(x,"is unlike anything i've ever seen....")
# inspect(0)
# inspect(-15)


# planets = ['mercury','venus','earth','Mars','Juptier','Saturn','Uranus','Neptune']
# print(planets[1])
# for planet in planets:
#     print(planet,end=' ')


# for i in range(5):
#     print("Doing important work i=",i)


# i=0
# while i<10:
#     print(i,end=' ')
#     i+=1


# hello = """hello
# world"""
# print(hello)


# planet = 'Pluto'
# print(planet[0])
# numbers = [1,2,3,4,5,6]
# numbers = [1,2,3,4,5,6,["A","B"]]
# print(numbers[6][1])
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.append(100)
# print(numbers)
# numbers.clear()
# print(5 in numbers)
# print(10 not in numbers)
# numbers.remove(3)
# numbers.pop()  //remove last element
# del numbers[1]


# numberList = [1,1]
# numbersSet = {1,1}
# letterSet = {"A", "A", "B", "C", "C"}
# print(numberList)  #order is gurantee
# print(numbersSet)  #don't print repeated number
# print(letterSet)   #order is not allowed


# Union
# lettersA = {"A", "B", "C", "D"}
# lettersB = {"A", "B", "E", "F"}
# union = lettersA | lettersB
# print(f"union = {union}")
# #Intersection
# intersection = lettersA & lettersB
# print(f"intersection = {intersection}")
# #Difference
# difference = lettersA - lettersB
# print(f"difference = {difference}")


# Dictionaries
# person = {
#     "name" : "Eslam",  #Key is Unique
#     "age" : 25,
#     "address" : "Egypt"
# }
# print(person["name"])
# print(person["age"])
# print(person["address"])
# print(person.keys())
# print(person.values())
# print(person.get("age"))
# person["age"] = 100
# print(person.get("age"))
# person.clear()
# print(person)


# Loops
# names = ["Eslam", "Medhat", "Fathy", "Mohamed"]
# for name in names: # For Loop
#     print(name)


# person = {
#     "name" : "Eslam",  #Key is Unique
#     "age" : 25,
#     "address" : "Egypt"
# }
# print(person.items())
# for key in person:
#     # print(key)
#     print(f"key:{key} value:{person[key]}")

# EXERCISE

# result = 0
# numbers = [1, 3, 5, 6, 7, 9]
# for number in numbers:
#     result += number
#
# print(f"Result = {result}")


# WHILE Loop
# number = 0
# while number < 10:
#     print(number)
#     number +=1
# else:
#     print("while loop ended")


# BREAK
# number = 0
# while number < 10:
#     if number == 5:
#         break
#     number += 1
#     print(number)

# CONTINUIO
# while number < 10:
#     number += 1
#     if number < 5:
#         continue
#     print(number)

# number = 0
# for n in [1, 2, 3, 4, 5,6, 7, 8,9]:
#     if n < 5: # or ==
#         continue # or break
#     print(n)


# Functions

# def greet(name,age=20):
#     print(f"Hello {name} how are you")
#     if  age > 0:
#         print(f"I know your age = {age}")
#
# greet("Eslam")
# greet("world", 30)


# def is_adult(age):
#     if age >=16:
#         # return True
#         print("adult :)")
#     else:
#         # return False
#         print("not yaet an adult :(")
#
# # is_adult(25)
# # result = is_adult(45)
# # print(result)


# Built-in Function
# [].
# "".
# def #$@#% :
# import math
# print(math.pi)
# print(math.isqrt(16))
# from math import  isqrt
# print(isqrt(25))


# Modules

# import calculator
# print(calculator.addition(2,2))
# print(calculator.subtract(2,2))
# print(calculator.divide(2,2))
# print(calculator.multiply(2,2))
# from calculator import  addition
# from calculator import  subtract
# from calculator import  divide
# from calculator import  multiply


# CLASSES
class Phone:

    def __init__(self,brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand}is Calling {phone_number}")

iphone = Phone("Iphone 7+",300)
samsung = Phone("Samsung S20",1400)
#
print(iphone.brand)
print(iphone.price)
iphone.call("911")
print(samsung.brand)
print(samsung.price)


# DATES
# import datetime
# from datetime import datetime
# from datetime import date
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# print(datetime.date.today())
# print(datetime.datetime.now().time())

# from datetime import datetime
# from datetime import date
# now = datetime.now()
# print(now)
# print(now.strftime("%d-%m-%Y  %H:%M:%S"))
# print(now.strftime("%d-%b-%Y  %H:%M:%S"))
# print(now.strftime("%d-%B-%Y  %H:%M:%S"))
# print(date.today().strftime("%d-%m-%Y"))
# print(date.today().strftime("%d-%B-%Y"))



# # WORKING WITH FILES
# # write =w , read = r , write + read = r+ , append =a
# file = open("./data.csv","r+")
# file.write("id,name,email\n")
# file.write("1,Eslam,eslam@bamboogeeks.com\n")
# file.write("2,Ahmed,Ahmed@bamboogeeks.com\n")
# file.close()

# file = open("./data.csv","r")
# # print(file.read())
# # file.readline()
# for line in file:
#     print(line)




# # READING FROM THE INTERNET
# from urllib import request
#
# r = request.urlopen("http://www.google.com")
# print(r.getcode())
# print(r.read)



# FETCHING JOKES
# from urllib import request
# import json
# url ="http://api.jokes.one/jod"
# r = request.urlopen(url)
# print(r.getcode())
# data = r.read()
# jsonData = json.loads(data)
# print(jsonData)

