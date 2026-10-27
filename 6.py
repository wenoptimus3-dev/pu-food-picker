import sys

k = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip('\n')

ans = []
for c in s:
    if 'a' <= c <= 'z':
        ans.append(chr((ord(c) - 97 + k) % 26 + 97))
    elif 'A' <= c <= 'Z':
        ans.append(chr((ord(c) - 65 + k) % 26 + 65))
    else:
        ans.append(c)

print("".join(ans))