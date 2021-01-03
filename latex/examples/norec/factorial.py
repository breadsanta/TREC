#!/usr/bin/env python3
def factorial(n):
	res = 1
	while n > 0:
		res *= n
		n -= 1
	return res

n = int(input("Factorial de... "))

if n < 0:
	print("El nombre ha de ser positiu.")
else:
	print(f"El factorial de {n} és {factorial(n)}")
