import itertools

houses = [1,2,3]
orders = list(itertools.permutations(houses))

print orders

for (red,blue,green) in orders:
    print red, blue, green
