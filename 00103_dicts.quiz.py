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

