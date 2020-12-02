#!/usr/bin/env python3
import utils

def sort(array):
	for i in range(len(array[:-1])):
		low = i
		for j in range(i, len(array)):
			if array[low] > array[j]:
				low = j

		array[i], array[low] = array[low], array[i]
	return array

if __name__ == "__main__":
	array = utils.numbers()
	print(sort(array))
