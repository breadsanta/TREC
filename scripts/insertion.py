#!/usr/bin/env python3
import utils

def sort(array):
	for i in range(len(array)):
		comp = array[i]
		j = i - 1
		while j >= 0 and array[j] > comp:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = comp
	return array

if __name__ == "__main__":
	array = utils.numbers()
	print(sort(array))
