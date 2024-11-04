# Create your own lists of:
# 1. Three favorite books
# 2. Their page counts

books = ["Harry Potter", "Percy Jackson", "Matilda"]
pages = [300, 250, 200,]

#1 Combine them into pairs
# Imagine you're matching each book with its pages count
def combined_pairs_a_b(a,b):
    # zip is like taking one item from each list and putting them together
    # list() turns these pairs into something we can see
    combined_pair = list(zip(a,b))
    return combined_pair
# Each pair is a tuple - a tuple is like a pair that can't be changed

combined_pair_result = combined_pairs_a_b(books,pages)
print(combined_pair_result)

#2 - Make a dictionary
def combined_a_b_dict(a,b):
    # dict() makes a dictionary where books are keys and pages are values
    combined_dict = dict(zip(a,b))
    return combined_dict

combined_dict_result = combined_a_b_dict(books,pages)
print(combined_dict_result)

#2.1 Now we can easily look up any book's price!

print(f"The book's price: ${combined_dict_result['Matilda']}")

# 3. Count frequency of prices:

from collections import Counter
pages_frequency = Counter(pages)
print(pages_frequency)

#4. Finding things in a dictionary
# Looking up one specific price
def book_prices(book_name,book_dictionary):
    return book_dictionary[book_name]

book_price_result = book_prices("Percy Jackson",combined_dict_result)
print(book_price_result)

#5 Finding the most expensive book:

def most_expensive_book(sample_dictionary):
    book_result = max(sample_dictionary, key=sample_dictionary.get)
    return book_result

most_exp_book_result = most_expensive_book(combined_dict_result)
print(most_exp_book_result)

#7 sum up all the pages count 
def sum_of_all(dictionary_name):
    sum_eveyrthing = sum(dictionary_name.values())
    return sum_eveyrthing

sum_of_pages = sum_of_all(combined_dict_result)
print(sum_of_pages)

# Question 8: How would you find the average pages from the pages list?
def average_result(list_name):
    sum_list = sum(list_name)
    length_list = len(list_name)
    average_return = sum_list/length_list
    return average_return

average_pages = average_result(pages)
print(average_pages)

# Question 9: How can you sort the books alphabetically?
def sorting_list(list_name): 
    sorted_list = sorted(list_name)
    return sorted_list 

sorted_books = sorting_list(books)
print(sorted_books)

# Question 10: How would you sort the `combined_dict_result` by scores in descending order?
def sorting_by_values(dictionary_name): 
    sorted_result = sorted(dictionary_name.items(), key=lambda x: x[1], reverse=True)
    return sorted_result

sorted_by_scores = sorting_by_values(combined_dict_result)
print(sorted_by_scores)

# Question 11: What code would you write to find the minimum pages and the corresponding book name?

def minimum(dictionary_name):
    minimum_book_name = min(dictionary_name, key=dictionary_name.get)
    minimum_pages = dictionary_name[minimum_book_name]
    return  minimum_pages, minimum_book_name

min_book_name = minimum(combined_dict_result)
print(min_book_name)

# Question 12: How can you filter out books with pages greater than 250?
#using comprehension
def filter_books(page_number,dictionary_name): 
    filtered_books = { books : pages
                      for books,pages in combined_dict_result.items()
                      if pages > page_number}
    return filtered_books

result = filter_books(250, combined_dict_result)
print(result)

#uisng lists 
def filter_books(page_number,dictionary_name): 
    filtered_books = {}
    for books,pages in dictionary_name.items(): 
        if pages > page_number: 
            filtered_books[books] = pages 
            return filtered_books 

result = filter_books(250, combined_dict_result)
print(result)

# Question 13: Can you create a new list that contains the length of each book?
def new_list(dictionary_name): 
    return [len(book) for book in dictionary_name.keys()]

result = new_list(combined_dict_result)
print(result)

# Question 14: How would you check if the book 'Matilda' is in the `combined_dict_result`?

def is_book_present(dictionary_name, certain_book): 
    is_present = certain_book in dictionary_name
    return is_present 

result = is_book_present(combined_dict_result, 'Matilda')
print(result)

# Question 15: How can you update 'Percy Jackson's pages to 90 in the `combined_dict_result`?

def updates(dictionary_name,update_name,update_num): 
    result = dictionary_name[update_name] = update_num 
    return result 

result = updates(combined_dict_result,'Percy Jackson', 90)
print(result)
print(combined_dict_result)

# Question 16: What would you do to remove 'Matilda' and their pages from the dictionary?
# def remove_entries(dictionary_name,del_name): 
#     result = dictionary_name.pop(del_name)
#     return result 

# result = remove_entries(combined_dict_result,'Matilda')
# print(result)
# print(combined_dict_result)

# Question 17: Can you find the number of unique pages in the `pages` list?

def unique_pages(list_name): 
    result = set(list_name)
    return result 

result = unique_pages(pages)
print(result)

# Question 18: How would you merge two dictionaries if you had another dictionary with additional books and pages?

temp_dict = {"Pride and Prejudice" : 400, "Dracula" : 700}

def adding_dict(original_dict,new_dict): 
    combined = original_dict.copy()
    combined.update(new_dict)
    return combined 

result = adding_dict(combined_dict_result, temp_dict)
print(result)


# Question 20: Can you reverse the order of the `books` list?

def reverse_list(list_name): 
    result = list_name.reverse()
    return result 

result = reverse_list(books)
print(result)
print(books)

# Question 21: How can you extract all the pages from the dictionary into a separate list?
def seperate_list(dictionary_name): 
    new_list = list(dictionary_name.values())
    return new_list 

result = seperate_list(combined_dict_result)
print(result)

# Question 23: Can you create a set from the `books` list to remove duplicates if there were any?
def set_list(list_name): 
    result = set(list_name)
    return result 

result = set_list(books)
print(result)

#SECTION II 


movies = ["Inception", "Avatar", "Matrix", "Inception", "Avatar", "Titanic"]
ratings = [8.8, 7.8, 8.7, 8.8, 7.8, 7.9]
movie_details = {
    "Inception": {"year": 2010, "genre": "sci-fi"},
    "Avatar": {"year": 2009, "genre": "fantasy"},
    "Matrix": {"year": 1999, "genre": "sci-fi"},
    "Titanic": {"year": 1997, "genre": "drama"}
}
viewer_preferences = {
    "John": ["sci-fi", "fantasy"],
    "Emma": ["drama", "fantasy"],
    "Mike": ["sci-fi", "drama"]
}

# Write a function that returns all unique genres from the movie_details dictionary.
movie_details = {
    "Inception": {"year": 2010, "genre": "sci-fi"},
    "Avatar": {"year": 2009, "genre": "fantasy"},
    "Matrix": {"year": 1999, "genre": "sci-fi"},
    "Titanic": {"year": 1997, "genre": "drama"}
}

print(movie_details)

def unique_genre(dict_name): 
    result = set(dict_name.values())
    return result 

answer = unique_genre(movie_details)
print(answer)

