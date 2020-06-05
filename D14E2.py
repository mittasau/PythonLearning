import re
items = ["XYZ(.com)", "ABC", "jkl(.com)", "pol(.com)"] 
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))