def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
