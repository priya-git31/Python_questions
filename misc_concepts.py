#1 Lists are like containers that can hold many things
toys = ["teddy bear", "car", "doll", "robot"]
prices = [10, 15, 12, 20]

print("Our toys:", toys)
print("Their prices:", prices)

# Now, let's learn about zip() - think of it like making pairs:
#1
# Imagine you're matching each toy with its price tag
def make_toy_price_pairs(toys_list, prices_list):
    # zip is like taking one item from each list and putting them together
    # list() turns these pairs into something we can see
    pairs = list(zip(toys_list, prices_list))
    return pairs

toy_pairs = make_toy_price_pairs(toys, prices)
print("\nToys with their prices:")
print(toy_pairs)  # Will show: [('teddy bear', 10), ('car', 15), ('doll', 12), ('robot', 20)]

# Each pair is a tuple - a tuple is like a pair that can't be changed
# ('teddy bear', 10) is a tuple - the toy and its price stay together!

#2 Converting our pairs into a dictionary
def make_toy_dictionary(toys_list, prices_list):
    # dict() makes a dictionary where toys are keys and prices are values
    toy_dict = dict(zip(toys_list, prices_list))
    return toy_dict

# Let's try it!
toy_store = make_toy_dictionary(toys, prices)
print("\nOur toy store dictionary:")
print(toy_store)  # Shows: {'teddy bear': 10, 'car': 15, 'doll': 12, 'robot': 20}

# 2.11Now we can easily look up any toy's price!
print(f"The car costs: ${toy_store['car']}")


# 3. Count frequency of toys:

from collections import Counter
toys_frequency = Counter(toys)
print(toys_frequency)

#4.Finding things in dictionaries:
# Looking up one specific price
def find_toy_price(toy_name, toy_dictionary):
    return toy_dictionary[toy_name]

# Let's find the doll's price
doll_price = find_toy_price("doll", toy_store)
print(f"\nThe doll costs: ${doll_price}")

#5. Finding the most expensive toy:

def find_most_expensive_toy(toy_dictionary):
    # max() with key=toy_dictionary.get looks at all prices and finds the highest
    most_expensive = max(toy_dictionary, key=toy_dictionary.get)
    return most_expensive

# Let's find out!
expensive_toy = find_most_expensive_toy(toy_store)
print(f"\nMost expensive toy is: {expensive_toy} at ${toy_store[expensive_toy]}")

#7 Finding Total Sum:
# Let's sum up all toy prices
def get_total_price(toy_dictionary):
    # sum() adds up all the values in the dictionary
    return sum(toy_dictionary.values())

total_toy_cost = get_total_price(toy_store)
print(f"\nTotal of all toy prices: ${total_toy_cost}")

#8 Finding Averages:
# Average toy price
def get_average_price(toy_dictionary):
    total = sum(toy_dictionary.values())  # Add up all prices
    count = len(toy_dictionary)           # Count how many toys
    return total / count                  # Divide total by count

avg_toy_price = get_average_price(toy_store)
print(f"\nAverage toy price: ${avg_toy_price}")

#9. Sorting Names Alphabetically:
# Sort toy names
def sort_toy_names(toy_dictionary):
    # Get the names and sort them
    return sorted(toy_dictionary.keys())

sorted_toys = sort_toy_names(toy_store)
print("\nToys in alphabetical order:")
print(sorted_toys)


#10 Sort toys by price (highest to lowest)
def sort_by_price(toy_dictionary):
    # sorted() with lambda function tells Python to look at the prices
    # reverse=True means highest to lowest
    return sorted(toy_dictionary.items(), 
                 key=lambda x: x[1],  # x[1] means look at the price
                 reverse=True)        # reverse=True means highest first

expensive_to_cheap = sort_by_price(toy_store)
print("\nToys from most to least expensive:")
for toy, price in expensive_to_cheap:
    print(f"{toy}: ${price}")


#12.

# Using list comprehension
expensive_toys = {toy: price for toy, price in toy_store.items() 
                 if price > 10}
print("\nExpensive toys (comprehension):")
print(expensive_toys)

# Using loop
def find_expensive_toys(toy_dict, price_limit):
    expensive = {}
    for toy, price in toy_dict.items():
        if price > price_limit:
            expensive[toy] = price
    return expensive