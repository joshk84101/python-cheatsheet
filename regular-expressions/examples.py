import re


# THE MAIN FUNCTIONS

print(re.search(r"cat", "my cat sat"))              # <re.Match object ...> (found it)
print(re.fullmatch(r"cat", "my cat sat"))           # None (the whole text isn't "cat")
print(re.sub(r"cat", "dog", "my cat sat"))          # my dog sat
print(re.findall(r"\d+", "3 cats, 12 dogs"))        # ['3', '12']


# CHECKING A MATCH

match = re.search(r"\d+", "abc123")
if match:                                           # a match object counts as true
    print("Found:", match.group())                  # Found: 123

match = re.search(r"\d+", "abc")
if not match:                                       # None counts as false
    print("No digits")                              # No digits


# ESCAPING A DOT

print(bool(re.search(r"youtube.com", "youtubeXcom")))     # True  (. matched X)
print(bool(re.search(r"youtube\.com", "youtubeXcom")))    # False (\. only matches a real dot)


# SETS

print(re.findall(r"[aeiou]", "regular"))            # ['e', 'u', 'a'] (every vowel)
print(re.findall(r"[^aeiou]", "regular"))           # ['r', 'g', 'l', 'r'] (every NON-vowel)


# QUANTIFIERS

print(bool(re.fullmatch(r"colou?r", "color")))      # True  (u is optional)
print(bool(re.fullmatch(r"colou?r", "colour")))     # True
print(bool(re.fullmatch(r"\d{3}", "087")))          # True  (exactly 3 digits)
print(bool(re.fullmatch(r"\d{3}", "0871")))         # False (4 digits)


# START AND END

print(bool(re.search(r"\d+", "abc123def")))         # True  (digits somewhere inside)
print(bool(re.search(r"^\d+$", "abc123def")))       # False (must be ONLY digits)
print(bool(re.search(r"^\d+$", "123")))             # True


# OR

print(bool(re.fullmatch(r"cat|dog", "dog")))        # True
print(bool(re.fullmatch(r"cat|dog", "bird")))       # False


# GROUPS

match = re.search(r"(\w+)@(\w+)\.com", "alex@example.com")
print(match.group(1))                               # alex   (1st brackets)
print(match.group(2))                               # example (2nd brackets)
print(match.groups())                               # ('alex', 'example')
user, domain = match.groups()                       # unpack into variables


# GROUPING WITHOUT CAPTURING

match = re.search(r"https?://(www\.)?site\.com/(\w+)", "https://www.site.com/alex")
print(match.groups())                               # ('www.', 'alex') -> username is group 2

match = re.search(r"https?://(?:www\.)?site\.com/(\w+)", "https://www.site.com/alex")
print(match.groups())                               # ('alex',) -> username is group 1


# IGNORE CASE

print(bool(re.search(r"hello", "HELLO", re.IGNORECASE)))   # True


# WORKED EXAMPLE: EMAIL

for email in ["alex@example.com", "alex@example.ie", "alex@example", "alex example.com"]:
    print(email, bool(re.fullmatch(r"\w+@\w+\.(com|ie|org)", email)))
    # alex@example.com True / alex@example.ie True / alex@example False / alex example.com False


# WORKED EXAMPLE: IRISH MOBILE

for number in ["0871234567", "087 1234567", "087-1234567", "087123456"]:
    print(number, bool(re.fullmatch(r"08\d[ -]?\d{7}", number)))
    # True / True / True / False


# WORKED EXAMPLE: USERNAME FROM A URL

for url in ["https://github.com/exampleuser", "http://www.github.com/exampleuser", "https://gitlab.com/exampleuser"]:
    match = re.search(r"^https?://(?:www\.)?github\.com/(\w+)$", url)
    if match:
        print(match.group(1))                       # exampleuser (twice), gitlab gives nothing


# WORKED EXAMPLE: VALUE FROM HTML

for html in ['<a href="https://cs50.harvard.edu">CS50</a>', '<a class="btn" href="/home">Home</a>', "<p>no link</p>"]:
    match = re.search(r'<a[^>]*href="([^"]+)"', html)   # single quotes because the pattern has "
    print(match.group(1) if match else None)        # https://cs50.harvard.edu / /home / None


# WORKED EXAMPLE: DATE

year, month, day = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", "2026-11-06").groups()
print(year, month, day)                             # 2026 11 06 (all strings)


# REPLACE AND FIND ALL

print(re.sub(r"\s+", " ", "too    many   spaces"))  # too many spaces
print(re.findall(r"\d+", "Order 66 shipped 3 items for 120 euro"))   # ['66', '3', '120']


# REGEX FOR THE SHAPE, PYTHON FOR THE MATHS

match = re.fullmatch(r"(\d{1,2})/(\d{4})", "13/2026")
if match:
    month = int(match.group(1))                     # groups are strings, so convert
    if 1 <= month <= 12:
        print("Valid")
    else:
        print("Invalid month")                      # Invalid month
