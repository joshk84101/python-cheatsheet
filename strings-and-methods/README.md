# Strings and Other Common Methods

## What is a string?

Text, wrapped in quotes (single `'...'` or double `"..."`, doesn't matter which as long as you're consistent).

```python
name = "Josh"
```

## Common string methods

| Method | What it does | Example |
|---|---|---|
| `.strip()` | removes whitespace from start/end | `"  hi  ".strip()` -> `"hi"` |
| `.lower()` | converts to lowercase | `"APPLE".lower()` -> `"apple"` |
| `.upper()` | converts to uppercase | `"apple".upper()` -> `"APPLE"` |
| `.title()` | capitalizes the first letter of each word | `"josh kelly".title()` -> `"Josh Kelly"` |
| `.capitalize()` | capitalizes only the first letter of the string | `"hello world".capitalize()` -> `"Hello world"` |
| `.replace(old, new)` | replaces one substring with another | `"hi bob".replace("bob", "sam")` -> `"hi sam"` |
| `.split()` | splits a string into a **list**, by spaces by default. **Returns a list of strings, not a single string.** | `"a b c".split()` -> `["a", "b", "c"]` |
| `.join()` | joins a list into a string, using the string as the separator | `"-".join(["a", "b"])` -> `"a-b"` |
| `.startswith()` | checks if a string starts with something | `"hello".startswith("he")` -> `True` |
| `.endswith()` | checks if a string ends with something | `"hello".endswith("lo")` -> `True` |
| `.find()` | returns the index of a substring, or -1 if not found | `"hello".find("l")` -> `2` |
| `.index()` | returns the index of the first occurrence of a value, but **crashes with a ValueError if it's not found** (unlike `.find()`, which returns -1 instead). Works on lists too, not just strings, this is how you'd look up a value's position in a list, like matching a month name to its number. | `"hello".index("l")` -> `2`, or `["January", "February", "March"].index("March")` -> `2` |
| `.count()` | counts how many times something appears | `"hello".count("l")` -> `2` |
| `.isdigit()` | checks if a string is made up only of digits | `"123".isdigit()` -> `True` |
| `.isalpha()` | checks if a string is made up only of letters | `"abc".isalpha()` -> `True` |

## String slicing (grabbing part of a string)

```python
word = "hello"

word[0]      # "h" (first letter)
word[-1]     # "o" (last letter)
word[0:3]    # "hel" (characters from index 0 up to, not including, 3)
word[:2]     # "he" (from the start up to index 2)
word[2:]     # "llo" (from index 2 to the end)
```

## f-strings (formatting text with variables inside)

```python
name = "Josh"
age = 22

print(f"My name is {name} and I am {age}")
# -> My name is Josh and I am 22
```

## Common type conversion functions

These aren't string-specific, but you'll use them constantly alongside strings.

| Function | What it does | Example |
|---|---|---|
| `str()` | converts something to a string | `str(5)` -> `"5"` |
| `int()` | converts something to a whole number | `int("5")` -> `5` |
| `float()` | converts something to a decimal number | `float("5.5")` -> `5.5` |
| `len()` | length of a string, list, or dict | `len("hello")` -> `5` |
| `type()` | tells you what type something is | `type(5)` -> `<class 'int'>` |

## Common mistakes

- Forgetting that `.strip()`, `.lower()`, etc. return a **new** string, they don't change the original unless you reassign it: `name = name.strip()`
- Mixing up `.find()` (returns -1 if not found) with `.index()` (crashes with ValueError if not found) with `in` (returns True/False)
- Forgetting that `.split()` gives you back a **list**, not a string, so you access pieces of it by position, like `parts[0]`, not by string methods directly
- Trying to do `int("hello")`, this crashes because "hello" isn't a valid number
- Off-by-one confusion with slicing, remember the end index is NOT included
- Off-by-one confusion with `.index()` on a list, it counts from 0, so the 9th item in a list sits at index 8, not 9
