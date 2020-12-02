#!/usr/bin/env python3
import utils

def sort(array):
	for i in range(len(array)):
		for j in range(len(array[:i])):
			if array[i] < array[j]:
				array[i], array[j] = array[j], array[i]
	return array

if __name__ == "__main__":
	array = utils.numbers()
	print(sort(array))
