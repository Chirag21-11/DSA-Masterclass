# def factorial(n):
#     assert n >= 0 and int(n) == n, 'The number must be positive integer only dude!'
#     if n in [0,1]:
#         return 1
#     else:
#         return n*factorial(n-1)
    
    
# print(factorial(1.5))


# def fibonacci(n):
#     assert n>=0 and int(n) == n , 'The number must be positive'
#     if n in [0,1]:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(7))



# def sumOfDigits(n):
#     assert n >=0 and int(n) == n , 'The number should be positive'
#     if n == 0:
#         return 0
#     else:
#         return int(n%10) + int(sumOfDigits(n//10))

# print(sumOfDigits(1.5))


# def Power(base,exp):
#     assert int(exp) == exp,'Give positive Number'
#     if exp == 0:
#         return 1
#     elif exp <0:
#         return 1/base* Power(base,exp+1)
#     else:
#         return base * Power(base,exp-1)

# print(Power(4,-1))




# def gcd(a,b):
#     assert int(a) == a and int(b) == b , 'Enter Integers only'
#     if a <0:
#         a=-1*a
#     if b <0:
#         b = -1* b
#     if b == 0:
#         return a
#     else:
#         return gcd(b,a%b)


# print(gcd(10,-122))



def DecimalToBinary(n):
    assert int(n) == n , 'Enter integer!!'
    if n ==0:
        return 0
    else:
        return n%2 + 10 * DecimalToBinary(int(n/2))

print(DecimalToBinary(-13))