#Dictionary Practice Questions
# Basic Operations:


# Create a dictionary called student with keys 'name', 'age', and 'grade'. Assign any values you want.
Student = { "name" : "Jhon", 
           "age" : 23,
           "grade" : "A"
}
print(Student)

# Given a dictionary fruits = {'apple': 5, 'banana': 3, 'orange': 2}, print the number of apples.
fruits = {'apple': 5, 'banana': 3, 'orange': 2}
value_apple = fruits["apple"]
print(value_apple)

# Add a new key-value pair 'mango': 4 to the fruits dictionary.
fruits["mango"] = 4
print(fruits)

# Remove 'orange' from the fruits dictionary.
removed_value = fruits.pop("orange")
print(fruits)

# Check if 'grape' exists in the fruits dictionary.
grape_exists = "grape" in fruits
print(grape_exists)

# Dictionary Methods:
# 6. Given scores = {'math': 85, 'science': 92, 'history': 78}, print all the subject names (keys) using a dictionary method.
scores = {'math': 85, 'science': 92, 'history': 78}
print(scores.keys())

# Print all the scores (values) from the scores dictionary using a dictionary method.
print(scores.values())

# Create a copy of the scores dictionary using a dictionary method.
copy_dict = fruits.copy()
print(copy_dict)

# Modification and Updates:
# 9. Given menu = {'coffee': 2.50, 'tea': 2.00, 'cookie': 1.50}, increase all prices by $0.50.
menu = {'coffee': 2.50, 'tea': 2.00, 'cookie': 1.50}

for item in menu: 
    menu[item] = menu[item] + 0.50
print(menu)

# Merge two dictionaries:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged1 = dict1 | dict2
print(merged1)
merged2 = {**dict1, ** dict2}
print(merged2)

# Practical Applications:
# 12.Create a phone book dictionary where you can:
# Add a new contact (name and number)
# Update an existing contact's number
# Delete a contact
phone_book = {
    "Haripriya" : 55123, 
    "Priya" : 34489, 
    "Riya" : 66678
}

phone_book["Iya"] = 7879
print(phone_book)   #New Contact Added

phone_book["Haripriya"] = 55321
print(phone_book) #Updated a contact 

phone_book.pop("Iya")
print(phone_book) #Deleted a Contact 

# Create a simple shopping dictionary:
shopping = {'milk': 2, 'bread': 1, 'eggs': 12}

# Print how many eggs are in the shopping list
number_eggs = shopping["eggs"]
print(number_eggs)

# Change the quantity of bread to 2
shopping["bread"] = 2
print(shopping)

# Create a simple  dictionary:
ages = {'Tom': 25, 'Jerry': 30, 'Sara': 28}

# Print Tom's age
tom_age = ages["Tom"]
print(tom_age)

# Add a new person 'Mike' who is 35
ages["Mike"] = 35
print(ages)

# Remove 'Jerry' from the dictionary
remove_jerry = ages.pop("Jerry")
print(ages)

# Print how many people are in the dictionary
print(len(ages))

# Count how many times each fruit appears in this list
fruits = {'apple': 0, 'banana': 0, 'orange':0}
fruit_list = ['apple', 'apple', 'banana', 'orange', 'apple', 'orange']

for fruit in fruit_list: 
    fruits[fruit] = fruits[fruit] + 1
print(fruits)


# Count occurrences of each color
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
color_count = {'red': 0, 'blue': 0, 'green': 0}

for color in colors: 
    color_count[color] = color_count[color] + 1
print(color_count)

# Count how many times each animal appears
animals = ['dog', 'cat', 'dog', 'bird', 'cat', 'dog']

# Start with empty count
animal_count = {}

for animal in animals: 
    # If we've seen this animal before
    if animal in animal_count: 
        animal_count[animal] = animal_count[animal] + 1 
    # If it's a new animal
    else:
        animal_count[animal] = 1
print(animal_count)

# Count days of the week:
days = ['Monday', 'Tuesday', 'Monday', 'Wednesday', 'Monday', 'Thursday', 'Friday']
day_count = {}

for day in days: 
    if day in day_count: 
        day_count[day] = day_count[day] + 1
    else: 
        day_count[day] = 1 
print(day_count)

# Count types of fruits:
fruit_basket = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

fruit_count = {}

for fruit in fruit_basket: 
    if fruit in fruit_count: 
        fruit_count[fruit] = fruit_count[fruit] + 1
    else: 
        fruit_count[fruit] = 1
print(fruit_count)

