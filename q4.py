a = float(input('Nhap a = '))
b = float(input('Nhap b = '))
c = float(input('Nhap c = '))

max_value = max(a, b, c)
min_value = min(a, b, c)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")

sorted_values = sorted([a, b, c])
print(f"Values in ascending order: {sorted_values}")
