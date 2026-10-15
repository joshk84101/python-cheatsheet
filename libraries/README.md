# Libraries

## What is a library?

Code someone else has already written that you can use in your own program. Saves you writing everything from scratch.

- **Module:** a single Python file of reusable code (like `random`)
- **Package:** a bundle of modules you install from the internet (like `pyfiglet`)
- **Library:** the general word for either

| Type | Examples | Need to install? |
|---|---|---|
| Built-in (comes with Python) | `random`, `statistics`, `sys`, `json` | No |
| Third-party (from PyPI) | `pyfiglet`, `emoji`, `inflect`, `requests` | Yes, with `pip` |

## Importing

Imports go at the **top** of the file.

| Style | Example | How you call it |
|---|---|---|
| Import the whole module | `import random` | `random.randint(1, 10)` |
| Import one thing from it | `from random import randint` | `randint(1, 10)` |
| Import several things | `from random import randint, choice` | `choice(["a", "b"])` |
| Import with a nickname | `import statistics as stats` | `stats.mean([1, 2])` |

**When to use which:** `import random` is clearer, because you can always see where a function came from. `from ... import` is handy when you use one function a lot.

## random

```python
import random

random.randint(1, 10)              # random whole number from 1 to 10 (BOTH ends included)
random.choice(["heads", "tails"])  # picks one random item from a list

cards = ["jack", "queen", "king"]
random.shuffle(cards)              # shuffles the list IN PLACE, returns None
print(cards)                       # e.g. ['king', 'jack', 'queen']
```

## statistics

```python
import statistics

statistics.mean([100, 90, 80])     # 90 (the average)
statistics.median([1, 3, 9])       # 3 (the middle value)
```

## sys.argv (command-line arguments)

`sys.argv` is a list of the words typed after `python` on the command line. `sys.argv[0]` is always the file name.

```python
import sys

print(sys.argv)
```

| You type | `sys.argv` | `len(sys.argv)` |
|---|---|---|
| `python name.py` | `["name.py"]` | 1 |
| `python name.py Josh` | `["name.py", "Josh"]` | 2 |
| `python name.py -f slant` | `["name.py", "-f", "slant"]` | 3 |

Always check the length **before** using a position, or you'll get an `IndexError`.

```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print(f"Hello, {sys.argv[1]}")
```

```
$ python name.py
Too few arguments
$ python name.py Josh
Hello, Josh
```

Use slicing to loop over every argument except the file name:

```python
for arg in sys.argv[1:]:    # [1:] skips sys.argv[0]
    print(f"Hello, {arg}")
```

## sys.exit

Stops the program immediately. If you give it a message, it prints the message first.

```python
sys.exit("Invalid usage")
```

## Installing packages with pip

`pip` downloads packages from PyPI (the Python Package Index). Run it in the **terminal**, not inside Python.

```
pip install pyfiglet
pip install emoji inflect      # can install several at once
```

## pyfiglet (big ASCII art text)

```python
from pyfiglet import Figlet

figlet = Figlet()
figlet.getFonts()              # list of every font name
figlet.setFont(font="standard")
print(figlet.renderText("Hi"))
```

```
 _   _ _
| | | (_)
| |_| | |
|  _  | |
|_| |_|_|
```

## emoji

```python
import emoji

emoji.emojize(":thumbs_up:")                    # 👍
emoji.emojize(":thumbsup:", language="alias")   # 👍 (alias allows the short names too)
```

## inflect (correct English grammar)

```python
import inflect

p = inflect.engine()

p.join(["Liesl", "Friedrich", "Louisa"])   # "Liesl, Friedrich, and Louisa"
p.join(["Liesl", "Friedrich"])             # "Liesl and Friedrich"
p.plural("cat")                            # "cats"
p.number_to_words(42)                      # "forty-two"
```

## requests and json (getting data from the internet)

An **API** is a website that sends back data instead of a web page. `requests` fetches it, and `.json()` turns it into Python dicts and lists.

```python
import requests

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
data = response.json()             # now a normal Python dict

for result in data["results"]:
    print(result["trackName"])
```

To print JSON in a readable layout:

```python
import json

print(json.dumps(data, indent=2))
```

## Making your own module

Any `.py` file can be imported by another file in the same folder.

```python
# sayings.py
def hello(name):
    return f"Hello, {name}"


def main():
    print(hello("world"))


if __name__ == "__main__":     # stops main() running when another file imports this
    main()
```

```python
# say.py
from sayings import hello

print(hello("Josh"))           # Hello, Josh
```

See the `functions` folder for more on `if __name__ == "__main__":`.

## Common mistakes

- Running `pip install` inside Python instead of in the terminal
- Naming your own file the same as a library (like `random.py` or `emoji.py`). Python imports your file instead of the real one and everything breaks
- Writing `import random` and then calling `randint()` on its own. Without `from random import randint`, it must be `random.randint()`
- Forgetting `random.randint(a, b)` includes **both** ends, so `randint(1, 10)` can return 10
- Writing `cards = random.shuffle(cards)`. `shuffle` changes the list in place and returns `None`, so `cards` becomes `None`
- Using `sys.argv[1]` without checking `len(sys.argv)` first, which causes `IndexError` when no argument is given
- Forgetting `sys.argv[0]` is the file name, not the first argument
