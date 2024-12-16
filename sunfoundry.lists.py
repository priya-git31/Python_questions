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


#11 Python Program to Remove Duplicates from a List

# my_list = [12,12,13,13,13,14,4,5,6]

# def remove_duplicates(given_list): 
#     set_list = set(my_list)
#     return set_list 

# result = remove_duplicates(my_list)
# print(result)


#10  Python Program to Merge Two Lists and Sort it
# my_list_1 = [6,7,8,9,9]
# my_list_2 = [1,2,23,4,5]

# def combined_list(my_list_1,my_list_2): 
#     combined_list = my_list_1 + my_list_2
#     sorted_combined_list = sorted(combined_list)
#     return sorted_combined_list

# result = combined_list(my_list_1,my_list_2)
# print(result)


#16  Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List

# import random

# empty_list = []

# for i in range(1,21): 
#     empty_list.append(random.randint(1,20))

# print(empty_list)


#12  Python Program to Swap the First and Last Element in a List

# my_list = ["d", "b", "c"]

# new_list = []

# def swapped_list(my_list): 
#     first_element = my_list[0]
#     last_element = my_list[-1]
#     first,*other, last = my_list
#     new_list = last_element, *other, first_element 
#     return new_list

# result = swapped_list(my_list)
# print(result)

# # Python Program to Return the Length of the Longest Word from the List of Words

# my_list = ["apple", "ball", "cat"]



# for item in my_list: 
#     chars = list(item)
#     length_chars = len(chars)

# print(length_chars)


# Python Program to Find the Union of Two Lists
# list_1 = [1,4,5,6]
# list_2 = [2,3,4]


# Python Program to Return the Length of the Longest Word from the List of Words
# my_list = ["apple", "ball", "cat"]

# my_list_len = []

# for item in my_list: 
#     item_len = len(item)
#     my_list_len.append(item_len)
#     longest_word = max(my_list_len)
# print(longest_word)

# Python Program to Count Occurrences of Element in List
# my_list = ["apple", "ball", "cat", "cat"]

# count_list = {}

# for item in my_list: 
#     if item in count_list: 
#         count_list[item] = count_list[item] + 1 
#     else: 
#         count_list[item] = 1
# print(count_list)

# Python Program to Find the Union of Two Lists

# list_1 = [1,4,5,6]
# list_2 = [2,3,4]

# union_two = list(set(list_1) | set(list_2))
# print(union_two)

# # Python Program to Find the Intersection of Two Lists
# list_1 = [1,4,5,6]
# list_2 = [2,3,4]

# union_two = list(set(list_1) & set(list_2))
# print(union_two)

# Python Program to Sort a List According to the Second Element in Sublist

lst = [[1, 4], [3, 2], [5, 6], [2, 1]]

new_list = sorted(lst, key=lambda x:x[1])
print(new_list)