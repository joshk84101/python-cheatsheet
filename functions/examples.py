# BASIC FUNCTION

def greet():
    print("Hello!")

greet()          # calling the function runs the code inside it
greet()          # can call it again as many times as you want


# PARAMETERS

def greet_name(name):        # "name" is the parameter
    print(f"Hello, {name}")

greet_name("Josh")           # "Josh" is the argument, gets plugged into "name"
greet_name("Sarah")


def add(x, y):
    print(x + y)

add(2, 3)         # prints 5


# RETURN VALUES

def add_return(x, y):
    return x + y            # sends the result back out of the function

result = add_return(2, 3)   # result now holds 5, ready to use
print(result)


# PRINT vs RETURN

def add_print(x, y):
    print(x + y)            # just displays it, doesn't hand back a usable value

a = add_print(2, 3)         # a is None, because print() doesn't return anything
b = add_return(2, 3)        # b is 5, because return actually hands the value back

print(a)
print(b)


# DEFAULT PARAMETER VALUES

def greet_default(name="friend"):
    print(f"Hello, {name}")

greet_default()          # uses the default -> "Hello, friend"
greet_default("Josh")    # overrides the default -> "Hello, Josh"


# SCOPE

def make_total():
    total = 10               # total only exists inside make_total()
    return total             # return is how you get the value out

print(make_total())          # prints 10
# print(total)               # would crash with NameError, total doesn't exist out here


# MAIN() AND if __name__ == "__main__":

def main():
    print(square(3))         # main() holds the program's main logic


def square(n):
    return n * n             # helper functions can sit below main()


if __name__ == "__main__":   # True only when you run this file directly
    main()                   # so main() doesn't run if another file imports this one
