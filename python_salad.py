# malayalam - check if this string is palindrome



# 1234321 - check if the given number is palindrome

# find those pair of numbers such that their sum is divisible by 2
numbers_list = [(10,22), (20, -15), (8,8), (1,2)]
result = [(x,y) for (x,y) in numbers_list if (x + y ) % 2 == 0 ]
print(result)

# find those pair of numbers such that their sum is divisible by 3
odd_list = [(10,22), (20, -15), (8,8), (1,2)]
result = [(x,y) for (x,y) in numbers_list if (x + y ) % 3 == 0 ]
print(result)
# use lsit comprehesnioosn to find the square and cubes of numbers that are between 10 and 50 and also that are multiples of 3