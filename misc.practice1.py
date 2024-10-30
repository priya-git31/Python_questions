# Here's our data:
flavors = ["chocolate", "vanilla", "strawberry", "mint"]
ratings = [9, 8, 7, 9]

# 1. Let's combine them into pairs:
def combine_a_b(a,b):
    combined_ab = list(zip(a,b))
    return combined_ab

combined_flavors_ratings = combine_a_b(flavors,ratings)
print(combined_flavors_ratings)

# 2. Make it into a dictionary:
def combine_dict(a,b): 
    combined_dict_ab = dict(zip(a,b))
    return combined_dict_ab

dict_flavors_ratings = combine_dict(flavors,ratings)
print(dict_flavors_ratings)

# 3. Count frequency of ratings:
from collections import Counter 
count_ratings = Counter(ratings)
print(count_ratings)

# 4. Look up one flavor's rating:
def one_ratings(flavour_name, flavour_dictionary):
    rating_result = flavour_dictionary[flavour_name]
    return rating_result

chocolate_rating = one_ratings("chocolate", dict_flavors_ratings)
print(chocolate_rating)

# 5. Find highest rated flavor:
def highest_rated(dictionary_name):
    highest_rated_result = max(dictionary_name, key=dictionary_name.get)
    return highest_rated_result

highest_rated_flavor = highest_rated(dict_flavors_ratings)
print(highest_rated_flavor)

# zip() combines lists into pairs
# dict() turns pairs into a dictionary where you can look things up
# Counter() counts how many times things appear
# Use square brackets [] to look up things in a dictionary
# max() with key=dictionary.get finds the item with the highest value

#7 Finding Total Sum of all the ratings:
def sum_of_all(dictionary_name):
    sum_result = sum(dictionary_name.values())
    return sum_result 

sum_of_ratings = sum_of_all(dict_flavors_ratings)
print(sum_of_ratings)

# Question 8: How would you find the average ratings from the ratings list?
def average_ratings(list_name):
    sum_ratings = sum(list_name)
    length_ratings = len(list_name)
    return_ratings = sum_ratings/length_ratings
    return return_ratings

average_ratings_result = average_ratings(ratings)
print(average_ratings_result)

# Question 9: How can you sort the flavours alphabetically?
def sorting_list(list_name): 
    sorted_list = sorted(list_name)
    return sorted_list

sorted_flavours = sorting_list(flavors)
print(sorted_flavours)

# Question 10: How would you sort the `names_scores_dict` by scores in descending order?

def sorting_desc(dictionary_name): 
    sorting_desc_result = sorted(dictionary_name.items(),
                                 key=lambda x: x[1],
                                 reverse=True)
    return sorting_desc_result

sorting_by_score = sorting_desc(dict_flavors_ratings)
print(sorting_by_score)

# Question 11: What code would you write to find the minimum rating and the corresponding flavour name?

def minimum_f_r(dictionary_name): 
    minimum_fl = min(dictionary_name, key=dictionary_name.get)
    minimum_rg = dictionary_name[minimum_fl]
    return minimum_rg, minimum_fl

minimum_rating_fl = minimum_f_r(dict_flavors_ratings)
print(minimum_rating_fl)