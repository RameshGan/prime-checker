"""Finds the Primes using Ératosthène's sieve"""
import math
from typing import List

def is_prime(n: int) -> bool:
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_numbers(upper_limit: int) -> List[int]:
    """
    Finds all prime numbers up to a specified upper limit.
    
    Args:
        upper_limit: The maximum integer to check.
        
    Returns:
        A list of integers that are prime.
    """
    prime_numbers: List[int] = []

    for candidate_number in range(2, upper_limit + 1):
        is_prime: bool = True
        square_root_limit: int = math.isqrt(candidate_number)

        for prime in prime_numbers:
            if prime > square_root_limit:
                break
            
            if candidate_number % prime == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(candidate_number)

    return prime_numbers

def get_composite_numbers (upper_limit : int, prime_numbers  : list[int] | None = None) -> list[int]:
    """Get composite number give a prime number list
        If the numbers aren't provided calculate them first.
    Args:
        limit (int): Limit upto which primes need yto be found out
        prime_numbers : List of prime numbers if already available.

    Returns:
        list[int]: List of composite numbers
    """

    number_range = range(2, upper_limit +1)
    if prime_numbers is None:
        primes  = find_prime_numbers(upper_limit)
    else:
        primes = prime_numbers

    result = list(filter (lambda x : True if x not in primes else False, number_range ))
    
    return result
    
def print_number_list(numbers : list[int]) -> None:
        """Print individual numbers from the list with proper formatting"""
        print(*(f"{number:>6,}" for number in numbers), sep=", ")

if __name__ == "__main__":
    """Find all primes upto 1000"""
    max_range: int = 1010
    primes : List[int] = find_prime_numbers( max_range)
    print(f"Primes up to {max_range}" )
    print_number_list(primes)

    composites = get_composite_numbers(max_range)
    print(f"Composite numbers  up to: {max_range}")
    print_number_list(composites)

    composites = get_composite_numbers(max_range, primes)
    print(f"Composite numbers given primes upt o: {max_range}")
    print_number_list(composites)




