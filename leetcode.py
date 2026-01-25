# digits = [9, 9, 9]
# def plus_one(digits):
#     i = len(digits) - 1      # start from last digit

#     while i >= 0:
#         print("i", i)
#         if digits[i] < 9:
#             print("digit i: ", digits[i])
#             digits[i] += 1   # add 1
#             print("digits: ", digits[i])
#             return digits
#         else:
#             digits[i] = 0    # change 9 to 0
#             i -= 1   
#             print("else i: ", i)# move left
#     print("1+digits: ", [1] + digits)
#     return [1] + digits
# print(plus_one(digits))


# ss = "hello world! 123"

# ss = input("Enter the string value: ")
# c = {"Letter" : 0, "digit" : 0}
# for e in ss:
#     if e.isalpha():
#         c["Letter"] +=1
#     elif e.isdigit():
#         c["digit"] += 1
#     else:
#         pass
# print("c:", c)


import math

C =50
H = 30
items = [x for x in input().split(",")]
lis = []
for item in items:
    value = str(int(round(math.sqrt(2*C*float(item)/H))))
    lis.append(value)
print(lis)
