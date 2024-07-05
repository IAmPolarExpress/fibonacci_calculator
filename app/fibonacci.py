## This is the mainnn fibonacci calculator aslo apparently my computer is lagging and I am typing too fast well how about that huh hmm.

def fib(i):
    if not isinstance(i, int):
        raise TypeError("Input must be type int, ya crazy wackadoo lol XD")
    if i < 0:
        raise ValueError("Are you trying to be cheeky?  You need to enter an int > 1")
    if i == 0:
        return 0
    if i <= 2:
        return 1
    return fib(i - 1) + fib(i - 2)