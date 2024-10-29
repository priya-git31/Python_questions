# Create your own lists of:
# 1. Three favorite books
# 2. Their page counts

books = ["Harry Potter", "Percy Jackson", "Matilda"]
pages = [300, 250, 200]

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

# Finding the most expensive book:

def most_expensive_book(sample_dictionary):
    book_result = max(sample_dictionary, key=sample_dictionary.get)
    return book_result

most_exp_book_result = most_expensive_book(combined_dict_result)
print(most_exp_book_result)