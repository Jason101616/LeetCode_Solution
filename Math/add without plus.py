# CtCI 17.1
# idea is seperating the add the carry part
# approach 1: recurse
def add(a, b):
    if b == 0:
        return a
    sum = a ^ b
    carry = (a & b) << 1
    return add(sum, carry)

# approach 2: iterate
def add(a, b):
    while b:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    return a