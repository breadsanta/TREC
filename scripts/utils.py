#!/usr/bin/env python3
import random

def numbers(min = 0, max= 10, count = 10, seed = None):
	if (seed):
		random.seed(seed)
	return [random.randrange(min, max) for i in range(count)]
