# ! /usr/bin/env python3
from p5 import *
import random

URL = 'https://picsum.photos/400/'

	
def disassemble(img: PImage) -> list:
	patches = []
	c = 0
	for i in range(10):
		for j in range(10):
			patches.append((c, img[i*40:(i+1)*40, j*40:(j+1)*40]))
			c += 1
	return patches

def assemble(patches: list) -> PImage:
	c = 0
	assembled = PImage(400, 400)
	for i in range(10):
		for j in range(10):
			assembled[i*40:(i+1)*40, j*40:(j+1)*40] = patches[c][1]
			c += 1
	return assembled

def setup():
	global img
	size(400, 400)
	img = load_image(URL)
	img.load_pixels()
	image(assemble(disassemble(img)), 0, 0)
	no_loop()

if __name__ == "__main__":
	run()
