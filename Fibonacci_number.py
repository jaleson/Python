#! python

def fab(n):
    a,b = 0,1
    while n >=2:
        b, a = a+b, b
        n = n-1
    return b;

print fab(3)
print fab(5)
print fab(10)
