# TRY / EXCEPT

try:
    x = int("cat")                # this fails, "cat" isn't a number
    print(x)                      # skipped, Python jumps straight to except
except ValueError:
    print("That's not a number")  # prints this instead of crashing


# ELSE

try:
    x = int("42")                 # this works
except ValueError:
    print("That's not a number")  # skipped, no error happened
else:
    print(f"You typed {x}")       # runs only because try worked


# CATCHING MORE THAN ONE EXCEPTION

for value in ["10", "cat", "0"]:
    try:
        result = 100 / int(value)
        print(result)             # "10" -> 10.0
    except ValueError:
        print("Not a number")     # "cat" -> ValueError
    except ZeroDivisionError:
        print("Can't divide by zero")   # "0" -> ZeroDivisionError


# COMMON EXCEPTIONS (each one caught so the file keeps running)

try:
    "5" + 5                       # TypeError: can't add text and a number
except TypeError:
    print("TypeError")

try:
    {"a": 1}["b"]                 # KeyError: "b" isn't a key in the dict
except KeyError:
    print("KeyError")

try:
    [1, 2, 3][5]                  # IndexError: there's no position 5
except IndexError:
    print("IndexError")


# PASS

try:
    x = int("cat")
except ValueError:
    pass                          # do nothing, carry on quietly


# KEEP ASKING UNTIL VALID

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))   # return exits the loop AND the function
        except ValueError:
            pass                        # bad input, loop round and ask again

# n = get_int("Number: ")             # uncomment to try it


# ENDING A LOOP WITH CTRL+D (EOFError)

def collect_names():
    names = []
    try:
        while True:
            names.append(input("Name: "))
    except EOFError:                    # Ctrl+D (Mac/Linux) or Ctrl+Z + Enter (Windows)
        print()                         # moves to a new line after ^D
        return names

# print(collect_names())              # uncomment to try it


# RAISE

def generate_integer(level):
    if level == 1:
        return 5
    else:
        raise ValueError("Invalid level")   # stops with your own error message

try:
    generate_integer(4)
except ValueError as e:               # "as e" stores the error so you can print it
    print(e)                          # prints: Invalid level
