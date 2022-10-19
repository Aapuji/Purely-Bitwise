a = int(input('A: '))
b = int(input('B: '))

print('0ba:', bin(a))
print('0bb:', bin(b))
print('sum:', a + b, bin(a + b))
print('pro:', a * b, bin(a * b))

cmp = lambda n: n == 0

def add(a, b):
    if cmp(b): return a
    return add(a ^ b, (a & b) << 1)

print('--')
print('add:', add(a, b))
print('mul:', mul(a, b))
