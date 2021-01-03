#!/usr/bin/env python3
def fibonacci(n):
	if n < 2:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Posició del nombre en la successió de Fibonacci: "))

if n < 0:
	print("El nombre ha de ser positiu.")
else:
	print(f"El nombre en posició {n} de la successió de fibonacci és: {fibonacci(n)}")
