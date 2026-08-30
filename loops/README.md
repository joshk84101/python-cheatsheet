# Loops

## For loops

Goes through items one at a time, a fixed number of times (or once per item in something).

**When to use:** looping through a list/dict/string, or when you know how many times to repeat.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):      # 1, 2, 3, 4, 5 (stop is not included)
    print(i)

for i in range(0, 10, 2):    # 0, 2, 4, 6, 8 (step = jump size)
    print(i)

calories = {"apple": 50, "banana": 110}
for fruit, cal in calories.items():
    print(fruit, cal)
```

## While loops

Keeps going as long as a condition is `True`. Used when you don't know in advance how many times it'll run.

**When to use:** waiting on a condition, validating user input.

```python
count = 0
while count < 3:      # condition checked BEFORE each loop
    print(count)
    count += 1        # this eventually makes the condition False

# while True + break: for when the condition can't be checked
# until AFTER you already have some input
while True:
    fruit = input("Item: ").strip().lower()
    if fruit != "":
        break     # manually exit the loop
```

## break and continue

```python
for number in range(10):
    if number == 5:
        break     # exits the loop completely

for number in range(5):
    if number == 2:
        continue    # skips this one, keeps looping
    print(number)
```

## Common mistakes

- Forgetting to update the variable in a `while` loop (causes infinite loop)
- Using `while True` without a `break` inside it
- Mixing up `range(5)` (stops before 5) with wanting to count 1 to 5