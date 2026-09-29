import math

# friends = 0

# friends = friends + 1
# friends += 1
# friends -= 2
# friends *= 3
# friends /= 4
# friends **= 2
# remainder = friends % 3

# print(remainder)

# x = 3.14
# y = 4
# z = 5

# result = round(x)
# result = abs(y)
# result = pow(z, 3)
# result = max(x, y, z)
# result = min(x, y, z)

# print(result)

# print(math.pi)
# print(math.e)

# result = math.sqrt(9)
# result = math.ceil(9.1)
# result = math.floor(9.9)
# print(result)

# Task 1. Calculate circumference of a circle

# radius = float(input('Enter the radius of a circle: '))
# circumference = 2 * math.pi * radius
# print(f'The circumference is : {round(circumference, 2)}cm')

# Task 2. Calculate the area of a circle

# radius = float(input('Enter the radius of a circle: '))
# area = math.pi * pow(radius, 2)
# print(f'The area of a circle is: {round(area, 2)}cm^2')

# Task 3. Find hypotinuze
a = float(input('Enter side A: '))
b = float(input('Enter side B: '))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'Side C = {c}')