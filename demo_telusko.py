# print("hello")

""" 1.) You are given a list that contains integers. You need to return the sum of the list.
Examples:
Input: arr = [54, 43, 2, 1, 5]
Output: 105
Explanation: Just sum it 54 + 43 + 2 + 1 + 5 = 105.
 """
# arr = [54, 43, 2, 1, 5]
# def add_elements(lst):
#     sum = 0
#     for n in lst:
#         sum = sum + n
#         # print(sum)
#         return sum
# print(add_elements(arr))    
    
# ======OR=======
# a = sum(arr)
# print(a)

""" 2.) You are given a list that contains integers. You need to decrement each element of 
the list by 1 and return the list.
Examples:
Input: arr = [54, 43, 2, 1, 5]
Output: 53 42 1 0 4
Explanation: Just decrement the numbers by 1.
"""

# arr = [54, 43, 2, 1, 5]
# def number_decrement(a):
#     dec_value = []
#     for i in range(len(a)):
#         dec_value.append(a[i]-1)
#     return dec_value
# print(number_decrement(arr))


""" 
3.) Given a string s, you need to reverse it.
Examples:
Input: s = "Hello"
Output: "olleH"
Explanation: Reverse of Hello is olleH
"""

# s = input("Enter the value: ")
# def reverse_string(text):
#     rev = reversed(text)
#     rev_str = "".join(rev)
#     return rev_str
# print(reverse_string(s))


# -----or--

# def reverse_string(text):
#     rev_str = text[::-1]
#     return(rev_str)
# print(reverse_string("Hello"))

#  -----or----

# s = "hello"
# rev_str = ""
# for ch in reversed(s):
#     rev_str +=  ch
# print(rev_str)


"""4.) Given a string s, you need to check if it is palindrome or not. A palidrome is a string that reads the same from front and back.
Note: Ignore the case in this question.
Examples:
Input: s = "Hello"
Output: false
Explanation: Hello is not equal to olleH so it's not a palindrome
"""
# s = input("Enter the string: ")
# str1 = s[::-1]
# if str1 == s:
#     print("Palindrome") 
# else:
#     print("Not")


"""5.) Given an integer array arr[], return the count of all the distinct elements in an array
Examples:
Input: arr[] = [2, 2, 3, 2]
Output: 2
Explanation: Distinct elements are {2, 3} 
# """
# a = [2, 2, 3, 2]
# def count_distinct(a):
#     dis_ele = []
#     # print("dis_type", type(dis_ele))
#     for e in a:
#         # print("inside for: ", e)
#         if e not in dis_ele:
#             # print("e: ", e)
#             dis_ele.append(e)
#             # print("value dis", dis_ele)
#     return(len(dis_ele))
# print("Output:", count_distinct(a))

"""
6.) Print elements from a given list present at odd index positions
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Note: The list index always starts at 0
 
Expected output:
20 40 60 80 100 """

# arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# def list_odd_index(a):
#     number_list = []
#     for index in range(len(a)):
#         if index % 2 == 1:
#             number_list.append(a[index])
#             print("Odd index: ", number_list)
#     return number_list
# print(list_odd_index(arr))

# -----------or----------
# a[::2] extracts elements at even indices (0, 2, 4) resulting in [10, 30, 50],
# while a[1::2] extracts elements at odd indices (1, 3, 5), resulting in [20, 40, 60].
# Slicing syntax list[start:stop:step] is used, where ::2 selects every second element starting from index 0 and 1::2 starts from index 1.

# arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # even = a[::2]  # Elements at even indices
# odd = arr[1::2]  # Elements at odd indices
# print(odd)

