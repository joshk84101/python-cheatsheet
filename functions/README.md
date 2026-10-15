# Functions

## What is a function?

A reusable block of code that you can run whenever you need it, instead of copying and pasting the same code over and over.

```python
def greet():
    print("Hello!")

greet()   # calling the function runs the code inside it
greet()   # can call it again as many times as you want
```

## Parameters (inputs to a function)

A parameter is a variable that lives inside the function, and gets filled in with whatever value you pass when you call it.

```python
def greet(name):        # "name" is the parameter
    print(f"Hello, {name}")

greet("Josh")            # "Josh" is the argument, gets plugged into "name"
greet("Sarah")
```

You can have multiple parameters:

```python
def add(x, y):
    print(x + y)

add(2, 3)     # prints 5
```

## Default parameter values

You can give a parameter a default value. If you don't pass anything, the default is used.

```python
def greet(name="friend"):
    print(f"Hello, {name}")

greet()          # uses the default -> "Hello, friend"
greet("Josh")    # overrides the default -> "Hello, Josh"
```

## Return values (getting a result out of a function)

`print()` just displays something, it doesn't give you a value back to use elsewhere. `return` actually hands a value back, so you can store it in a variable and use it later.

```python
def add(x, y):
    return x + y     # sends the result back out of the function

result = add(2, 3)    # result now holds 5
print(result)
```

**Key difference:**

```python
def add_print(x, y):
    print(x + y)      # just displays it, doesn't give you anything usable

def add_return(x, y):
    return x + y      # gives you a usable value

a = add_print(2, 3)    # a is None, because print() doesn't return anything
b = add_return(2, 3)   # b is 5, because return hands the value back

print(a)    # None
print(b)    # 5
```

**Rule of thumb:** if you need to use the result somewhere else (store it, compare it, test it), use `return`.

## Scope (where a variable exists)

A variable created inside a function only exists inside that function. Once the function finishes, it's gone.

```python
def make_total():
    total = 10      # total only exists inside make_total()
    return total

print(make_total())   # 10
print(total)          # NameError, total doesn't exist out here
```

To get a value out of a function, `return` it. Don't rely on variables leaking out.

## The main() pattern

Instead of writing code loose at the top level, put your program's main logic in a function called `main()`, and call it at the bottom of the file.

**Why:** Python reads files top to bottom. Putting everything in `main()` means all your other functions are defined before anything runs, so you can write `main()` first at the top and keep helper functions underneath.

```python
def main():
    name = input("Name: ")
    print(greet(name))


def greet(name):
    return f"Hello, {name}"


main()
```

## if __name__ == "__main__":

This line goes at the bottom of the file instead of a bare `main()` call.

```python
def main():
    print(square(3))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
```

**What it means:**
- When you **run** the file directly (`python square.py`), `__name__` is set to `"__main__"`, so `main()` runs
- When another file **imports** it (`from square import square`), `__name__` is the file's name instead, so `main()` does NOT run

**When to use:** always, in any file with a `main()`. It lets you import your functions into another file (like a test file) without the whole program running and asking for input.

## Common mistakes

- Forgetting the `()` when calling a function: `greet` does nothing, `greet()` runs it
- Using `print()` inside a function when you actually needed `return`, then getting `None` back
- Code after a `return` line never runs, because `return` exits the function immediately
- Trying to use a variable outside the function it was created in (causes `NameError`)
- Calling a function before it's defined, when the call is loose at the top level (the `main()` pattern avoids this)
- Writing `if __name__ == "main":` (missing the double underscores around `main`)
