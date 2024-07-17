# Prime Number Checker and Factorizer

This project contains a Python script to check if a given number is prime and to generate its prime factors using multiprocessing for efficiency.

## Description

The script provides functionalities to:
1. Check if a number is prime.
2. Generate prime factors of a given number. (Did not optimize)

It uses multiprocessing to speed up the prime-checking process by dividing the task of checking divisors across multiple CPU cores.

## Requirements

- Python 3.x
- `tqdm` module for displaying progress bars
- `multiprocessing` module for parallel processing
- `collections` module for handling defaultdict

## Installation

To install the required dependencies, run:
```bash
pip install tqdm
```

## Usage

Run the script with the following command:
```bash
python prime.py
```

Follow the prompts to input a number. The script will then determine if the number is prime and, if not, will display its prime factors.

## Example

```
This machine have 8 CPUs
Input a number to determined it is prime or not: 1000000000121
Calculating if 1000000000121 is Prime number:
(warn: the speed will be slower and slower)
100%|████████████████████████████████| 999999/999999 [01:08<00:00, 14616.05it/s]
1000000000121 is a prime number.
```

If the number is not prime, the output will display its factors.

```
This machine have 8 CPUs
Input a number to determined it is prime or not: 24
Calculating if 24 is Prime number:
(warn: the speed will be slower and slower)
  0%|                                                     | 0/3 [00:00<?, ?it/s]
24 is not a prime number.
The factor of 24 is:
n = 3 * 2 * 2 * 2
```

## Functions and Classes

### `DivisorGenerator`

A generator class to yield divisors for a given number.

- `__init__(self, x)`: Initializes the generator with a number `x`.
- `__iter__(self)`: Returns the iterator object.
- `__next__(self)`: Returns the next divisor pair `(x, i)`.

### `check_divisor(args)`

Helper function to check if a number is divisible by a given divisor.

- `args`: A tuple `(x, i)` where `x` is the number and `i` is the divisor.

### `is_prime_number(x: int) -> bool`

Checks if a number is prime using multiprocessing to speed up the process.

- `x`: The number to check.
- Returns `True` if the number is prime, `False` otherwise.

### `prime_factors(n: int) -> dict`

Returns the prime factors of a number as a dictionary where keys are factors and values are their counts.

- `n`: The number to factorize.
- Returns a dictionary of prime factors.

### `prime_factors_str(n: int, symbol=" * ", reverse_order: bool = False) -> str`

Returns the prime factors result generated from `prime_factors` but in string form for easy readability.

- `n`: The number to factorize.
- `symbol`: The symbol to use between factors.
- `reverse_order`: If `True`, factors are displayed in reverse order.
- Returns a string representation of the prime factors.


## Author

Steven Li

For any inquiries, please contact me at [sl10429@nyu.edu](mailto:sl10429@nyu.edu).
