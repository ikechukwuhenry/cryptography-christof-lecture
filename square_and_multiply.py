
def convert_exp_to_binary(exp):
    return format(exp, 'b')

def SAM(x,exp):
    exp_binary_str = convert_exp_to_binary(exp)
    size = len(exp_binary_str)
    ans = x
    if exp == 0:
        return 1
    if exp == 1:
        return ans
    temp_exp = 1
    for i in range(size):
        print(i)
        if exp_binary_str[i] == '1':
           ans = x * ans
        else:
            ans = ans**temp_exp
        temp_exp = 1 + temp_exp
    return ans

N = 1000000007

def exponentiation(bas, exp):
    t = 1;
    while(exp > 0): 
 
        # for cases where exponent
        # is not an even value
        if (exp % 2 != 0):
            t = (t * bas) % N
 
        bas = (bas * bas) % N
        exp = int(exp / 2)
    return t % N


print(SAM(2,7))
# print(convert_exp_to_binary(1))
# print(exponentiation(4,3))