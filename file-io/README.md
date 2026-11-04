# File I/O

## What is File I/O?

I/O means input and output. Normally everything a program stores in variables is lost when it ends. Writing to a file saves data so it's still there next time the program runs, and reading a file loads it back in.

**When to use:** saving data between runs, reading data someone else has saved (like a CSV of names or prices).

## Opening a file with `with`

```python
with open("names.txt", "a") as file:
    file.write("Josh\n")
```

- `open()` opens the file and gives you a file object to work with
- `with ... as file:` closes the file automatically when the block ends, even if there's an error
- Always use `with`, so you never forget to close the file

## File modes

The second argument to `open()` says what you want to do with the file.

| Mode | Meaning | If the file doesn't exist |
|---|---|---|
| `"r"` | **Read** (the default if you leave it out) | Raises `FileNotFoundError` |
| `"w"` | **Write**, and **wipes** everything already in the file | Creates it |
| `"a"` | **Append**: add to the end, keep what's there | Creates it |

## Writing to a file

```python
with open("names.txt", "a") as file:
    file.write("Josh\n")      # \n moves to a new line, write() doesn't add one for you
    file.write("Sarah\n")
```

## Reading a file

```python
# Line by line (best for most files)
with open("names.txt") as file:
    for line in file:
        print(line.rstrip())   # rstrip() removes the \n at the end of each line

# All lines into a list
with open("names.txt") as file:
    lines = file.readlines()   # ["Josh\n", "Sarah\n"]

# The whole file as one string
with open("names.txt") as file:
    text = file.read()         # "Josh\nSarah\n"
```

**Why `.rstrip()`?** Each line keeps its `\n` at the end. Without `.rstrip()`, `print()` adds its own newline as well, so you'd get a blank line between every line.

## Handling a missing file

```python
import sys

try:
    with open("names.txt") as file:
        for line in file:
            print(line.rstrip())
except FileNotFoundError:
    sys.exit("File does not exist")
```

## CSV files

A CSV (comma-separated values) file is a simple text spreadsheet. The first line is usually the header.

```
name,house
Harry,Gryffindor
Draco,Slytherin
```

### The manual way (split it yourself)

```python
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
```

This breaks if a value contains a comma, like `"Number Four, Privet Drive"`, and it treats the header line as data. That's why the `csv` library exists.

### The easy way: `csv.DictReader`

```python
import csv

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} is in {row['house']}")
```

- Uses the header line as the dictionary keys, so each `row` is like `{"name": "Harry", "house": "Gryffindor"}`
- Skips the header automatically
- Handles commas inside quoted values
- Still works if the columns are in a different order

| Tool | Each row is a | Access a value with |
|---|---|---|
| `csv.reader` | list | `row[0]` |
| `csv.DictReader` | dictionary | `row["name"]` |

### Writing a CSV: `csv.DictWriter`

```python
import csv

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": "Hermione", "house": "Gryffindor"})
```

`fieldnames` tells it which column each dictionary key goes in.

## Reading one CSV and writing a new one

A common job: read a file, change each row, and save the result as a **new** file. Think of it as copying from an old notebook into a new one. Both notebooks need to be open on the desk at the same time.

**Example:** `prices.csv` has prices without VAT. Make `prices_vat.csv` with a new column for the price including 23% VAT.

`prices.csv` (input):
```
item,price
Coffee,3.00
Sandwich,6.50
```

`prices_vat.csv` (output, created by the program):
```
item,price,price_vat
Coffee,3.00,3.69
Sandwich,6.50,8.00
```

```python
import csv

with open("prices.csv") as infile:                               # 1. open the input to read
    reader = csv.DictReader(infile)                              #    hands you one row at a time as a dictionary

    with open("prices_vat.csv", "w", newline="") as outfile:     # 2. open the output to write (created blank)
        writer = csv.DictWriter(outfile, fieldnames=["item", "price", "price_vat"])
        writer.writeheader()                                     # 3. write the column titles ONCE

        for row in reader:                                       # 4. one row at a time from the input
            price = float(row["price"])                          #    change the data
            price_vat = round(price * 1.23, 2)
            writer.writerow({                                    #    write ONE row to the output
                "item": row["item"],
                "price": row["price"],
                "price_vat": f"{price_vat:.2f}",
            })
```

### The rule: set up once, repeat inside the loop

| Before the loop (once) | Inside the loop (every row) |
|---|---|
| Open both files | Change the data |
| Make the reader and the writer | Write one row with `writerow()` |
| Write the header with `writeheader()` | |

### Why the second `with` goes inside the first
- Both files have to be **open during the loop**: you read from one and write to the other on every row
- If the output `with` came **after** the input `with`, the input file would already be closed, and the reader would have nothing left to give
- If the output were opened **inside the loop** with `"w"`, it would be wiped on every row, so only the last row would survive

### Naming the files
Give the two files **different names** (`infile` and `outfile`). If both were called `file`, the second would replace the first.

### `writerow()` takes a dictionary
- The **keys** must match the `fieldnames` exactly
- The **values** are this row's data

```python
writer.writerow({"item": "Coffee", "price": "3.00", "price_vat": "3.69"})
# writes the line: Coffee,3.00,3.69
```

### `newline=""`
On Windows, the `csv` module adds a blank line between rows unless you open the output file with `newline=""`. It does no harm on other systems, so always include it when writing a CSV.

## Sorting what you read

```python
students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

for student in sorted(students, key=lambda student: student["name"]):
    print(student["name"])
```

- `sorted()` returns a new sorted list
- `key=` says **what to sort by**
- `lambda student: student["name"]` is a tiny one-line function: "given a student, use their name"
- Add `reverse=True` to sort Z to A

## Common mistakes

- Using `"w"` when you meant `"a"`. `"w"` wipes the whole file first
- Forgetting `\n` when writing, so everything ends up on one line
- Forgetting `.rstrip()` when reading, so you get extra blank lines when printing
- Reading a file that doesn't exist without catching `FileNotFoundError`
- Running the program from a different folder than the file. `open("names.txt")` looks in the folder the **terminal** is in, not the folder the `.py` file is in
- Splitting a CSV by hand with `.split(",")` when values can contain commas. Use the `csv` library
- Forgetting the header line is data too when reading a CSV by hand
- Opening the output file **inside** the loop with `"w"`, so every row wipes the one before and only the last row is saved
- Putting the output `with` **after** the input `with` instead of inside it, so the input is already closed when the loop runs
- Calling `writeheader()` inside the loop, so the titles are written on every row
