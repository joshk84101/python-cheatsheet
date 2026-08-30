# Lists and Dictionaries

## Lists

An ordered collection of items. Use square brackets `[]`.

**When to use:** order matters, duplicates are okay, looping through a simple sequence.

```python
fruits = ["apple", "banana", "cherry"]

fruits[0]          # access by position -> "apple"
fruits.append("orange")   # add to the end
fruits.remove("banana")   # remove a specific item
len(fruits)         # number of items in the list

for fruit in fruits:
    print(fruit)

if "cherry" in fruits:
    print("found it")
```

## Dictionaries

Stores data as key/value pairs. Use curly braces `{}`. Look things up by name (key), not position.

**When to use:** looking things up by label, related pieces of info stored together.

```python
calories = {"apple": 50, "banana": 110}

calories["apple"]        # access by key -> 50
calories.get("mango")      # safe access, returns None if missing
calories["mango"] = 60     # add a new key/value
calories["apple"] = 55     # update a value
del calories["banana"]     # remove a key/value pair

for fruit, cal in calories.items():
    print(fruit, cal)
```

## Common built-in methods/functions

| Name | What it does | Example |
|---|---|---|
| `len()` | returns the number of items in a list, dict, or string | `len(fruits)` -> `3` |
| `.strip()` | removes whitespace (spaces, newlines) from start/end of a string | `" hi ".strip()` -> `"hi"` |
| `.lower()` | converts a string to lowercase | `"APPLE".lower()` -> `"apple"` |
| `.get()` | safely gets a value from a dict, no error if key missing | `calories.get("kiwi")` -> `None` |
| `.append()` | adds an item to the end of a list | `fruits.append("kiwi")` |
| `.items()` | gets key/value pairs from a dict for looping | `for k, v in d.items():` |

## Common mistakes

- Using `[]` when you meant `{}` (list vs dict) — square vs curly brackets
- Forgetting `()` on method calls — `.strip` vs `.strip()`
- Using `calories["mango"]` on a key that doesn't exist (crashes) instead of `.get()` (safe)