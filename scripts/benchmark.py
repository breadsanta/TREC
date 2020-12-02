import bubble, insertion, merge, quick, selection, shell
import json, utils, time
import sys

sys.setrecursionlimit(8000)

algs = [bubble, insertion, merge, quick, selection, shell]
batches = [125, 250, 500, 1000, 2000, 4000, 8000]

results = {bubble.__name__: {}, insertion.__name__: {}, merge.__name__: {}, quick.__name__: {}, selection.__name__: {}, shell.__name__: {}}

for alg in algs:
	for batch in batches:
		if bubble  == alg and batch > 4000:
			break # el temps d'execució és massa llarg
		start = time.perf_counter()
		alg.sort(utils.numbers(max=batch, count=batch))
		end = time.perf_counter()
		delta = end - start
		results[alg.__name__][batch] = delta
		print(alg.__name__, batch, delta)

print(results)

with open("./data/out.json", "w") as outfile:
	json.dump(results, outfile)
