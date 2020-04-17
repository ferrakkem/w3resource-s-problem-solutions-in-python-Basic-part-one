import sys
import datetime
import calendar
from datetime import date
import math
import os.path
import struct
import os, inspect, getpass
import platform
import site
from math import sqrt

'''
Problem:1
Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, 
Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are


'''
def problemNumber_one():
    print(
        "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


#problemNumber_one()

'''
Problem:2
Write a Python program to get the Python version you are using
'''
def problemNumber_two():
    #for check out version you need to import sys
    print("Python version: " + sys.version)

#problemNumber_two()

'''
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
'''
def problemNumber_three():
    #for get dateime you need to import datetime
    now = datetime.datetime.now()
    print(now.strftime("Current date and time:\n%Y-%m-%d %H:%M:%S"))

#problemNumber_three()

'''
Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''

def problemNumber_flour(radious, circle):
    radious = int(radious)
    circle = int(circle)
    return radious * circle

result = problemNumber_flour(2, 3.1416)
#print(result)

'''
Write a Python program which accepts the user's first and 
last name and print them in reverse order with a space between them
'''

def problemNumber_five():
    first_name = input("Enter First name: ")
    last_name = input("Enter last name: ")
    revesre = first_name + " " + last_name
    return (revesre[::-1])

#print(problemNumber_five())

def reverse_name_process_two(strValue):
    str = ""
    for i in strValue:
        str = i + str
        return str

#print(reverse_name_process_two("World"))


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

#print(reverse("we"))

'''
Write a Python program which accepts a sequence of comma-separated 
numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23'
'''
def convertIntoListAndTuple():
    values = input("Enter your number : ")
    l = values.split(",")
    t = tuple(l)
    print(l)
    print(t)

#convertIntoListAndTuple()
'''
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java
'''

def p7_splitFileExtension_():
    file_name = input("Enter your file name with extention :")
    file_extention = file_name.split(".")
    return ("File extention is :" + file_extention[-1])

#print(p7_splitFileExtension_())
'''
Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]
'''

def p8_findOutColor():
    color_list = ["Red", "Green", "White", "Black"]
    first_color = color_list[0]
    last_color = color_list[-1]
    return ("First :" + first_color + " and last color : " +  last_color)

#print(p8_findOutColor())

'''
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output :
The examination will start from : 11 / 12 / 2014
'''

def p9_replace():
    exam_st_date = (11, 12, 2014)
    output = str(exam_st_date).replace(",", "/")
    print(output)
    print(abs.__doc__)
#p9_replace()

'''
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module
'''
def p_12calender():
    year = int(input("Enter year: "))
    month = int(input("Enter month :"))
    print(calendar.month(year, month))

#p_12calender()

'''
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
def numberOfDays():
    f_date = date(2014, 7, 2)
    l_date = date(2014, 7, 11)
    delta = l_date - f_date
    return (delta.days)

#print(numberOfDays())

'''
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference. 
'''
def finddifference():
    base_number = 17
    user_input_number = int(input("Enter your number :"))

    if user_input_number <= base_number:
        result = base_number - user_input_number
        return result
    else:
        result = (user_input_number - base_number) * 2
        return result


dif_result = finddifference()
print(dif_result)

























































