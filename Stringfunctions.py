s = "Instagram"

print(s.lower())            # Converts all letters to lowercase
print(s.upper())            # Converts all letters to uppercase
print(s.startswith("In"))   # Checks if string starts with "In"
print(s.endswith("ram"))    # Checks if string ends with "ram"
print(s.isalpha())          # Checks if all characters are alphabetic
print(s.isalnum())          # Checks if all characters are alphanumeric (letters or numbers)
print(s.capitalize())       # Capitalizes the first letter, rest lowercase
print(s.swapcase())         # Swaps case of each letter
print(s.find("a"))          # Finds first index of "a", -1 if not found
print(s.count("a"))         # Counts how many times "a" appears
