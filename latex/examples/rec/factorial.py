#!/usr/bin/env python3
def factorial(n):
	if n == 0:
		return 1
		
	return n * factorial(n-1)

n = int(input("Factorial de... "))

if n < 0:
	print("El nombre ha de ser positiu.")
else:
	print(f"El factorial de {n} és {factorial(n)}")
