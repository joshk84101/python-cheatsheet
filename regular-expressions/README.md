# Regular Expressions

## What is a regular expression?

A **regular expression** (regex) is a short pattern that describes what some text should look like. Instead of checking text character by character with loops and `if`s, you write one pattern and Python checks it for you.

**When to use:** checking a format is valid (email, phone number), pulling a piece out of text (a username from a URL), or finding and replacing patterns.

```python
import re

if re.search(r"^\d{3}$", "087"):
    print("Three digits")
```

## Always use `r"..."` (raw strings)

Put an `r` in front of every pattern. Without it, Python tries to read things like `\d` itself and gives warnings.

```python
r"\d+"     # correct
"\d+"      # works, but Python complains
```

If the pattern contains a `"`, use single quotes around it instead: `r'src="(\w+)"'`

## The main functions

| Function | Question it answers | Gives back |
|---|---|---|
| `re.search(pattern, text)` | Is the pattern **anywhere** in the text? | A match object, or `None` |
| `re.fullmatch(pattern, text)` | Does the **whole** text match the pattern? | A match object, or `None` |
| `re.sub(pattern, new, text)` | Replace every match with something else | A new string |
| `re.findall(pattern, text)` | Find **every** match | A list of strings |

```python
re.search(r"cat", "my cat sat")           # match (found "cat" in the middle)
re.fullmatch(r"cat", "my cat sat")        # None (the whole text isn't "cat")
re.sub(r"cat", "dog", "my cat sat")       # "my dog sat"
re.findall(r"\d+", "3 cats, 12 dogs")     # ["3", "12"]
```

**Important:** `re.search` never gives back `True` or `False`. It gives a match object or `None`. So check it like this:

```python
match = re.search(r"\d+", text)
if match:         # matched
    ...
if not match:     # didn't match
    ...
```

Never `if match == True:`, because a match object is never equal to `True`.

## Plain text

Letters, numbers and most symbols just match themselves.

| Pattern | Input | Match? |
|---|---|---|
| `cat` | `my cat` | ✅ `cat` |
| `embed/` | `youtube.com/embed/abc` | ✅ `embed/` |
| `cat` | `my dog` | ❌ |

## Special characters (escape with `\` to match the real thing)

These have special meanings. To match the actual character, put `\` in front.

| Character | Special meaning | Real character |
|---|---|---|
| `.` | Any one character | `\.` |
| `?` | Optional | `\?` |
| `+` | One or more | `\+` |
| `*` | Zero or more | `\*` |
| `(` `)` | Group | `\(` `\)` |
| `[` `]` | Set | `\[` `\]` |
| `^` `$` | Start / end | `\^` `\$` |

| Pattern | Input | Match? |
|---|---|---|
| `youtube.com` | `youtubeXcom` | ✅ (`.` matched the `X`, probably not what you wanted) |
| `youtube\.com` | `youtubeXcom` | ❌ |
| `youtube\.com` | `youtube.com` | ✅ |

`/`, `:`, `"`, `=`, `<`, `>`, `@` and `-` (outside `[ ]`) are **not** special, so type them as they are.

## Character shortcuts

| Pattern | Means | Example matches |
|---|---|---|
| `\d` | One digit (0 to 9) | `7` |
| `\D` | One character that is **not** a digit | `a`, `-` |
| `\w` | One "word" character: letter, digit or `_` | `a`, `7`, `_` |
| `\W` | One character that is **not** a word character | `.`, ` `, `@` |
| `\s` | One space, tab or newline | ` ` |
| `\S` | One character that is **not** whitespace | `a`, `.` |
| `.` | Any one character (except newline) | `a`, `7`, `.` |

## Sets: `[ ]`

Square brackets match **one** character from a list.

| Pattern | Means | Input | Match? |
|---|---|---|---|
| `[aeiou]` | One vowel | `cat` | ✅ `a` |
| `[a-z]` | One lowercase letter | `Cat` | ✅ `a` |
| `[A-Z]` | One uppercase letter | `Cat` | ✅ `C` |
| `[0-9]` | One digit (same as `\d`) | `x7` | ✅ `7` |
| `[a-zA-Z]` | One letter, any case | `7Q` | ✅ `Q` |
| `[^>]` | One character that is **not** `>` | `abc>` | ✅ `a` |
| `[^"]` | One character that is **not** `"` | `abc"` | ✅ `a` |

**Watch out:** `[0-255]` does **not** mean "0 to 255". It means one character that is `0`, `1`, `2` or `5`. Sets only ever match **one character**.

## How many: quantifiers

These go **after** the thing they repeat.

| Pattern | Means | Example |
|---|---|---|
| `x?` | 0 or 1 `x` (optional) | `colou?r` matches `color` and `colour` |
| `x*` | 0 or more `x` | `ab*c` matches `ac`, `abc`, `abbbc` |
| `x+` | 1 or more `x` | `\d+` matches `7`, `42`, `2026` |
| `x{3}` | Exactly 3 `x` | `\d{3}` matches `087` |
| `x{2,4}` | Between 2 and 4 `x` | `\d{2,4}` matches `12`, `123`, `1234` |
| `x{1,}` | 1 or more (same as `+`) | |

**Watch out:** the quantifier goes **after**. `\d+` is right. `+\d` gives an error: `nothing to repeat`.

## Start and end: `^` and `$`

| Pattern | Means |
|---|---|
| `^` (at the start of the pattern) | The text must **start** here |
| `$` (at the end of the pattern) | The text must **end** here |

| Pattern | Input | Match? | Why |
|---|---|---|---|
| `\d+` | `abc123def` | ✅ `123` | Digits are somewhere in there |
| `^\d+$` | `abc123def` | ❌ | Text must be **only** digits |
| `^\d+$` | `123` | ✅ | Only digits, start to end |
| `^Hi` | `Hi Alex` | ✅ | Starts with `Hi` |
| `^Hi` | `Oh Hi` | ❌ | Doesn't start with `Hi` |

**Rule of thumb:** use `^...$` when checking a **whole** input is valid (like a phone number). Leave them off when **searching inside** bigger text (like HTML).

**Watch out:** `^` means something different inside `[ ]`. There, it means **not**: `[^>]` is "any character except `>`".

## Or: `|`

| Pattern | Input | Match? |
|---|---|---|
| `cat\|dog` | `my dog` | ✅ `dog` |
| `^(cat\|dog)$` | `cat` | ✅ |
| `^(cat\|dog)$` | `bird` | ❌ |

Wrap the options in brackets so `^` and `$` apply to the whole choice.

## Groups: `( )`

Brackets do two jobs:
1. **Group** several characters so a quantifier applies to all of them
2. **Capture** what they matched so you can get it out afterwards

```python
match = re.search(r"(\w+)@(\w+)\.com", "alex@example.com")

match.group(1)     # "alex"               (1st brackets)
match.group(2)     # "example"            (2nd brackets)
match.groups()     # ("alex", "example")  (all of them, as a tuple)
match.group()      # "alex@example.com"   (the whole match)
```

- `.group(1)` is the 1st brackets, `.group(2)` the 2nd, and so on. Counting starts at **1**
- `.groups()` (with an s) gives **all** of them as a tuple, which you can unpack:

```python
user, domain = match.groups()
```

### Grouping without capturing: `(?: )`

Use `(?: )` when you need brackets **only** to make something optional or repeated, and don't want it to count as a group.

| Pattern | Groups captured from `https://www.site.com/alex` |
|---|---|
| `https?://(www\.)?site\.com/(\w+)` | `("www.", "alex")`, so the username is `group(2)` |
| `https?://(?:www\.)?site\.com/(\w+)` | `("alex",)`, so the username is `group(1)` |

Two different `?` here:
- `?:` straight after `(` means "don't capture"
- `?` after `)` means "this whole group is optional"

## Flags

| Flag | Effect | Example |
|---|---|---|
| `re.IGNORECASE` | Capitals don't matter | `re.search(r"hello", "HELLO", re.IGNORECASE)` matches |

## Worked examples

### 1. Is this a valid email?

```python
re.fullmatch(r"\w+@\w+\.(com|ie|org)", email)
```

| Input | Result |
|---|---|
| `alex@example.com` | ✅ |
| `alex@example.ie` | ✅ |
| `alex@example` | ❌ no ending |
| `alex example.com` | ❌ no `@` |
| `alex@example.net` | ❌ `.net` not allowed |

### 2. Is this an Irish mobile number?

Format: `08`, then one digit, then 7 digits, with an optional space or dash after the first three.

```python
re.fullmatch(r"08\d[ -]?\d{7}", number)
```

| Input | Result |
|---|---|
| `0871234567` | ✅ |
| `087 1234567` | ✅ |
| `087-1234567` | ✅ |
| `087123456` | ❌ only 6 digits at the end |
| `0971234567` | ❌ doesn't start with `08` |

### 3. Pull a username out of a URL

```python
match = re.search(r"^https?://(?:www\.)?github\.com/(\w+)$", url)
if match:
    print(match.group(1))
```

| Input | Output |
|---|---|
| `https://github.com/exampleuser` | `exampleuser` |
| `http://www.github.com/exampleuser` | `exampleuser` |
| `https://gitlab.com/exampleuser` | (no match, nothing printed) |

### 4. Pull a value out of HTML

Find the `href` of a link, allowing other attributes before it.

```python
match = re.search(r'<a[^>]*href="([^"]+)"', html)
```

| Input | `match.group(1)` |
|---|---|
| `<a href="https://cs50.harvard.edu">CS50</a>` | `https://cs50.harvard.edu` |
| `<a class="btn" href="/home">Home</a>` | `/home` |
| `<p>no link</p>` | (no match) |

| Piece | Job |
|---|---|
| `<a` | Must be a link tag |
| `[^>]*` | Skip any other attributes, but don't go past the end of the tag |
| `href="` | Then find `href="` |
| `([^"]+)` | Capture everything up to the closing quote |
| `"` | The closing quote |

### 5. Pull a date apart

```python
match = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", "2026-11-06")
year, month, day = match.groups()
```

| Variable | Value |
|---|---|
| `year` | `"2026"` |
| `month` | `"11"` |
| `day` | `"06"` |

Groups are always **strings**. Use `int()` if you need to do maths or compare them to numbers.

### 6. Replace: tidy up extra spaces

```python
re.sub(r"\s+", " ", "too    many   spaces")
```
Output: `"too many spaces"`

### 7. Find every number in some text

```python
re.findall(r"\d+", "Order 66 shipped 3 items for 120 euro")
```
Output: `["66", "3", "120"]`

## Regex for the shape, Python for the maths

Regex can't do maths. If you need to check a number is in a range (like 1 to 12 for a month), use regex to check the **shape** and pull out the number, then check the value with normal Python:

```python
match = re.fullmatch(r"(\d{1,2})/(\d{4})", "13/2026")
if match:
    month = int(match.group(1))
    if 1 <= month <= 12:
        print("Valid")
    else:
        print("Invalid month")       # this one prints
```

## Building a pattern without losing your mind

1. **Write out a real example** of the text you want to match
2. **Go left to right**, turning each part into pattern pieces: fixed text stays as it is, parts that change become `\d+`, `\w+` etc.
3. **Add one piece at a time** and test after each one
4. **Put brackets around** only the parts you want to keep
5. **Test on regex101.com**: it highlights what matches and explains every symbol

## Common mistakes

- Forgetting the `r` before the pattern
- Forgetting `\` before a dot, so `.` matches **any** character
- Putting a quantifier **before** what it repeats (`+\d` instead of `\d+`)
- Thinking `[0-255]` means "0 to 255". It's one character: `0`, `1`, `2` or `5`
- Writing `"a" or "b"` inside a function call. Python turns that into just `"a"`. Use `a|b` in the pattern, or a tuple in `.endswith(("a", "b"))`
- Forgetting `^` and `$` when the **whole** input must match, so extra text before or after slips through
- Checking `if match == True:`. Use `if match:` or `if not match:`
- Calling `.group()` when there was no match. `None` has no `.group()`, so check first
- Calling `.split()` on a match object. Split the original string, or use `.groups()`
- Plain `( )` for an optional part, which shifts your other group numbers. Use `(?: )`
- Mixing up `^` at the start of a pattern (start of text) with `^` inside `[ ]` (not)
- Forgetting groups give back **strings**, so `int()` them before comparing to numbers
- Using `"` inside a pattern wrapped in `"..."`. Wrap it in `'...'` instead
