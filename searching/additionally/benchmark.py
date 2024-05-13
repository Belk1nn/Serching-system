import color

def benchmark(func):
    import time
    
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'{color.CYAN}[Execution time]:{color.WHITE} {end - start} sec.')
    return wrapper