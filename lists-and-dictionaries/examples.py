# LISTS

fruits = ["apple", "banana", "cherry"]

print(fruits[0])          # access by position -> "apple"
fruits.append("orange")   # add "orange" to the end of the list
fruits.remove("banana")   # remove "banana" from the list
print(len(fruits))        # print how many items are in the list

for fruit in fruits:
    print(fruit)          # print each fruit, one at a time

if "cherry" in fruits:
    print("found it")     # only runs if "cherry" is in the list


# DICTIONARIES

calories = {"apple": 50, "banana": 110}

print(calories["apple"])         # access value by key -> 50
print(calories.get("mango"))     # safe access, returns None (no error) if key is missing
calories["mango"] = 60           # add a new key/value pair
calories["apple"] = 55           # update an existing value
del calories["banana"]           # remove a key/value pair

for fruit, cal in calories.items():
    print(fruit, cal)            # print each key and value together


# COMMON METHODS/FUNCTIONS

print(len(fruits))                # number of items in a list, dict, or string
print("  hi  ".strip())           # removes whitespace from start/end -> "hi"
print("APPLE".lower())            # converts to lowercase -> "apple"