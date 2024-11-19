# # FOR LOOP: 
# for i in range(1, 5):
#     print(i)

# # WHILE LOOP 
# i = 1
# while i < 5:
#     print(i)
#     i += 1


#1Python Program to Check Whether a Given Number is Even or Odd

# number = 15

# if number % 2 == 0: 
#     print("even number")
# else: 
#     print("odd number")

# #2Python Program to Check Whether a Number is Positive or Negative
# number = 17

# if number > 0: 
#     print("positive number")
# else: 
#     print("negative number")

# #3Python Program to Print All Odd Numbers in a Range

# for i in range(1,11): 
#     if i % 2 != 0: 
#         print(i)

# #4Python Program to Check if a Number is a Palindrome

# number = 1221

# def palindrome(given_number): 
#     string_number = str(given_number)
#     if string_number == string_number[::-1]: 
#         return "palindrome"
#     else: 
#         return "not palindrome"
    
# result = palindrome(number)
# print(result)

# #5Python Program to Reverse a Number

# number = 1290

# def reverse_number(number): 
#     str_number = str(number)
#     result = str_number[::-1]
#     return result 

# result = reverse_number(number)
# print(result)

# # 6 Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

# for i in range(1,11): 
#     if i % 2 != 0 and i % 3 != 0: 
#         print(i)

# #7Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

# for i in range(1,11): 
#     if i % 7 == 0 and i % 5 == 0: 
#         print(i)

# #8Python Program to Print All Numbers in a Range Divisible by a Given Number

# given_number = 2

# for i in range(1,12): 
#     if i % given_number == 0: 
#         print(i)


# #9  Python Program to Find Sum of Digits of a Number


# #12 Python Program to Count the Number of Digits in a Number

# # given_number = 123457

# # def count_digits(given_number): 
# #     str_number = str(given_number)
# #     length_number = len(str_number)
# #     return length_number 

# # result = count_digits(given_number)
# # print(result)



# 13 Python Program to Count the Number of Digits in a Number

given_value = 14 
n = given_value

for i in range(1,n + 1): 
    if given_value % i == 0: 
        print(i)

# 14 Python Program to Find the Smallest Divisor of an Integer
# given_value = 14 
# n = given_value

# total = []

# for i in range(1,n + 1): 
#     if given_value % i == 0: 
#         append_total = total.append(i)
        
# min_val = min(total)
# print(min_val)




# # l = list(str(123))
# # print(l)


# # a = list("apple")
# # print(a)

# # number = 123 

# # def temp_sum(given_number): 
# #     list_num = int(list(str(given_number)))
# #     sum_num = sum(list_num)
# #     return sum_num

# # result = temp_sum(number)
# # print(result)


# a = "1"
# b = "2"
# result = int(a) + int(b)
# print(result)





# # 13 Python Program to Find All the Divisors of an Integer

# # 14 Python Program to Find the Smallest Divisor of an Integer

# # 17 Python Program to Print Table of a Given Number

# given_number = 3

# result = []

# def table(given_number): 
#     numbers = list(range(1,11))
#     for num in numbers: 
#         result.append(num * given_number)
#     return result 

# result = table(given_number)
# print(result)
         
# # given_number = 4 

# # for num in range(1,11): 
# #     result = (given_number * num)
# #     print(result)


# 20 Python Program to Check Whether a given Year is a Leap Year

# year = 1904

# if year % 4 == 0 and year % 100 != 0: 
#     print("leap year")
# else: 
#     print("not leap year")

# 21 Python Program to Convert Centimeters to Feet and Inches

# cm = int(input("Enter height in centimeters: "))

# inches = cm * 0.393701 
# feet = cm * 0.0328084
# print(inches)
# print(feet)

#22 Python Program to Read a Number n and Compute n+nn+nnn

number = int(input("Enter a number"))

temp = str(n)
t1 = temp + temp
print(t1)
