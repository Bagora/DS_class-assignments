import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"Execution time: {execution_time:.5f} seconds")
        return result
    return wrapper

@timer
def my_function():
    # Function code goes here
    time.sleep(2)

my_function()
