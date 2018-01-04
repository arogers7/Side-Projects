#index corresponds to number (zero is invalid)
#empty means it is prime
all_numbers = [[],[],[]]
primes = [2]
limit = 1e27
min_divisors = 4e6
def find_prime_divisor(num):
    for prime in primes:
        if num % prime == 0:
            return prime
        if prime*prime > num:
            return 0
    return 0

if __name__ == '__main__':
    limit = 1e27
    min_divisors = 4e6
    test = [2,4,6,8]
    binary_search(test,4)
    """
    for i in range(3,limit):
        prime_divisor = find_prime_divisor(i)
        if prime_divisor == 0:
            primes.append(i)
            all_numbers.append([])
        else:
            all_numbers.append(all_numbers[i/prime_divisor].copy())
            try:
                all_numbers[i]
            except (KeyError):
                all_numbers[i]
    """
    #dictionary has 'KeyError'
