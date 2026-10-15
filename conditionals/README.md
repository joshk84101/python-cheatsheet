# Conditionals

## if / elif / else

Runs different code depending on whether a condition is `True` or `False`.

**When to use:** making decisions, like checking user input or choosing what to print.

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:     # only checked if the first condition was False
    print("B")
elif score >= 70:
    print("C")
else:                 # runs if NONE of the above were True
    print("F")
```

- Python checks from the top down and stops at the **first** `True` condition
- `elif` and `else` are optional
- You can have as many `elif`s as you need, but only one `if` and one `else`

## Comparison operators

| Operator | Meaning | Example |
|---|---|---|
| `==` | equal to | `5 == 5` -> `True` |
| `!=` | not equal to | `5 != 3` -> `True` |
| `<` | less than | `3 < 5` -> `True` |
| `>` | greater than | `3 > 5` -> `False` |
| `<=` | less than or equal to | `5 <= 5` -> `True` |
| `>=` | greater than or equal to | `4 >= 5` -> `False` |
| `in` | is it inside a string, list, or dict | `"a" in "cat"` -> `True` |

## and / or / not

Combine conditions together.

| Operator | True when | Example |
|---|---|---|
| `and` | **both** sides are True | `x > 0 and x < 10` |
| `or` | **at least one** side is True | `x == 1 or x == 2` |
| `not` | flips True to False and False to True | `not x == 5` |

```python
age = 25

if age >= 18 and age < 65:
    print("Working age")

# Python lets you chain comparisons, which reads more naturally:
if 18 <= age < 65:
    print("Working age")
```

## if vs elif (separate checks vs one decision)

```python
x = 5

# Separate ifs: EVERY one is checked, so more than one can run
if x > 0:
    print("positive")
if x > 3:
    print("bigger than 3")     # both lines print

# elif: only ONE branch runs, then it stops
if x > 0:
    print("positive")
elif x > 3:
    print("bigger than 3")     # never reached, first branch already ran
```

**Rule of thumb:** use `elif` when the options are one decision with one answer. Use separate `if`s when each check is its own independent question.

## Returning True / False directly

A comparison already gives you `True` or `False`, so you don't need an `if` to return it.

```python
# Long way
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Short way (does exactly the same thing)
def is_even(n):
    return n % 2 == 0
```

`%` is the remainder operator: `7 % 2` -> `1`, `8 % 2` -> `0`. Very handy for checking even/odd.

## match (Python 3.10+)

A cleaner way to compare one value against lots of exact options.

**When to use:** checking one variable against a list of fixed values (like a menu choice or a name).

```python
name = "Harry"

match name:
    case "Harry" | "Hermione" | "Ron":     # | means "or"
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                                # _ is the catch-all, like else
        print("Who?")
```

The same thing with `if` / `elif`:

```python
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
```

## Common mistakes

- Using `=` (assigns a value) instead of `==` (compares values) in a condition
- Writing `if x == 1 or 2:`, which is always True. It must be `if x == 1 or x == 2:`, or `if x in [1, 2]:`
- Forgetting the colon `:` at the end of an `if`, `elif`, `else`, or `case` line
- Comparing a number to text from `input()`. `input()` always returns a string, so `"5" == 5` is `False`. Convert first with `int()`
- Putting `elif` conditions in the wrong order. `if score >= 70:` before `if score >= 90:` means a score of 95 gets a C
- Using separate `if`s when you meant `elif`, so more than one branch runs
