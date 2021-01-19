#!/usr/bin/env python3
def fibonacci(n):
	res = 0
	pre_res = 1
	for i in range(n):
		t = pre_res
		pre_res = res
		res += t
	return res
		

n = int(input("Posició del nombre en la successió de Fibonacci: "))

if n < 1:
	print("El nombre ha de ser superior a 0.")
else:
	print(
		f"El nombre en posició {n} de la successió de fibonacci és: {fibonacci(n)}")
