#!/usr/bin/env python3
import bubble, insertion, merge, quick, selection, shell
import json, utils, time, sys

sys.setrecursionlimit(8000)

algs = [bubble, insertion, merge, quick, selection, shell]
batches = [125, 250, 500, 1000, 2000, 4000, 8000]
iters = 5

results = {}

for alg in algs:
	results[alg.__name__] = []
	for i in range(iters):
		results[alg.__name__].append({})
		print(results)
		for batch in batches:
			if alg == bubble and batch > 4000:
				break # el temps d'execució és massa llarg
			
			unsorted = utils.numbers(max=batch, count=batch)
			
			start = time.perf_counter()
			alg.sort(unsorted)
			end = time.perf_counter()
			delta = end - start
			results[alg.__name__][i][batch] = delta
			print(alg.__name__, i, batch, delta)

print(results)

with open("./data/out.json", "w") as outfile:
	json.dump(results, outfile)
