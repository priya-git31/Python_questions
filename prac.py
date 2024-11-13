# # FOR LOOP: 
# for i in range(1, 5):
#     print(i)

# # WHILE LOOP 
# i = 1
# while i < 5:
#     print(i)
#     i += 1


# Python Program to Reverse a Number

# number = 12345

# def reverse_number(given_number): 
#     str_num = str(given_number)
#     reverse = str_num[::-1]
#     return reverse

# result = reverse_number(number)
# print(result)



# Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

# for i in range(1,101): 
#     if (i % 2 != 0) or (i % 3 != 0): 
#         print(i)


# Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range
# for i in range(1,101): 
#     if (i % 7 == 0) and (i / 5 != 0): 
#         print(i)


# # Python Program to Print All Numbers in a Range Divisible by a Given Number
given_number = 5

for i in range(1,11): 
    if i % (given_number) == 0: 
        print(i)


# Python Program to Find Sum of Digits of a Number