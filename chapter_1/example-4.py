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

def fib_with_threading():
    thread_1 = threading.Thread(target=print_fib, args=(35,))
    thread_2 = threading.Thread(target=print_fib, args=(36,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

start_time = time.time()

fib_no_threading()

end_time = time.time()

print(f'Время работы для fib_no_threading {end_time - start_time:.4f} c.')

start_time = time.time()

fib_with_threading()

end_time = time.time()

print(f'Время работы для fib_with_threading {end_time - start_time:.4f} c.')