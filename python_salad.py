#1 apple is fruit - return this in such a way that it prints fruit is apple 
#2 malayalam - check if this string is palindrome
#3 1234321 - check if the given number is palindrome

#4 find those pair of numbers such that their sum is divisible by 2
numbers_list = [(10,22), (20, -15), (8,8), (1,2)]
result = [(x,y) for (x,y) in numbers_list if (x + y ) % 2 == 0 ]
print(result)

#5 find those pair of numbers such that their sum is divisible by 3
odd_list = [(10,22), (20, -15), (8,8), (1,2)]
result = [(x,y) for (x,y) in numbers_list if (x + y ) % 3 == 0 ]
print(result)

#6 Use list comprehensions to find the square and cubes of numbers that are 
# between 10 and 50 and also that are multiples of 3

numbers = [ x for x in range(1,51) if x % 3 == 0]
print(numbers)

import math
