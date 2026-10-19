# Python Fundamentals Checklist

Last updated: October 17, 2026

**How to use this:** tick a box (`[x]`) only when you can do the thing from a blank file, without looking anything up. Items already used in this repo are pre-ticked, but using something once is "started", not "mastered". If a topic still feels shaky, untick it and redo an exercise.

---

## 1. Basics
- [x] Variables, `input()`, and type casting (`int()`, `float()`)
- [x] f-strings
- [x] Arithmetic, comparison, and logical operators (`and`, `or`, `not`)
- [x] `%` (modulo) and `//` (floor division)
- [x] Operator precedence and `**` for exponents
- [ ] `round()`, `abs()`, and the `math` module

## 2. Control Flow
- [x] `if` / `elif` / `else`, including nested conditions
- [x] `match` / `case`
- [x] `for` loops with `range()` (including step and counting down)
- [x] `while` loops and `while True` with `break`
- [x] `continue`
- [x] Nested loops
- [x] Boolean flag variables
- [ ] `for ... else` and `while ... else`

## 3. Strings
- [x] Looping over characters
- [x] Character-check methods (`.isupper()`, `.islower()`, `.isdigit()`, `.isalpha()`)
- [x] `.upper()`, `.lower()`, `.join()`
- [x] `ord()` and `chr()`
- [ ] Slicing beyond reversing (`s[2:6]`, `s[::2]`)
- [ ] `.split()`, `.strip()`, `.replace()`, `.find()`, `.count()`
- [ ] Formatting numbers and alignment (`{x:.2f}`, `{name:<10}`)

## 4. Lists
- [x] Creating lists, `.append()`, and indexing (`my_list[0]`)
- [x] Membership checks with `in`
- [x] List comprehensions
- [ ] Slicing, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`
- [ ] Largest/smallest without `max()` / `min()` (redo `number_listdicts.py`)
- [ ] Looping with `enumerate()`
- [ ] 2D lists (lists inside lists)

## 5. Tuples and Sets
- [x] Tuple unpacking (multiple return values)
- [ ] Why tuples are immutable, and when to use them
- [ ] Set operations: union, intersection, difference
- [ ] Using a set to remove or detect duplicates

## 6. Dictionaries
- [x] Creating a dictionary and using it for lookups
- [ ] Add, update, delete, and `.get()`
- [ ] Looping with `.keys()`, `.values()`, `.items()`
- [ ] Counting frequency (e.g. letters in a word)
- [ ] Nested dictionaries
- [ ] Lists of dictionaries (e.g. a device inventory)

## 7. Functions
- [x] `def`, parameters, and `return`
- [x] Returning multiple values
- [x] Functions calling other functions
- [x] Passing lists into functions
- [x] Re-calling a function for fresh results instead of reusing stale variables
- [ ] Default parameters and keyword arguments
- [ ] Variable scope: local vs. global
- [ ] Functions that build and return a new list or dict
- [ ] Recursion (factorial, countdown)
- [ ] Docstrings

## 8. Error Handling
- [ ] `try` / `except` with `ValueError` and `ZeroDivisionError`
- [ ] Input validation that never crashes on bad input (note: `.isalpha()` alone lets values like `"12abc"` or `"-5"` through)
- [ ] Reading a traceback from the bottom up

## 9. Modules and Files
- [x] `import random` and `import time`
- [ ] `import math` and `datetime`
- [ ] Reading and writing text files with `with open(...)`
- [ ] CSV and JSON basics
- [ ] `if __name__ == "__main__":`
- [ ] Splitting a project across multiple `.py` files

## 10. Habits
- [ ] Hand-trace code before running it
- [ ] Test edge cases (empty input, boundaries, wrong types)
- [ ] PEP 8 spacing and naming (`snake_case`, spaces around `=`)
- [ ] Comments that explain *why*, not *what*
- [ ] Clear commit messages
- [ ] A README for every folder and project
- [ ] A `.gitignore` (keep `.DS_Store` out of the repo)

## 11. Later, Once the Above Feels Solid
- [ ] Classes and objects (intro OOP)
- [ ] `pip` and virtual environments
- [ ] Regular expressions (`re`)
- [ ] `ipaddress`, `socket`, `hashlib` (networking and security)
- [ ] `requests` for calling web APIs

---

## Suggested Order of Practice
1. **Dictionaries and sets** — used everywhere in networking scripts, and the least practiced so far.
2. **List methods and slicing** — to lock in what the list exercises started.
3. **`try` / `except`** — makes the calculator and menu programs crash-proof.
4. **Variable scope** — explains why functions sometimes can't change outer variables.
5. **File I/O** — unlocks projects that save data between runs (e.g. a to-do list).
