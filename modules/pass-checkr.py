"""password checker."""

import re

# password checker that contrains the following:
# At least 8 characters long
# Contains any sort of letters, and number $%#@

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}")

string = input("Please enter a password: ")

a = pattern.search(string)
print(a)

