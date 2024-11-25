#1 Python Program to Find Largest Number in a List

# my_list = [1,2,3,10]

# for i in my_list: 
#     max_list = max(my_list)
# print(max_list)

#2 Python Program to Find Second Largest Number in a List

# my_list = [9,2,3,10]

# for i in my_list:
#     reversed_list = sorted(my_list, reverse=True)
#     second_largest = reversed_list[1]
# print(second_largest)

#3 Python Program to Print Largest Even and Largest Odd Number in a List

# my_list = [10,11,8,9,12]

# even_list = []
# odd_list = []

# for i in my_list: 
#     if i % 2 == 0: 
#         even_list.append(i)
#         max_even = max(even_list)
#     else: 
#         if i % 2 != 0: 
#             odd_list.append(i)
#             max_odd = max(odd_list)

# print(max_even)
# print(max_odd)

# Python Program to Split Even and Odd Elements into Two Lists

my_list = [24, 23, 18, 8, 9, 5]

even_list = []
odd_list = []

for i in my_list: 
    if i % 2 == 0: 
        even_list.append(i)
        
    else: 
        if i % 2 != 0: 
            odd_list.append(i)
            
print(even_list)
print(odd_list)