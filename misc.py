
# Two sample lists
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [85, 92, 78, 88, 95]

# Question 1: Can you combine these two lists into a list of tuples?
def combined_list(a,b):
    combined_list_ex = list(zip(a,b))
    return combined_list_ex

combined_names_scores = combined_list(names,scores)
print(combined_names_scores)

# Question 2: Can you convert the zipped list into a dictionary?
def combined_dict(a,b):
    combined_dict_ex = dict(zip(a,b))
    return combined_dict_ex

names_scores_dict = combined_dict(names,scores)
print(names_scores_dict)


# Question 3: What is the frequency of scores using Counter?
from collections import Counter
scores_frequency = Counter(scores)
print(scores_frequency)

# Question 4: If you want to access Charlie's score, how would you do that from the dictionary?
def access_scores(names,names_scores_dict):
    return names_scores_dict[names]

Charlie_score = access_scores("Charlie", names_scores_dict)
print(Charlie_score)
 

# Question 5: Can you find the name with the highest score?
def highest_score(names_scores_dict):
    highest_score_return = max(names_scores_dict, key=names_scores_dict.get)
    return highest_score_return 

name_highest_score = highest_score(names_scores_dict)
print(name_highest_score)

# Question 6: How would you create a list of only the names?

# Question 7: How would you find the total sum of all scores?
def sum_of_values(dictionary_name):
    summed_result = sum(dictionary_name.values())
    return summed_result 

sum_of_scores = sum_of_values(names_scores_dict)
print(sum_of_scores)    

# Question 8: How would you find the average score from the `scores` list?
def average_scores_list(list_name): 
    sum_list = sum(list_name)
    len_list = len(list_name)
    avg_list = sum_list/len_list
    return avg_list 

avg_scores_result = average_scores_list(scores)
print(avg_scores_result)

# Question 9: How can you sort the names alphabetically?
def sort_names(list_name):
    sorted_names = sorted(names)
    return sorted_names

names_sort = sort_names(names)
print(names_sort)

# Question 10: How would you sort the `names_scores_dict` by scores in descending order?
def sort_by_values(dictionary_name): 
    sort_result = sorted(dictionary_name.items(), key=lambda x: x[1], reverse=True)
    return sort_result 

sort_by_scores = sort_by_values(names_scores_dict)
print(sort_by_scores)


# Question 11: What code would you write to find the minimum score and the corresponding name?
# Question 12: How can you filter out names with scores greater than 90?
# Question 13: Can you create a new list that contains the length of each name?
# Question 14: How would you check if the name 'David' is in the `names_scores_dict`?
# Question 15: How can you update 'Alice's' score to 90 in the `names_scores_dict`?
# Question 16: What would you do to remove 'Charlie' and their score from the dictionary?
# Question 17: Can you find the number of unique scores in the `scores` list?
# Question 18: How would you merge two dictionaries if you had another dictionary with additional names and scores?
# Question 19: How would you calculate the average length of names in the `names` list?
# Question 20: Can you reverse the order of the `names` list?
# Question 21: How can you extract all the scores from the dictionary into a separate list?
# Question 22: How would you find the median score if the `scores` list was unsorted?
# Question 23: Can you create a set from the `names` list to remove duplicates if there were any?

