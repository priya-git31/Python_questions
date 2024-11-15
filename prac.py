# # FOR LOOP: 
# for i in range(1, 5):
#     print(i)

# # WHILE LOOP 
# i = 1
# while i < 5:
#     print(i)
#     i += 1


#1Python Program to Check Whether a Given Number is Even or Odd

number = 15

if number % 2 == 0: 
    print("even number")
else: 
    number % 3 == 0
    print("odd number")

#2Python Program to Check Whether a Number is Positive or Negative
number = 17

if number > 0: 
    print("positive number")
else: 
    number < 0
    print("negative number")

#3Python Program to Print All Odd Numbers in a Range

for i in range(1,11): 
    if i % 2 != 0: 
        print(i)

#4Python Program to Check if a Number is a Palindrome

number = 1221

def palindrome(given_number): 
    string_number = str(given_number)
    if string_number == string_number[::-1]: 
        return "palindrome"
    else: 
        return "not palindrome"
    
result = palindrome(number)
print(result)

#5Python Program to Reverse a Number

number = 1290

def reverse_number(number): 
    str_number = str(number)
    result = str_number[::-1]
    return result 

result = reverse_number(number)
print(result)

# 6 Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

for i in range(1,11): 
    if i % 2 != 0 and i % 3 != 0: 
        print(i)

#7Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

#8Python Program to Print All Numbers in a Range Divisible by a Given Number

given_number = 2

for i in range(1,12): 
    if i % given_number == 0: 
        print(i)


#12 Python Program to Count the Number of Digits in a Number

given_number = 123457

def count_digits(given_number): 
    str_number = str(given_number)
    length_number = len(str_number)
    return length_number 

result = count_digits(given_number)
print(result)