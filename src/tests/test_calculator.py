from prime_wizard.calculator import is_prime # Adjust if your function name differs

def test_basic_primes():
    assert is_prime(7) is True
    assert is_prime(13) is True

def test_non_primes():
    assert is_prime(4) is False
    assert is_prime(9) is False

def test_negative_numbers():
    assert is_prime(-5) is False