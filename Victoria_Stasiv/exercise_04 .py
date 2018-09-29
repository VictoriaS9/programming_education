class cached(dict):
    def __init__(self, func):
        print("Calculated value => Hello, world")
        self.func = func
    def __call__(self, *args):
        print("Using data from the cache =>" + "Hello, world")
        return self[args]
    def __missing__(self, key):
        result =  self.func(*key)
        return result
@cached
def my_func():
    return " "
my_func()
my_func()
my_func()
my_func()
my_func()