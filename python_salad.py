# 1 apple is fruit - return this in such a way that it prints fruit is apple 

# word = "apple is fruit"
# # result = fruit is apple

# # 2 malayalam - check if this string is palindrome
# def palindrome(given_word): 
#     if given_word[::-1] == given_word:
#         return ("It is a Palindrome")
#     else: 
#         return ("It is not a Palindrome")

# result = palindrome("malayalam")
# print(result)

# result2 = palindrome("Python")
# print(result2)



# # 3 numbers = 1234321 - check if the given number is palindrome
# def palindrome(given_numbers): 
#    if given_numbers[::-1] == given_numbers:
#      return ("It is a Palindrome")
#    else: 
#      return ("It is not a Palindrome")

# result = palindrome(1234321)
# print(result)

# result2 = palindrome("1234325")
# print(result2)


# #4 find those pair of numbers such that their sum is divisible by 2
# numbers_list = [(10,22), (20, -15), (8,8), (1,2)]
# result = [(x,y) for (x,y) in numbers_list if (x + y ) % 2 == 0 ]
# print(result)

# #5 find those pair of numbers such that their sum is divisible by 3
# odd_list = [(10,22), (20, -15), (8,8), (1,2)]
# result = [(x,y) for (x,y) in numbers_list if (x + y ) % 3 == 0 ]
# print(result)

# #6 Use list comprehensions to find the square and cubes of numbers that are 
# # between 10 and 50 and also that are multiples of 3

# import math
# numbers = [ x for x in range(10,51) if x % 3 == 0]
# print(numbers)
# result = [(math.sqr(x), pow(x,3)) for x in numbers]
# print(result)








# # Python Program to Find All the Divisors of an Integer
integer = 7 
divisors = []

for i in range(1,integer + 2): 
    if integer % i == 0: 
        divisors.append(i)

print(divisors)


# # Python Program to Find the Smallest Divisor of an Integer
integer = 15
divisors = []

for i in range(1,integer + 2): 
    if integer % i == 0: 
        divisors.append(i)
        min_value = min(divisors)

print(min_value)


# check if the given number is palindrome
number = 1221

def palindrome(given_number):
    if given_number[0] == given_number[-1]: 
        return "palindrome"

result = palindrome(number)
print(result)



    
# # Python Program to Count the Number of Digits in a Number


# random list, sort it, then find median, and average, len is even 
# scores = [85, 92, 78, 88, 95,96]

# def median(given_list): 
#    sorted_list = sorted(given_list)
#    length = len(sorted_list)
#    if length % 2 == 0: 
#     first_val = sorted_list[2]
#     second_val = sorted_list[3]
#     add = first_val + second_val
#     median = add / 2
#     return median

# result = median(scores)
# print(result)
      

# random list, sort it, then find median, and average, len is even 

# fruit
