#!/usr/bin/env python3
import utils

def sort(array):
	if len(array) < 2:
		return array
	mid = len(array)//2
	left = sort(array[:mid])
	right = sort(array[mid:])

	merged = []
	l = 0
	r = 0

	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			merged += [left[l]]
			l += 1
		else:
			merged += [right[r]]
			r += 1

	if l < len(left):
		merged += left[l:]
	if r < len(right):
		merged += right[r:]

	return merged

if __name__ == "__main__":
	array = utils.numbers()
	print(sort(array))
