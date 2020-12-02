#!/usr/bin/env python3
import utils
import insertion

def sort(array):
	step = len(array) // 2
	while step != 0:
		for offset in range(step):
			sorted = insertion.sort(array[offset::step])
			for i in range(len(sorted)):
				array[step*i + offset] = sorted[i]
		step //= 2
	return sorted

if __name__ == "__main__":
	array = utils.numbers()
	print(sort(array))
