# find the greatest common divisor of 2 inputs
def gcd(a, b):
    if a == 0: return b
    return gcd(b % a, a)

# 2 integers a and b are Relatively prime if the 
# GCD (Greatest Common Divisor) of them is 1.
def relative_prime(a, b):
    return gcd(a, b) == 1

# Synonymous to relatively prime
def coprime(a, b):
    return gcd(a, b) == 1

# Euler’s Phi function ? (n) for an input n 
# is the count of numbers in {1, 2, 3, …, n-1} 
# that are relatively prime to n, i.e., the numbers whose 
# GCD (Greatest Common Divisor) with n is 1.
def euler_phi(n):
    result = 1
    i  = 2
    while i < n:
        if coprime(i, n):
            result += 1
        i += 1
    return result

#  function for extended Euclidean Algorithm 
def gcdExtended(a, b): 
    # Base Case 
    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 


# print(euler_phi(13))
print(gcd(3,20))
print(gcdExtended(7,20))