RETRIES = 4
def decorator(tries, delay=1):
    """:param tries:
    :param delay:
    :return:
    """
    import time, math
    if tries <0 or delay <=0:
        raise ValueError ("tries must be 0 or greater and delay must be greater than 0")
    def decorate(func):
        def wrapper(*args, **kwargs):
            Thetries=tries
            _delay = delay
            Thetries+=1
            while Thetries>0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    Thetries -=1
                    if Thetries ==0: raise
                    time.sleep(_delay)
        return wrapper
    return decorate
@decorator(RETRIES, delay=0.3)
def my_func():
    import random
    n = random.choice(["p", "y", "t", "h", "o", "n"])
    print ("got  %s" %n)
    if n!="n":
        raise ValueError("Please give me 'n' letter")
    return n
n = my_func()
print("main got %s" %n )