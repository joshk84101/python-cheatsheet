# Running this creates names.txt, students.csv, prices.csv and prices_vat.csv in the folder your terminal is in

import csv
import sys


# WRITING A FILE

with open("names.txt", "w") as file:      # "w" wipes the file first, so each run starts fresh
    file.write("Josh\n")                    # \n moves to a new line
    file.write("Sarah\n")

with open("names.txt", "a") as file:      # "a" adds to the end, keeps what's there
    file.write("Ciara\n")


# READING A FILE

with open("names.txt") as file:           # no mode given, so "r" (read) is the default
    for line in file:                       # one line at a time
        print(line.rstrip())                # rstrip() removes the \n at the end

with open("names.txt") as file:
    lines = file.readlines()                # every line into a list
    print(lines)                            # ['Josh\n', 'Sarah\n', 'Ciara\n']


# HANDLING A MISSING FILE

try:
    with open("missing.txt") as file:       # this file doesn't exist
        print(file.read())
except FileNotFoundError:
    print("missing.txt does not exist")     # sys.exit("...") in a real program


# WRITING A CSV

with open("students.csv", "w", newline="") as file:   # newline="" stops blank rows appearing on Windows
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writeheader()                                # writes the "name,house" header line
    writer.writerow({"name": "Harry", "house": "Gryffindor"})
    writer.writerow({"name": "Draco", "house": "Slytherin"})
    writer.writerow({"name": "Hermione", "house": "Gryffindor"})


# READING A CSV THE MANUAL WAY

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")        # split each line on the comma
        print(f"{name} is in {house}")                 # note: prints the header as data too


# READING A CSV WITH csv.DictReader

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)           # uses the header line as dictionary keys
    for row in reader:                      # header is skipped automatically
        students.append(row)                # each row is like {"name": "Harry", "house": "Gryffindor"}


# READING ONE CSV AND WRITING A NEW ONE

with open("prices.csv", "w", newline="") as file:      # first, make an input file to work with
    file.write("item,price\nCoffee,3.00\nSandwich,6.50\n")

with open("prices.csv") as infile:                               # 1. open the input to read
    reader = csv.DictReader(infile)                              #    one row at a time as a dictionary

    with open("prices_vat.csv", "w", newline="") as outfile:     # 2. open the output, INSIDE the first with
        writer = csv.DictWriter(outfile, fieldnames=["item", "price", "price_vat"])
        writer.writeheader()                                     # 3. titles, written ONCE before the loop

        for row in reader:                                       # 4. every row: change it, then write it
            price = float(row["price"])                          #    "3.00" (text) becomes 3.0 (number)
            price_vat = round(price * 1.23, 2)                   #    add 23% VAT
            writer.writerow({
                "item": row["item"],
                "price": row["price"],
                "price_vat": f"{price_vat:.2f}",                  #    always 2 decimal places
            })

with open("prices_vat.csv") as file:
    print(file.read())                                           # item,price,price_vat / Coffee,3.00,3.69 / Sandwich,6.50,8.00


# SORTING

for student in sorted(students, key=lambda student: student["name"]):   # sort by name
    print(f"{student['name']} is in {student['house']}")

for student in sorted(students, key=lambda student: student["name"], reverse=True):  # Z to A
    print(student["name"])
