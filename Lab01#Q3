a = float(input('Nhập a = '))
b = float(input('Nhập b = '))
c = float(input('Nhập c = '))
x = float(input('Nhập x = '))

S1 = a*x*x + b*x + c
print("S1 = ", S1)

discriminant = b*b - 4*a*c
if discriminant > 0:
    S2 = a * c * (b*b - 4) / (b*b - 4*a*c)
else:
    S2 = 0
print('S2 = ', S2)

a = float(input('Nhập lại a = '))
b = float(input('Nhập lại b = '))
c = float(input('Nhập lại c = '))

if a + b > c and a + c > b and b + c > a:
    print('a,b,c là các cạnh của 1 tam giác')
    chu_vi = a + b + c
    p = (a + b + c) / 2
    diện_tích = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('chu_vi = ', chu_vi)
    print('diện_tích = ', diện_tích)
else:
    print('a,b,c không phải là các cạnh của 1 tam giác')
