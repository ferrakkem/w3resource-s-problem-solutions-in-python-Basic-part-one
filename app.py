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


#dif_result = finddifference()
#print(dif_result)

'''
Write a Python program to test whether a number is within 100 of 1000 or 2000
'''
def p17_withinRangeOrOutOfRange(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

#print(p17_withinRangeOrOutOfRange(900))

'''
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return three times of their sum
'''
def p18_calculateTheSumOfThreeGivenNumbers(num1, num2, num3):

    if num1 == num2 and num2 == num3:
        result = (num1 + num2 + num3) *3
        return  result
    else:
        result = num1 + num2 + num3
        return result

#threeNumber = p18_calculateTheSumOfThreeGivenNumbers(1, 3, 3)
#print(threeNumber)

'''
Write a Python program to get a new string from a given string where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged
'''
def p19_stringUpdate():
    count = 0

    while count <= 10:
        user_string = input("Enter your string :")
        value = "is"
        finding = user_string.startswith("is ")
        #print(finding)
        if finding == True:
            return user_string
        else:
            print("Not")
            new_string = "is " + user_string
            print(new_string)
    count = count+1

#print(p19_stringUpdate())

'''
 Write a Python program to get a string which is n (non-negative integer) copies of a given string
'''
def p20_copiesOfAString(uesr_string, num):
    result = ""
    for i in range(num):
        print(i)
        result = result + uesr_string
    return result
#print(p20_copiesOfAString("abc", 3))

'''
Write a Python program to find whether a given number 
(accept from the user) is even or odd, print out an appropriate message to the user
'''
def p21_findEvenOrOdd():
    user_input = int(input("Enter a number: "))
    if user_input % 2 == 0:
        print("Even Number")
    else:
        print("Odd number")

#p21_findEvenOrOdd()

'''
Write a Python program to count the number 4 in a given list
'''
def p22_count_the_number(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count +1
    return count

#print(p22_count_the_number([1, 4, 6, 7, 4]))
#print(p22_count_the_number([1, 4, 6, 4, 7, 4]))

'''
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2
'''

def p23_getStringFromUser():
    user_string = input("Enter your string: ")
    update_string = ""
    new_string = user_string[:2]
    print(new_string)
    if len(new_string) >= 2:
        for i in range(2):
            update_string = update_string + new_string
        print( update_string)


#p23_getStringFromUser()

def randomProblem():
    total = 0

    for i in range(1, 100):
        if i % 3 == 0 or i % 5 ==0:
            total = total + i;
    print(total)

#randomProblem()

'''
Write a Python program to test whether a passed letter is a vowel or not.
'''

def p24_checkVowel():
    input_letter = input("Enter your letter: ")
    vowel = "aeiou"
    if input_letter in vowel:
        print("Vowel")
    else:
        print("Not vowel")
#p24_checkVowel()
'''
Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''
def p25_valueIsContained(grroud_value, n):

    if n in grroud_value:
        return True
    else:
        return False

#print(p25_valueIsContained([1, 5, 8, 3],3))
#print(p25_valueIsContained([1, 5, 8, 3],-1))

'''
Write a Python program to create a histogram from a given list of integers.
'''

def histogram( items ):
    for i in items:
        output = ""
        times = i
        while times > 0:
            output = output + "*"
            times = times - 1
        print(output)

#histogram([2, 3, 6, 5])

'''
Write a Python program to concatenate all elements in a list into a string and return it.
'''
def p27_concatenate(number_list):
    #print(str(number_list))
    outputString = ""
    for i in number_list:
        #print(i)
        outputString = outputString + str(i)
    print(outputString)

#p27_concatenate([1,2,3,4,5])

'''
Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing 
if any numbers that come after 237 in the sequence. Go to the editor
Sample numbers list :

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

'''
def p28_evenOrOddList(number_list):
    a = []

    for i in number_list:
        if i < 237 and i % 2 == 0:
            a.append(i)
        else:
            continue
            return  a
    print(a)
numbers = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527
    ]
#p28_evenOrOddList(numbers)

'''
Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
'''
def p29_findColorDiffSet():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])

    new_color_set = color_list_1.difference(color_list_2)
    print(new_color_set)

#p29_findColorDiffSet()

def p29_second_findColorDiffSet():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    new_color_set = []

    for color in color_list_1:
        if color not in color_list_2:
            new_color_set.append(color)
    print(new_color_set)

#p29_second_findColorDiffSet()

'''
Write a Python program that will accept the base and height of a triangle and compute the area.
'''
def p30_findArea(height, base):
    a = (height * base) / 2
    return a

#print(p30_findArea(20,40))

'''
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
'''
def p31_greatestCommon_Divisor(x, y):
    gcd = 1
    if x % y == 0:
        return y

    for i in range(int(y/2),0,-1):
        if x % 2 == 0 and y % 2 == 0:
            print(x, y)
            gcd = i
            print(gcd)
            break
    return gcd

#get_gcd = p31_greatestCommon_Divisor(102, 8)
#print(get_gcd)
#get_gcd = p31_greatestCommon_Divisor(17, 12)
#print(get_gcd)

'''
Write a Python program to get the least common multiple (LCM) of two positive integers.
'''
def p32_leastCommon_Divisor(x, y):
    if x > y:
        z= x
    else:
        z= y

    while (True):
        if ((z % y == 0) and (z % x ==0)):
            lcm = z
        z = z +1
    return  lcm


#get_lcm = p32_leastCommon_Divisor(4, 6)
#print(get_lcm)

'''
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
'''
def p33_SumOfthreInt(num1, num2, num3):
    if num1 == num2 or num2 == num3:
        return 0
    else:
        result = num1 + num2 + num3
        return result

#sumOutPut = p33_SumOfthreInt(2,3,4)
#print(sumOutPut)

#sumOutPut = p33_SumOfthreInt(2,3,3)
#print(sumOutPut)

'''
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
'''
def p34_sumOfTwoInt(num1, num2):

    sum_result = num1 + num2
    if sum_result in range(15,20):
        return 20
    else:
        return sum_result

#sum_result = p34_sumOfTwoInt(10, 5)
#print(sum_result)

'''
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''
def p35_returnTrue(num1, num2):
    if (num1 == num2) or (num1 + num2 == 5) or (num1 - num2) == 5:
        return True
    else:
        return False

#result_return = p35_returnTrue(10,5)
#print (result_return)

'''
Write a Python program to add two objects if both objects are an integer type
'''
def p36_add_two_objects(a ,b):
    if not (isinstance(a, int)) and isinstance(b, int):
        raise TypeError("Input must be integer")
    return a+b

#resultOftwo = p36_add_two_objects(2,2)
#print(resultOftwo)
'''
Write a Python program to display your details like name, age, address in three different lines.
'''

def p37_psersonalInformation(name, age, address):

    print("My name is :" + name)
    print("My age is :" + str(age))
    print("My address is :" + address)


#p37_psersonalInformation("Ferrakkem", 31, "Toronto, Ontario, Canada")

'''
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
'''
def p40_distance():
    p1 = [4, 0]
    p2 = [6, 6]
    distaance = math.sqrt((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)
    print (distaance)

#p40_distance()
'''
Write a Python program to check whether a file exists.
'''

def p41_fileExists():
    open('abc.txt', 'w')
    print(os.path.isfile('abc.txt'))

#p41_fileExists()

'''
Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS
'''
def p42_checkVersion():
    print(struct.calcsize("P") * 8)

#p42_checkVersion()
'''
Write a Python program to get OS name, platform and release information.
'''
def p43_getSystemInfo():
    os_name = os.name
    platform_name = platform.version()
    release_info = platform.release()
    print("Os name :"+ os_name + "\nplatform name: " + platform_name +"\nRelease :" + release_info)
    site_pacl_name =site.getsitepackages()
    print(site_pacl_name)

    print(inspect.getfile(inspect.currentframe()))
    print(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    workers = os.cpu_count()
    print(workers)

    a = "2.200";
    print(str(a))
    print(float(a))
#p43_getSystemInfo()
'''
Write a Python program to print without newline or space.
'''

def p50_withOutNewLine():
    for i in range(0,10):
        print("*", end="")
    print("\n")

#p50_withOutNewLine()

def p51_too():
    print("your message")
    print(">>>your message", file=sys.stderr)

    username = getpass.getuser()
    print("user name :" + username)

#p51_too()

def p57_sum_of_n_numbers(n):
    import time
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s = s+1
    end_time = time.time()

'''
Write a python program to find the sum of the first n positive integers. 
'''
def p58_sumofInputNumber(n):
    sum = (n *(n + 1)) /2
    print(sum)

#p58_sumofInputNumber(2)

'''
 Write a Python program to calculate the hypotenuse of a right angled triangle. 
'''
def p60_FindHypotenuse():

    print("Enter your ab and bc :")

    ab = int(input())
    bc = int(input())
    print("We will find out AC?")
    ac = sqrt((ab**2) + (bc**2))
    print(ac)

#p60_FindHypotenuse()

'''
 Write a Python program to convert the distance (in feet) to inches, yards, and miles. 
'''
def p61_feetToOtherUnit():
    feet = float(input("Enter Feet :"))

    inches = 12 * feet
    print(inches)

    yeard = 0.333333 * feet
    print(yeard)

    miles = 0.000189394 * feet
    print(miles)

#p61_feetToOtherUnit()

'''
Write a Python program to get an absolute file path.
'''
def p63_absulatePath(path_name):
    return os.path.abspath(path_name)

#print(p63_absulatePath("abc.txt"))

'''
 Write a Python program to convert seconds to day, hour, minutes and seconds.
'''
def p65_convertSecondsToDay():
    user_time = int(input("Enter your seconds :"))
    day = user_time // (24 * 3600)
    print(day)
    user_time = user_time % (24*3600)
    print(user_time)
    hour = user_time // 3600
    print(hour)
    user_time = user_time % 3600
    print(user_time)
    minutes = user_time //60
    print(minutes)
    user_time = user_time % 60
    print(user_time)
    seconds = user_time
    print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

#print(p65_convertSecondsToDay())

'''
 Write a Python program to calculate the sum of the digits in an integer.
'''
def p68_sumOfGivenInteger():
     num = int(input("Enter your four integer :"))

     x = num // 1000;
     x1 = (num - x*1000) // 100;
     x2 = (num - x*1000 - x1*100) // 10
     x3 = num - x*1000 - x1*100 - x2*10
     sum = x + x1 + x2 +x3
     print("Sum of :" +str (num) + " is : " +str(sum))

#p68_sumOfGivenInteger()

def checkInputLent():
    num_values = int(input("Enter your value :"))
    a_string = str(num_values)
    length = len(a_string)
    print(length)

    my_string = "1"
    print(my_string.zfill(length))


checkInputLent()
























































