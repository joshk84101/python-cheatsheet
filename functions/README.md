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

a = add_print(2, 3)    #