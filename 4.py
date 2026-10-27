n = int(input())
names = []
subtotals = []

for _ in range(n):
    line = input().split()
    name = line[0]
    price = int(line[1])
    quantity = int(line[2])
    
    paid_qty = quantity - (quantity // 3)
    subtotal = paid_qty * price
    
    names.append(name)
    subtotals.append(subtotal)

total_sum = sum(subtotals)
if total_sum >= 1000:
    final_total = total_sum - 100
else:
    final_total = total_sum

for i in range(n):
    print(f"{names[i]} {subtotals[i]}")

print(f"TOTAL {final_total}")

max_sub = -1
max_name = ""
for i in range(n):
    if subtotals[i] > max_sub:
        max_sub = subtotals[i]
        max_name = names[i]

print(f"TOP {max_name}")