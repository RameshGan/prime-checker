"""Finds the Primes using Erosthane's seive"""
import math
from typing import List


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


if __name__ == "__main__":
    """Find all primes upto 100"""
    max_range: int = 100
    results: List[int] = find_prime_numbers(max_range)
    print(f"Primes up to {max_range}: {results}")

    #added for second commit on composites branch
    #Filter out all the primes in the range and get the composites
    numbers : list[int] = range(2,101)
    composites = list(filter(lambda x : True if  x not in results else False, numbers))
    print(f"Composites upto  {max_range} : {composites}")

