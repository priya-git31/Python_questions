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

