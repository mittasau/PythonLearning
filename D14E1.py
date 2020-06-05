import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("63633636dgdgdgd7372GGGG")) 
print(is_allowed_specific_char("@#@$@%@^@&@&"))