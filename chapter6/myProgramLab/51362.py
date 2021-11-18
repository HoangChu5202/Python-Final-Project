x = 1
y = "two"
z = 0
try:
    z = int(y) +int(x)
except ValueError:
    z = -1

print(z)