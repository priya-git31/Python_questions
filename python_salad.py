# Starting dictionary
student_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 88,
    'David': 79,
    'Eve': 91
}

# 1. Write a function to print all student names (keys) using a for loop.
for student in student_scores:
    all_keys = student_scores.keys()
    print(all_keys)

# 2. Write a function that accepts a dictionary and returns a list of all student names (keys).
# print(student_scores.keys())

# 3. Write a function to check if a specific student (key) is present in the dictionary.
alice_exists = 'Alice' in student_scores
print(alice_exists)

# 4. Write a function to count the number of students in the dictionary.
student_count = {}

for student in student_scores: 
    if student in student_count:
        student_count[student] = student_count[student] + 1 
    else: 
        student_count[student] = 1 
print(student_count)

# 5. Write a function that prints all students whose names start with a specific letter.

# 6. Write a function to remove a student from the dictionary using their name (key).
 #del student_count['Alice']

# 7. Write a function to find all students with names of a given length.


# 8. Write a function to check if all students’ names start with a capital letter.


# 9. Write a function to create a list of all students whose names have more than 4 characters.


# 10. Write a function to return a sorted list of student names in alphabetical order.
student_scores = {
    'Blice': 85,
    'Sob': 92,
    'Charlie': 88,
    'Aavid': 79,
    'Eve': 91
}

students_names = student_scores.keys()
students_sorted =sorted(students_names)
print(students_sorted)

# Starting dictionary

student_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 88,
    'David': 79,
    'Eve': 91
}

# 1. Write a function to print all student scores (values) using a for loop.
# student_values = {}

# for student in student_scores: 
#     student_values = student_scores.values()
# print(student_values)    #missed the logic here 


# 2. Write a function that accepts a dictionary and returns a list of all student scores (values).
students_values = student_scores.values()
print(students_values)

# 3. Write a function to check if a specific score (value) is present in the dictionary.


# 4. Write a function to calculate the average score of all students in the dictionary.
# average = 0 

# for key,value in student_scores.items():
#          average = sum(int(value))/len(value)
# print(average)



# 5. Write a function that prints the students who scored above a specific threshold.


# 6. Write a function to remove all students whose scores are below a specific value.


# 7. Write a function to find the highest score among all students in the dictionary.


# 8. Write a function to count how many students have a score greater than or equal to 90.


# 9. Write a function that returns a list of scores in ascending order.


# 10. Write a function to find the sum of all scores in the dictionary.


print(student_scores.keys())

students_values = student_scores.values()
print(students_values)


students_values = student_scores.values()
print(students_values)