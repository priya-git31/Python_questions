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