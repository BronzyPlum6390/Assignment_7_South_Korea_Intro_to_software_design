def upper_or_lower(s):
    if c[0] == 'a' or c[0] == 'b' or c[0] == 'c':
        return s.upper()
    else:
        return s.lower()

c = input()
print(upper_or_lower(c))

