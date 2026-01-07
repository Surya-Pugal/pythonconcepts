from collections import Counter


"""1. Print all Prime numbers in an Interval
2. Check whether a number is Prime or not"""

# l = int(input("Enter the beginning number: "))
# u = int(input("Enter the ending number: "))

# for num in range(l, u+1):
#     if num >1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num) 


# ================OR======================


# n = int(input("Enter the number: "))
# count = 0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i%j == 0:
#             count = count+1
#     if count == 2:
#         print(i)
#     count = 0


 
# n = int(input("Enter the number: "))
# if n % 2 != 0:
#     print(f"The number {n} is prime")
# else:
#         print(f"The number {n} is not prime")


# =====0r====
# n = int(input("Enter the number: "))
# count = 0
# for i in range(1,n):
#     if n%i == 0:
#         count = count+1
# if count == 1:
#     print("prime")
# else:
#     print("not prime")

# ======or========

# n = int(input("Enter the number: "))
# for i in range(2,n):
#     if n%i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

"""3.) Parse a comma-separated string and convert it into a dictionary
Input:"id:101,name:Sagar,dept:IT,salary:50000"
Output:{'id': '101', 'name': 'Sagar', 'dept': 'IT', 'salary': '50000'}
"""
# s = "id:101,name:Sagar,dept:IT,salary:50000"

# d = {}
# for item in s.split(","):
#     # print(f"item split: {item}")
#     k, v = item.split(":")
#     # print("key and value", k,v)
#     d[k] = v
#     # print("dic: ", d[k])
# print(d)


"""4.) Reverse the numbers of the list
 
Input = [1,2,3,4,5,6]
Output= [5,4,3,2,1]
 """
 
# Input = [1,2,3,4,5,6]
# def reverse_list(r):
#      rev = []
#      rev += reversed(r)
#      return rev
#     #  print(rev)
# print(reverse_list(Input))

# Input = [1,2,3,4,5,6]
# rev = Input[::-1]
# print(rev)

"""5.) Flatten a nested list
Input:[[1, 2], [3, 4], [5]]
Output: [1, 2, 3, 4, 5]
Concept: Array manipulation."""

# Input = [[1, 2], [3, 4], [5]]
# def flatten_nested_list(lis):
#     flat_lis = []
#     for element in lis:
#         print("element: ", element)
#         if type(element) is list:
#             print("type", type(element))
#             for item in element:
#                 print("item: ", item)
#                 flat_lis.append(item)
#                 print("flat_lis: ", flat_lis)
#     return flat_lis
# print(flatten_nested_list(Input))

"""
6.) Validate mobile numbers using simple rules
Rule:
* must be 10 digits
* must start with 6/7/8/9
Input:["9876543210", "12345", "6789000000"]
Output: ["9876543210", "6789000000"]
"""
# Input = ["9876543210", "12345", "6789000000"]
# def validate_mobile_num(nums):
#     output = []
#     for n in nums:
#         print("n: ", n)
#         if len(n) == 10 and n.isdigit() and n[0] in "6789":
#             print("len: ", len(n))
#             print("digit: ", n.isdigit())
#             print("index of n: ", n[0])
#             output.append(n)
#             print("output: ", output)
#     return output
# validate_mobile_num(Input)

""""7.) Count how many times each word appears in a log line
Input:
 
"ERROR failed to connect ERROR timeout WARNING retry"
"""
# Input = "ERROR failed to connect ERROR timeout WARNING retry"
# def split_words(log_line):
#     words = log_line.split()
#     print(words)
#     word_count = {}
#     for word in words:
#         word_count[word] = word_count.get(word,0)+1
#     return word_count
# print(split_words(Input))

# Input = "ERROR failed to connect ERROR timeout WARNING retry"
# words = Counter(Input.split())
# print(words)


# // First try to familiarize with OOPS then attempt these questions
# 8.) Create a class Person and define all its attributes like age, name, gender, weight etc, also 
# create two functions getAge and getName which will return the age and name of the person respectively
# class Person:
#     def __init__(self, age, name, gender, weight):
#         self.age = age
#         self.name = name
#         self.gender = gender
#         self.weight = weight
#     def getAge(self):
#         return self.age
#     def getName(self):
#         return self.name
# person1 = Person(30, "Surya", "F", 58)
# print(person1.getAge())
# print(person1.getName())
    
    # Attributes nothing but a variable like age, name, gender...
    # age = 30
    # name = "John"
    # gender = "M"
    # Weight = 56
    # Creating an object is a instantiation(Or instantiating object)
# objectname = classname()

# By default the method parameter should be self. Self : its point to the current object
#     def getAge(self):
#         print("Hello", self.name, "H r u")
# ob = Person()
# print(ob.name)
# print(ob.age)
# print(ob.getAge)    

# __init__() method is used for initialize the variables/attributes of object. It is used to assign the value
# it call once. It call once the object is created. 
        
    
# class statement or keyword should not be empty so if you want to define the function or method, attribute later the we use "pass"
# class student:
#     pass


# 9.) Create a class and named “Shape“ and created 1 function calculatedArea and calculate the area of the given shape.
# There are multiple shapes like square, circle, cone, each shape has a different formula to calculate area.
# class Shape:
#     def __init__(self, name):
#         self.name = name
        
        
#     def calculatedArea(self):
#         if self.name == "square":
#             s = int(input("Enter the squares side length: "))
#             square_area = s*s
#             print(f"The area of square is {square_area}.")
#         elif self.name == "circle":
#             r = int(input("Enter the radius length: "))
#             pi = 3.14
#             circ_area = pi * r * r
#             print(f"The given circle length is {circ_area}.")
#         elif self.name == "cone":
#             r = int(input("Enter the radius length: "))
#             h = int(input("Enter the height: "))
#             pi = 3.14
#             cone_area = 0.33*pi*r*r*h
#             print(f"The given cone value is {cone_area}.")
# if __name__ == "__main__":
#     print("In Main: {__name__}")
#     shape_name = input("Enter the shape name: ")
#     s = Shape(shape_name)
#     s.calculatedArea()
            