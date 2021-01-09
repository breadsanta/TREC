#!/usr/bin/env python3
import bubble, insertion, merge, quick, selection, shell
import json, utils, time, sys

sys.setrecursionlimit(8000)

algs = [bubble, insertion, merge, quick, selection, shell]
batches = [125, 250, 500]#, 1000, 2000, 4000, 8000]
iters = 3

results = []


for i in range(iters):
	results.append({})
	for alg in algs:
		results[i].update({alg.__name__: {}})
		print(results)
		for batch in batches:
			if alg == bubble and batch > 4000:
				break # el temps d'execució és massa llarg
			
			unsorted = utils.numbers(max=batch, count=batch)
			
			start = time.perf_counter()
			alg.sort(unsorted)
			end = time.perf_counter()
			delta = end - start
			results[i][alg.__name__][batch] = delta
			print(i, alg.__name__, batch, delta)

print(results)

with open("./data/out.json", "w") as outfile:
	json.dump(results, outfile)
