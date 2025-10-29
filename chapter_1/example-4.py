import time
import threading

def print_fib(number: int):
    def fib(n: int) -> int:
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    print(f'fib({number}) = {fib(number)}')

def fib_no_threading():
    print_fib(35)
    print_fib(36)

start_time = time.time()

fib_no_threading()

end_time = time.time()

print(f'Время работы {end_time - start_time:.4f} c.')