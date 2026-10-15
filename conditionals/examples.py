# IF / ELIF / ELSE

score = 85

if score >= 90:
    print("A")
elif score >= 80:             # only checked if the first condition was False
    print("B")                # prints B, then stops checking
elif score >= 70:
    print("C")
else:                         # runs only if NONE of the above were True
    print("F")


# COMPARISON OPERATORS

print(5 == 5)                 # True, equal to
print(5 != 3)                 # True, not equal to
print(3 < 5)                  # True, less than
print(4 >= 5)                 # False, greater than or equal to
print("a" in "cat")           # True, "a" is inside "cat"
print("kiwi" in ["apple", "banana"])   # False, not in the list


# AND / OR / NOT

age = 25

if age >= 18 and age < 65:    # and: BOTH sides must be True
    print("Working age")

if 18 <= age < 65:            # chained comparison, same as the line above
    print("Working age")

if age == 25 or age == 30:    # or: at least ONE side must be True
    print("25 or 30")

if not age == 40:             # not: flips the result
    print("Not 40")


# IF vs ELIF

x = 5

if x > 0:
    print("positive")         # prints
if x > 3:
    print("bigger than 3")    # also prints, separate ifs are all checked

if x > 0:
    print("positive")         # prints
elif x > 3:
    print("bigger than 3")    # skipped, elif stops after the first True branch


# RETURNING TRUE / FALSE DIRECTLY

def is_even(n):
    return n % 2 == 0         # the comparison already gives True or False

print(is_even(4))             # True
print(is_even(7))             # False
print(7 % 2)                  # 1, % gives the remainder after dividing


# MATCH (Python 3.10+)

name = "Harry"

match name:
    case "Harry" | "Hermione" | "Ron":    # | means "or"
        print("Gryffindor")               # prints Gryffindor
    case "Draco":
        print("Slytherin")
    case _:                               # _ catches anything else, like else
        print("Who?")
