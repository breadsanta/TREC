#!/usr/bin/env python3
import utils

def sort(array):
	if len(array) < 2:
		return array
	
	pivot = array[0] # agafo el primer element com a pivot, pot ser qualsevol
	lower, higher = [], []

	for i in array[:-1]:
		if i < pivot:
			lower.append(i)
		else:
			higher.append(i)

	lower = sort(lower)
	higher = sort(higher)

	return lower + [pivot] + higher

if __name__ == "__main__":
	array = utils.numbers()
	print(sort(array))
