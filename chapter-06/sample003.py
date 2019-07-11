import experiment
import experiment

import example
print(example.x)

example.x = 7
print(example.x)

import importlib
example = importlib.reload(example)
print(example.x)

import math
print(math.pi)
math.pi = 3
print(math.pi)
math = importlib.reload(math)
print(math.pi)

import imp
math = imp.reload(math)
print(math.pi)