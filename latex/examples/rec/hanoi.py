#!/usr/bin/env python3
def hanoi(n, start, end, aux):
	if n == 1:
		print(f"Mou 1 de {start} a {end}")
		return
	hanoi(n-1, start, aux, end)
	print(f"Mou {n} de {start} a {end}")
	hanoi(n-1, aux, end, start)


n = int(input("Nombre de discs: "))

if n < 1:
	print("Hi ha d'haver com a mínim un disc.")
else:
	hanoi(n, 'A', 'B', 'C')
