# Run this file with:  python examples.py Josh Sarah
# The third-party packages need installing first:  pip install pyfiglet emoji inflect

import random
import statistics
import sys


# IMPORT STYLES

from random import randint            # now you can call randint() without "random."
import statistics as stats            # a nickname, now stats.mean() works too

print(randint(1, 6))                  # random number from 1 to 6
print(stats.mean([2, 4, 6]))          # 4


# RANDOM

print(random.randint(1, 10))          # random whole number from 1 to 10 (both ends included)
print(random.choice(["heads", "tails"]))   # picks one item from the list

cards = ["jack", "queen", "king"]
random.shuffle(cards)                 # shuffles the list in place, returns None
print(cards)                          # e.g. ['king', 'jack', 'queen']


# STATISTICS

print(statistics.mean([100, 90, 80]))     # 90, the average
print(statistics.median([1, 3, 9]))       # 3, the middle value


# SYS.ARGV

print(sys.argv)                       # e.g. ['examples.py', 'Josh', 'Sarah']
print(len(sys.argv))                  # how many words were typed, including the file name

if len(sys.argv) > 1:                 # check the length BEFORE using a position
    for arg in sys.argv[1:]:          # [1:] skips sys.argv[0], the file name
        print(f"Hello, {arg}")
else:
    print("No names given")


# THIRD-PARTY PACKAGES
# Wrapped in try/except so the file still runs if they aren't installed

try:
    from pyfiglet import Figlet

    figlet = Figlet()
    figlet.setFont(font="standard")   # pick a font by name
    print(figlet.renderText("Hi"))    # prints "Hi" in big ASCII letters
except ImportError:
    print("pyfiglet not installed")

try:
    import emoji

    print(emoji.emojize(":thumbs_up:"))                    # 👍
    print(emoji.emojize(":thumbsup:", language="alias"))   # 👍, alias allows short names
except ImportError:
    print("emoji not installed")

try:
    import inflect

    p = inflect.engine()
    print(p.join(["Liesl", "Friedrich", "Louisa"]))   # Liesl, Friedrich, and Louisa
    print(p.join(["Liesl", "Friedrich"]))             # Liesl and Friedrich
    print(p.plural("cat"))                            # cats
    print(p.number_to_words(42))                      # forty-two
except ImportError:
    print("inflect not installed")


# SYS.EXIT

sys.exit("Done, sys.exit stops the program here")   # prints the message and ends
print("This line never runs")
