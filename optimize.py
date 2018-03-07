#!/usr/bin/env python

import numpy as np
import random

def f(x):
    return x**3

def optimize_step(f, bounds, n):

    space = np.linspace(f(bounds[0]), f(bounds[1]), n)
    return max(space)

def optimize_random(f, bounds, n):

    try:
        rand = random.sample(range(f(bounds[0]), f(bounds[1])), n)
        return max(rand)

    except ValueError:
        print "Sample size is larger than population; give a smaller n value"

def optimize_gradient(f, bounds, epsilon):

    space = np.linspace(f(bounds[0]), f(bounds[1]), 100)
    r = random.choice(space)
    print r
        #gradient ascent
    step_size = 0.2
    diff = 0
    while diff < epsilon:
        w_max = r + step_size
        w_new = w_max
        diff = w_new - w_max

    return "max:", diff


if __name__ == '__main__':
    x = optimize_step(f, (1,2), 5)
    y = optimize_random(f, (1,100), 100)
    #print y
    print optimize_gradient(f, (1,5), 1e-1)