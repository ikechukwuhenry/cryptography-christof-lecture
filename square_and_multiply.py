def square_multiply(base, exponent):
    x = base
    e = bin(exponent)[2:]
    result = x
    i = 1
    while i < (len(e)):
        # print("iteration ", i)
        result = result ** 2
        if e[i] == '1':
            result = result * x
        i = i + 1
    return result

# Example usageclear
print(square_multiply(2,11))