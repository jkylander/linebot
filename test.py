import re

string = "background.js"
match = re.match(r"([^?]+)", string)

if match:
    matched_chars = match.group(1)
    print(matched_chars)
else:
    print("No match found")