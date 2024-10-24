# ⁠Given a list of numbers, use a method to append the number 10 to the end of the list.
numbers = [12,11,34,556,56]
numbers.append(10)
print(numbers)

# Given a list of strings, use a method to extend it by adding another list of two strings to it.
fruits = ["apple", "pineapple", "custard apple"]
berries = ["strawberry", "blueberry"]

fruits.append(berries)
print(fruits)

# ⁠Given a list of numbers, use a method to insert the number 25 at index 2.
numbers = [12,11,34,556,56]
numbers.insert(2,25)
print(numbers)

# ⁠Given a list of strings, use a method to remove the string "apple" from the list.
fruits = ["apple", "pineapple", "custard apple"]
fruits.pop(0)
print(fruits)

# Given a list of numbers, use a method to find and print the index of the number 15 in the list.
numbers = [12,11,15,34,556,56]
index_of_15 = numbers.index(15)
print(index_of_15)

# ⁠Given a list of numbers, use a method to sort the list in ascending order.
numbers = [12,11,15,34,556,56]
numbers.sort()
print(numbers)

# ⁠Given a list of strings, use a method to count how many times "banana" appears in the list.
fruits = ["apple","banana", "pineapple", "custard apple", "banana", "banana"]
banana_occurence = fruits.count("banana")
print(banana_occurence)

# ⁠Given a list of numbers, use a method to reverse the order of elements in the list.
numbers = [12,11,15,34,556,56]
numbers.reverse()
print(numbers)

# ⁠Given a list of numbers, use a method to clear all the elements from the list.
numbers = [12,11,15,34,556,56]
numbers.clear()
print(numbers)


# ⁠Given a list of strings, use a method to pop and print the last item in the list.
fruits = ["apple", "pineapple", "custard apple"]
last_item = fruits.pop()
print(last_item)

# ⁠Given a list of numbers, use a method to count how many times the number 7 appears in the list.
numbers = [12,7,11,715,7,34,77556,7,56,7]
count_7 = numbers.count(7)
print(count_7)

# ⁠Given a list of strings, use a method to remove the element at index 3.
fruits = ["mango", "strawberry", "apple", "custard apple", "orange"]
fruits.pop(3)
print(fruits)

# ⁠Given a list of numbers, use a method to sort the list in descending order.
numbers = [12,7,11,715,7,34,77556,7,56,7]
numbers.sort(reverse = True)
print(numbers)

# ⁠Given a list of strings, use a method to copy the list to a new list and print the new list.
fruits = ["mango", "strawberry", "apple", "custard apple", "orange"]
new_list = fruits.copy()
print(new_list)

# ⁠Given a list of numbers, use a method to find and print the maximum number in the list.
numbers = [12,7,11,715,7,34,77556,7,56,7]
max_number = max(numbers)
print(max_number)

# ⁠Given a list of strings, use a method to find and print the length of the list.
fruits = ["mango", "strawberry", "apple", "custard apple", "orange"]
length_of_fruits = len(fruits)
print(length_of_fruits)

# ⁠Given a list of numbers, use a method to sum up all the elements in the list.
numbers = [12,7,11,715,7,34,77556,7,56,7]
sum_numbers = sum(numbers)
print(sum_numbers)


# ⁠Given a list of strings, use a method to add a new string "orange" at the beginning of the list.
fruits = ["mango", "strawberry", "apple", "custard apple"]
fruits.insert(0,"organge")
print(fruits)

# ⁠Given a list of numbers, use a method to print a sorted version of the list without modifying the original list.
numbers = [12,7,11,715,7,34,77556,7,56,7]
new_numbers = sorted(numbers)
print(new_numbers)

# # ⁠Given a list of numbers, use a method to remove all occurrences of the number 3 from the list.
# numbers = [12,7,3,3,3,311,715,7,34,77556,7,56,7]
# numbers.remove(3)
# print(numbers)

# These questions help practice various list methods like append(), extend(), insert(), remove(), index(), sort(), count(), reverse(), clear(), pop(), and others.