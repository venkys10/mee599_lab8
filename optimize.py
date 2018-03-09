#!/usr/bin/env python

import numpy as np
import random
import matplotlib.pyplot as plt
import pdb

def f(x):
    return x**3

def optimize_step(f, bounds, n):

    space = np.linspace(f(bounds[0]), f(bounds[1]), n)
    plt.plot(range(n), space)
    return max(space)

def optimize_random(f, bounds, n):

    try:
        rand = random.sample(range(f(bounds[0]), f(bounds[1])), n)
        plt.plot(range(n), rand)
        return max(rand)

    except ValueError:
        print "Sample size is larger than population; give a smaller n value"

def optimize_gradient(f, bounds, epsilon):

    space = np.linspace(f(bounds[0]), f(bounds[1]), 100)
    r = random.choice(space)
    print r
        #gradient ascent
    w_list = []
    h = 0.01
    step_size = 0.002
    diff = 0
    w_n = r
    w_max = 0
    count = 0
    while diff < epsilon or diff < 0:

        gradient = (f(w_n + h) - f(w_n)) / h
        w_max = w_n + step_size * gradient

        diff = w_max - w_n
        
        w_list.append(w_max)
        if w_max > f(bounds[1]):
            w_max = f(bounds[1])
            w_n = w_max
        elif w_max < f(bounds[0]):
            w_max = f(bounds[0])
            w_n = w_max
        else:
            w_n = w_max
        count = count + 1
    print "count", count
    #plt.plot(range(count), w_list, 'ro')
    #plt.show()
    return "max:", w_max

def optimize_md(f, bounds):
    max_v = 0
    max_s = 0
    for i in range(1000):
        s = []
        for min_val, max_val in bounds:
            s.append(random.uniform(min_val, max_val))

            if f(*s) > max_v:
                max_v = f(*s)
                max_s = s

        
    return max_s
        # for elem in bounds(tuples):
        #     max_tup = (f(bounds[elem]))
        #     print max_tup

        

if __name__ == '__main__':
    #x = optimize_step(f, (1,2), 5)
    #y = optimize_random(f, (1,100), 100)
    #print y
    print optimize_gradient(f, (1,5), 1e-5)
    print optimize_md(f, [(2,3), (-2,3), (4,8)])