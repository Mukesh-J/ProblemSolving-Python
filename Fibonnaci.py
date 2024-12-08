def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Example usage
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci sequence up to {n}: {fibonacci(n)}")
