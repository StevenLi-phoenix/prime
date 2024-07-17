from collections import defaultdict
from multiprocessing import Pool, cpu_count, freeze_support
from tqdm import tqdm


class DivisorGenerator:
    """Generator class to yield divisors for a given number."""

    def __init__(self, x):
        self.x = x
        self.i = 2
        self.limit = int(x ** 0.5) + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.limit:
            raise StopIteration
        result = (self.x, self.i)
        self.i += 1
        return result

    def __len__(self):
        return self.limit - 2


def check_divisor(args):
    """Helper function to check if a number is divisible by a given divisor."""
    x, i = args
    return x % i == 0


def is_prime_number(x: int) -> bool:
    """Check if a number is prime using multiprocessing to speed up the process."""
    if x <= 1:
        return False

    divisor_generator = DivisorGenerator(x)

    # Create a pool of workers
    with Pool(cpu_count()) as pool:
        # Generate the divisors on the fly and check them in parallel
        for result in tqdm(pool.imap_unordered(check_divisor, divisor_generator), total=len(divisor_generator)):
            if result:
                return False
    return True


def prime_factors(n: int) -> dict:
    """Return the prime factors of a number as a dictionary where keys are factors and values are their counts."""
    factors = defaultdict(int)
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors[divisor] += 1
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors[n] += 1
            break
    return dict(factors)


def prime_factors_str(n: int, symbol=" * ", reverse_order: bool = False) -> str:
    """Retuen the prime factors result generate from prime_factors but in string for for easy readability"""
    factors = prime_factors(n)
    string = []
    for k, v in factors.items():
        for i in range(v):
            string.append(str(k))
    return symbol.join(string) if reverse_order else symbol.join(string[::-1])


if __name__ == '__main__':
    pass
    # Case 1: Judge if the number user input is an prime number or not
    # print(f"This machine have {cpu_count()} CPUs")
    # n = eval(input("Input a number to determined it is prime or not: "))  # hint: 1000000000121 is a prime number
    # if type(n) is not int: raise TypeError("Please input a valid positive integer")
    # print(f"Calculating if {n} is Prime number:")
    # print("(warn: the speed will be slower and slower)")
    # state = is_prime_number(n)
    # print(f"{n} is{'' if state else ' not'} a prime number.")
    # if not state:
    #     print(f"The factor of {n} is:")
    #     print("Calculating n's factors", end="")
    #     print("\r" + " " * 23, end="")
    #     print(f"\rn = {prime_factors_str(n)}")

    # Case 2: Find All Prime Number
    # i = 1
    # while True:
    #     i += 2
    #     state = is_prime_number(i)
    #     print(f"{i} is{'' if state else ' not'} a prime number.")
    #     if state:
    #         with open("prime.txt", "a+") as f:
    #             f.write(str(i))
    #             f.write("\n")




