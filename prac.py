# # FOR LOOP: 
# for i in range(1, 5):
#     print(i)

# # WHILE LOOP 
# i = 1
# while i < 5:
#     print(i)
#     i += 1


# Python Program to Reverse a Number

number = 1221

def reverse_number(given_number): 
    string_number = str(given_number)
    if string_number == string_number[::-1]: 
        return "palindrome"
    else: 
        return "not palindrome"
    
result = reverse_number(number)
print(result)



# Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

for i in range(1,11): 
    if i % 2 != 0 and i % 3 != 0: 
        print(i)


# # Python Program to Print All Numbers in a Range Divisible by a Given Number
number = 7 

for i in range (1,16): 
    if i % number == 0: 
        print(i)

# Python Program to Find Sum of Digits of a Number