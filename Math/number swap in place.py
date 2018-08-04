# approach 1:
a = a - b
b = a + b
a = b - a

# approach 2: (CtCI P462)
a = a ^ b
b = a ^ b
a = a ^ b
