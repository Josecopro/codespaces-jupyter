n = 7


def IntegerReplacement(n, Counter = 0):
    print("Counter = ", Counter)
    if n == 1:
        return Counter
    if n % 2 == 0:
        Counter =  IntegerReplacement(n/2, Counter + 1)
    else:
      Counter = min(IntegerReplacement(n +1, Counter + 1),IntegerReplacement(n - 1, Counter + 1) )

    return Counter

print(IntegerReplacement(n))  
        