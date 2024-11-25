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

# 4 Python Program to Split Even and Odd Elements into Two Lists

# my_list = [24, 23, 18, 8, 9, 5]

# even_list = []
# odd_list = []

# for i in my_list: 
#     if i % 2 == 0: 
#         even_list.append(i)
        
#     else: 
#         if i % 2 != 0: 
#             odd_list.append(i)
            
# print(even_list)
# print(odd_list)


#5  Python Program to Find Average of a List
# my_list = [10,23,98]

# def average_of_list(my_list):
#     sum_list = sum(my_list)
#     length_list = len(my_list)
#     average_list = sum_list/length_list
#     return average_list

# result = average_of_list(my_list)
# print(result)

# 6 Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List

# my_list = [12, -12, 45,55,67,1,2,3,-11,-3,17]

# even_list = []
# odd_list = []
# negative_list = []

# for i in my_list: 
#     if i % 2 == 0 and i > 0: 
#         even_list.append(i)
#         sum_even = sum(even_list)
#     elif i % 2 != 0 and i > 0: 
#         odd_list.append(i)
#         sum_odd = sum(odd_list)
#     elif i < 0: 
#         negative_list.append(i)
#         negative_sum = sum(negative_list)
#     else: 
#         print("No Match")

# print(sum_even)
# print(sum_odd)
# print(negative_sum)


# Python Program to Count Occurrences of Element in List


#11 Python Program to Remove Duplicates from a List

my_list = [12,12,13,13,13,14,4,5,6]

def remove_duplicates(given_list): 
    set_list = set(my_list)
    return set_list 

result = remove_duplicates(my_list)
print(result)