#dupa
def prime_checker(n):
    is_prime=True
    for dupa in range(2, n):
        if(n%dupa==0):
            is_prime=False
            print('NIEPIERWSZAKURWA')
            break
    if (is_prime): print('pierwsza kurwa')
while 1:
    n=int(input('sprawdzanie pierwszych'))
    prime_checker(n)