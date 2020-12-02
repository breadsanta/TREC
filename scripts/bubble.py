#!/usr/bin/env python3
import utils

def sort(array):
	while True:
		for i in range(len(array[:-1])):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				break

		# aquest else s'executa si el bloc anterior s'ha executat sense cap break, és a dir, si mai s'ha complert la condició array[i] > array[i+1]
		else:
			break
	return array
		
if __name__ == "__main__":	
	array = utils.numbers()
	print(sort(array))
