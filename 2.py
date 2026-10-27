s = input()
s = s.strip()
parts = s.split()
cleaned = "_".join(parts)

cleaned = cleaned.lower()

print(cleaned)
is_valid = True
length = len(cleaned)


if length < 6 or length > 16:
    is_valid = False
else:
   
    for char in cleaned:
        if not (('a' <= char <= 'z') or ('0' <= char <= '9') or char == '_'):
            is_valid = False
            break
if is_valid and length > 0:
    print("VALID")
else:
    print("INVALID")
