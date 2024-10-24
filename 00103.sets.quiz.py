# Create a set of three numbers: 1, 2, 3
my_numbers = {1,2,3}
print(my_numbers)

# Convert this list to a set to remove duplicates
numbers = [1, 2, 2, 3, 3, 3]
set_Numbers = set(numbers)
print(set_Numbers)

# Adding Elements
# Add 'orange' to the set
fruits = {'apple', 'banana'}
orange_add = fruits.add("orange")
print(fruits)

# Question 1.1
# Create an empty set called 'numbers'
numbers = set()   # Use the set() function to create an empty set
                  # numbers = {}   creates an empty dictionary not set 

# Add the numbers 1, 2, and 3 one at a time
numbers.add(1)
numbers.add(2)
numbers.add(3)
print(numbers)

# Adding Elements
# Add 'yellow' to the colors set
colors = {'red', 'blue', 'green'}
colors.add('yellow')
print(colors)

# Add multiple colors: orange, purple, pink at once
# colors.update('orange', 'pink', 'purple')
# This will split each string into individual characters!
colors.update(['orange', 'pink', 'purple'])
print(colors)

# Removing Elements
# Remove 'blue' from the colors set
colors.remove('blue')
print(colors)

# Try to remove 'yellow' from the colors set. 
# Which method should you use to avoid an error if yellow isn't in the set?
colors.discard('black')
print(colors)
# discard() won't raise an error if element doesn't exist

# Checking Elements
# Check if 'red' is in the colors set
colors = {'red', 'blue', 'green'}
red_exist = 'red' in colors
print(red_exist)

# How many colors are in the set?
color_count = len(colors)
print(color_count)

# Intersection, Unique and Difference
colors1 = {'red', 'blue', 'green'}
colors2 = {'blue', 'yellow', 'orange'}

# 1. Colors that are in both sets (intersection)
combined_colors = colors1.intersection(colors2)
print(combined_colors)
# Operator: set1 & set2

# 2. Union (all unique colors)
unique_colors = colors1.union(colors2)
print(unique_colors)
# Operator: set1 | set2

# 3. Colors in colors1 but not in colors2 (difference)
colors1_unique = colors1.difference(colors2)
print(colors1_unique)
# Operator: set1 - set2

#Subsets
# You have two sets:
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# 1. Is set1 a subset of set2?
is_set1_subset = set1.issubset(set2) #method
is_set1_sub = set1 <= set2 #operator     
print(is_set1_subset)      #Subset (A ⊆ B): All elements of A are in B
print(is_set1_sub)

# 2. Is set2 a superset of set1?
set2_superset = set2.issuperset(set1)
set2_super = set2 >= set1  #Superset (A ⊇ B): A contains all elements of B
print(set2_superset)       #Operator: A >= B
print(set2_super)

# Working with Characters in Sets
string = "Facebook"


