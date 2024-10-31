
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
def filter_scores(dictionary_name): 
    filter_name = min(dictionary_name, key=dictionary_name.get)
    filter_score = dictionary_name[filter_name]
    return filter_score, filter_name

result = filter_scores(names_scores_dict)
print(result)

# Question 12: How can you filter out names with scores greater than 90?
#coprehension
def filter_scores(dictionary_name, set_score): 
    filtered_scores = {names: scores
                      for names, scores in dictionary_name.items()
                      if scores > set_score}
    return filtered_scores

result = filter_scores(names_scores_dict,90)
print(result)

#lists 
def filter_scores(dictionary_name, set_score): 
    filtered_scores = {}
    for name, score in dictionary_name.items(): 
        if score > set_score:
            filtered_scores[name] = score
    return filtered_scores

result = filter_scores(names_scores_dict, 90)
print(result)

# Question 13: Can you create a new list that contains the length of each name?
def length_new(dictionary_name): 
    return [len(name) for name in dictionary_name.keys()]

result = length_new(names_scores_dict)
print(result)

# Question 14: How would you check if the name 'David' is in the `names_scores_dict`?
def is_name_present(names_scores_dict, certain_name): 
    is_present = certain_name in names_scores_dict
    return is_present

result = is_name_present(names_scores_dict,'David')
print(result)

# Question 15: How can you update 'Alice's' score to 90 in the `names_scores_dict`?
def updates(dictionary_name, new_score, up_name): 
    updated_name = dictionary_name[up_name] = new_score
    return updated_name

result = updates(names_scores_dict,90,'Alice')
print(result)

# Question 16: What would you do to remove 'Charlie' and their score from the dictionary?

def remove_entry(dictionary_name,certain_name): 
    del_entry = dictionary_name.pop(certain_name)
    return del_entry 

result = remove_entry(names_scores_dict,'Charlie')
print(result)
print(names_scores_dict)

# Question 17: Can you find the number of unique scores in the `scores` list?
def unique_scores(list_name): 
    result = set(list_name)
    return result 

result = unique_scores(scores)
print(result)

# Question 18: How would you merge two dictionaries if you had another dictionary with additional names and scores?
temp_dict = {"Allsion" : 100, "Carl" : 23}

def merge_dict(old_dict,new_dict): 
    combined = old_dict.copy()
    combined.update(new_dict)
    return combined 

result = merge_dict(names_scores_dict,temp_dict)
print(result)

# Question 19: How would you calculate the average length of names in the `names` list?
# def avg_name_length(dictionary_name): 
#     names = list(dictionary_name.keys())
#     for name in names: 
#         return len(names)
    
# result = avg_name_length(names_scores_dict)
# print(result)

# Question 20: Can you reverse the order of the `names` list?

def reverse_list(my_list): 
    result = my_list.reverse()
    return(result)

result = reverse_list(names)
print(result)
print(names)

# Question 21: How can you extract all the scores from the dictionary into a separate list?



# Question 22: How would you find the median score if the `scores` list was unsorted?
# Question 23: Can you create a set from the `names` list to remove duplicates if there were any?

