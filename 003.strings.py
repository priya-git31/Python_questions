# len(string): Returns the length (number of characters) of the string.
# string.upper(): Converts all characters in the string to uppercase.
# string.lower(): Converts all characters in the string to lowercase.
# string.capitalize(): Capitalizes the first character of the string.
# string.title(): Converts the string to title case where the first letter of each word is capitalized.

# string.strip(): Removes leading and trailing whitespace characters from the string.
# string.startswith(prefix): Returns True if the string starts with the specified prefix.
# string.endswith(suffix): Returns True if the string ends with the specified suffix.
# string.replace(old, new): Replaces all occurrences of the old substring with the new substring.
# string.split(separator): Splits the string into a list of substrings based on the separator.

# string.join(iterable): Joins a list of strings into one string using the original string as a separator.
# string.find(substring): Returns the index of the first occurrence of a substring in the string.
# string.rfind(substring): Returns the index of the last occurrence of a substring in the string.
# string.isalpha(): Returns True if all characters in the string are alphabetic.
# string.isdigit(): Returns True if all characters in the string are digits.

# string.isalnum(): Returns True if all characters in the string are alphanumeric.
# string.islower(): Returns True if all characters in the string are lowercase.
# string.isupper(): Returns True if all characters in the string are uppercase.
# string.isnumeric(): Returns True if all characters in the string are numeric.
# string.count(substring): Returns the number of non-overlapping occurrences of a substring in the string.

# ------------------------ Questions on string 1
this_string = "Hello, World!"


# How can you convert "Hello, World!" to all lowercase characters?
print(this_string.lower())

# What method would you use to check if String 1 starts with "Hello"?
print(this_string.startswith("Hello"))
      
# How do you find the index of the first occurrence of "o" in String 1?
print(this_string.find("o"))

# What is the result of replacing "Hello" with "Hi" in String 1?
print(this_string.replace("Hello", "Hi"))

# How can you remove leading and trailing whitespace characters from String 1?
stripped_string = this_string.strip()
print(stripped_string )

# What is the output of splitting String 1 by ","?
print(this_string.split(","))

# How would you join the list ["Hello", "World!"] into a single string using a space as a separator?
joined_string = ' '.join(["Hello", "World"])
print(joined_string)

# How do you check if String 1 contains only alphanumeric characters?
isalphanum = this_string.isalnum()
print(isalphanum)

# What is the count of "l" characters in String 1?
count_l = this_string.count("l")
print(count_l)

# Is String 1 ending with an exclamation mark?
ends_with = this_string.endswith("!")
print(ends_with)