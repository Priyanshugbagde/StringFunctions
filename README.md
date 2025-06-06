# String Methods in Python

This program demonstrates the usage of various common string methods in Python using the example string `"Instagram"`.

## Code Summary

```python
s = "Instagram"

print(s.lower())         # Converts to lowercase
print(s.upper())         # Converts to uppercase
print(s.startswith("In"))# Checks if string starts with "In"
print(s.endswith("ram")) # Checks if string ends with "ram"
print(s.isalpha())       # Checks if all characters are alphabetic
print(s.isalnum())       # Checks if all characters are alphanumeric
print(s.capitalize())    # Capitalizes the first character
print(s.swapcase())      # Swaps the case of each letter
print(s.find("a"))       # Finds first occurrence of "a"
print(s.count("a"))      # Counts number of times "a" appears

Output 
instagram
INSTAGRAM
True
True
True
True
Instagram
iNSTAGRAM
3
2
