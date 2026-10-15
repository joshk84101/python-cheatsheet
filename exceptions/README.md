# Exceptions

## What is an exception?

An error that happens while your program is running. If you don't handle it, the program crashes and prints a "Traceback".

```python
x = int("cat")
# ValueError: invalid literal for int() with base 10: 'cat'
```

## Common exceptions

| Exception | When it happens | Example that causes it |
|---|---|---|
| `ValueError` | right type, but a value that doesn't make sense | `int("cat")` |
| `TypeError` | wrong type for the operation | `"5" + 5` |
| `NameError` | using a variable that doesn't exist | `print(totl)` (typo) |
| `ZeroDivisionError` | dividing by zero | `10 / 0` |
| `KeyError` | dict key doesn't exist | `{"a": 1}["b"]` |
| `IndexError` | list position doesn't exist | `[1, 2, 3][5]` |
| `EOFError` | user presses **Ctrl+D** during `input()` | |
| `KeyboardInterrupt` | user presses **Ctrl+C** | |

## try / except

Put the code that might fail in `try`. If it fails, Python jumps to `except` instead of crashing.

**When to use:** anything that depends on outside input, like converting what the user types.

```python
try:
    x = int(input("Number: "))
    print(f"You typed {x}")
except ValueError:
    print("That's not a number")
```

- If `int()` works, the `except` block is skipped
- If `int()` fails, Python skips the rest of `try` and runs `except`

## else

Runs only if the `try` block worked (no error). Keeps `try` focused on just the line that might fail.

```python
try:
    x = int(input("Number: "))
except ValueError:
    print("That's not a number")
else:
    print(f"You typed {x}")     # only runs if no error happened
```

## Catching more than one exception

```python
try:
    result = 10 / int(input("Number: "))
except ValueError:
    print("That's not a number")
except ZeroDivisionError:
    print("Can't divide by zero")

# Or handle several the same way:
try:
    result = 10 / int(input("Number: "))
except (ValueError, ZeroDivisionError):
    print("Invalid input")
```

## pass (ignore the error silently)

`pass` means "do nothing". Useful when you just want to ask again without printing a message.

```python
try:
    x = int(input("Number: "))
except ValueError:
    pass
```

## The "keep asking until valid" pattern

The most useful pattern from CS50. Combines `while True`, `try`, and `return`.

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))   # return exits the loop AND the function
        except ValueError:
            pass                        # bad input, loop round and ask again


n = get_int("Number: ")
```

```
Number: cat
Number: 4.5
Number: 7
```

## Ending a loop with Ctrl+D (EOFError)

Some programs keep collecting input until the user presses **Ctrl+D** (Mac/Linux) or **Ctrl+Z then Enter** (Windows).

```python
names = []

try:
    while True:
        names.append(input("Name: "))
except EOFError:
    print()                    # moves to a new line after ^D
    print(names)
```

## raise (throwing your own error)

Use `raise` to stop the program on purpose when something is wrong.

```python
def generate_integer(level):
    if level == 1:
        return 5
    else:
        raise ValueError("Invalid level")


try:
    generate_integer(4)
except ValueError as e:     # "as e" stores the error so you can use it
    print(e)                # Invalid level
```

## Common mistakes

- Using a bare `except:` with no error type. It catches everything, even Ctrl+C and your own typos, which hides real bugs. Name the error: `except ValueError:`
- Putting too much code in `try`. Only wrap the line that might fail, and put the rest in `else`
- Using a variable that was meant to be set in `try` after it failed. If `x = int(...)` failed, `x` was never created, so using it later causes `NameError`
- Catching `KeyboardInterrupt` (Ctrl+C) when the program should end on `EOFError` (Ctrl+D)
- Forgetting the `while True` loop, so the user only gets one chance to type a valid value
