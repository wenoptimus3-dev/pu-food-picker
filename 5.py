m = int(input())
drink_names = []
drink_prices = []
drink_counts = []

for _ in range(m):
    line = input().split()
    drink_names.append(line[0])
    drink_prices.append(int(line[1]))
    drink_counts.append(0)

n = int(input())
order_students = []
order_drinks = []
order_qtys = []
student_names = []

for _ in range(n):
    line = input().split()
    s_name = line[0]
    d_name = line[1]
    qty = int(line[2])
    
    order_students.append(s_name)
    order_drinks.append(d_name)
    order_qtys.append(qty)
    
    d_idx = drink_names.index(d_name)
    drink_counts[d_idx] += qty
    
    found = False
    for s in student_names:
        if s == s_name:
            found = True
            break
    if not found:
        student_names.append(s_name)

final_prices = []
for i in range(m):
    p = drink_prices[i]
    if drink_counts[i] >= 10:
        p -= 5
    final_prices.append(p)

student_amounts = [0] * len(student_names)
for i in range(n):
    s_idx = student_names.index(order_students[i])
    d_idx = drink_names.index(order_drinks[i])
    student_amounts[s_idx] += order_qtys[i] * final_prices[d_idx]

for i in range(m):
    print(f"DRINK {drink_names[i]} {drink_counts[i]}")

for i in range(len(student_names)):
    print(f"STUDENT {student_names[i]} {student_amounts[i]}")

print(f"TOTAL {sum(student_amounts)}")