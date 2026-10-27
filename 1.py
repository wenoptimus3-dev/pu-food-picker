b, n, r, c = map(int, input().split())
service_fee = (b * r) // 100

t = b + service_fee - c
if t < 0:
    t = 0

print(t)
q = t // n
b_count = t % n
a_count = n - b_count

print(f"{q} {a_count}")
print(f"{q + 1} {b_count}")
