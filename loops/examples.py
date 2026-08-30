# FOR LOOPS

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)              # prints each fruit in the list

for i in range(5):
    print(i)                  # prints 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)                  # prints 1, 2, 3, 4, 5 (stop is not included)

for i in range(0, 10, 2):
    print(i)                  # prints 0, 2, 4, 6, 8 (step = jump size)

calories = {"apple": 50, "banana": 110}
for fruit, cal in calories.items():
    print(fruit, cal)         # prints each key and value together


# WHILE LOOPS

count = 0
while count < 3:              # condition checked BEFORE each loop
    print(count)
    count += 1                # this eventually makes the condition False

# while True + break: keep looping until we manually decide to stop
while True:
    fruit = input("Item: ").strip().lower()
    if fruit != "":
        break                 # exits the loop once the user types something


# BREAK AND CONTINUE

for number in range(10):
    if number == 5:
        break                 # exits the loop completely once number hits 5
    print(number)

for number in range(5):
    if number == 2:
        continue              # skips printing 2, but keeps looping
    print(number)