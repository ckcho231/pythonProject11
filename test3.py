def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a = 0
    b = 1
    while a < n:
        print(a, end=', ')
        # a, b = b, a + b
        a = b
        b = a + b
    print()

# 안녕하세요 만나서 반가워요 이런일을 좋아하는것 아니였어요?

# Now call the function we just defined:
fib(100)
