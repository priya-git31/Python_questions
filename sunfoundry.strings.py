
# 4 Python Program to Replace All Occurrences of ‘a’ with $ in a String
# string_input = input("Enter a string: ")

# def replace_string(given_string,existing,replaced): 
#     result = given_string.replace(existing, replaced)
#     return result

# result = replace_string(string_input, "a", "$")
# print(result)   


# # Python Program to Remove the nth Index Character from a Non-Empty String
# string_input = input("Enter a string: ")
# srting_index_remove = int(input("Enter the index: "))

# def remove_string_index(given_string,index_num): 
#     removed_string = given_string.pop[2]
#     return given_string 

# result = remove_string_index(string_input,srting_index_remove)
# print(result)

# Python Program to Replace Every Blank Space with Hyphen in a String
string_input = input("Enter a string: ")

def replace_string(given_string,existing,replaced): 
    result = given_string.replace(existing, replaced)
    return result

result = replace_string(string_input, " ", "-")
print(result) 