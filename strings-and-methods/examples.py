# STRING METHODS

name = "  Josh Kelly  "

print(name.strip())            # removes whitespace from start/end -> "Josh Kelly"
print(name.lower())            # converts to lowercase
print(name.upper())            # converts to uppercase
print(name.strip().title())    # capitalizes each word (strip first so spacing doesn't mess it up)
print("hello world".capitalize())   # capitalizes only the first letter -> "Hello world"

message = "hi bob"
print(message.replace("bob", "sam"))   # replaces "bob" with "sam" -> "hi sam"

words = "a b c".split()        # splits into a list -> ["a", "b", "c"]
print(words)

joined = "-".join(["a", "b"])  # joins list items with "-" between them -> "a-b"
print(joined)

print("hello".startswith("he"))   # True
print("hello".endswith("lo"))     # True
print("hello".find("l"))          # 2 (index of first "l")
print("hello".count("l"))         # 2 (how many "l"s)
print("123".isdigit())            # True (all characters are digits)
print("abc".isalpha())            # True (all characters are letters)


# STRING SLICING

word = "hello"
print(word[0])       # "h" (first letter)
print(word[-1])      # "o" (last letter)
print(word[0:3])     # "hel" (index 0 up to, not including, 3)
print(word[:2])      # "he" (start up to index 2)
print(word[2:])      # "llo" (index 2 to the end)


# F-STRINGS

age = 22
print(f"My name is Josh and I am {age}")   # inserts the variable directly into the string


# TYPE CONVERSION

print(str(5))          # "5" (number turned into a string)
print(int("5"))        # 5 (string turned into a whole number)
print(float("5.5"))    # 5.5 (string turned into a decimal number)
print(len("hello"))    # 5 (length of the string)
print(type(5))         # <class 'int'>