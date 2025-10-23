import os
import threading

def one_parent_process():
    print(f'Исполняется Python-процесс с идентификатором {os.getpid()}')

    total_threads = threading.active_count()
    threading_name = threading.current_thread().name

    print(f'В данный момент Python исполняет {total_threads} поток(ов)')
    print(f'Имя текущего потока {threading_name}')


def hello_from_thread():
    print(f'Привет от потока {threading.current_thread()}!')


def multi_thread_process():
    hello_thread = threading.Thread(target=hello_from_thread)
    hello_thread.start()

    total_threads = threading.active_count()
    threading_name = threading.current_thread().name

    print(f'В данный момент Python выполняет {total_threads} поток(ов)')
    print(f'Имя текущего потока {threading_name}')
    hello_thread.join()
