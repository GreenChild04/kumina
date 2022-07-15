import time
import threading


def crackPassword():
	start = time.time()
	count = 0
	times = 10 ** 8
	while count <= times:
		count += 1
	end = time.time()
	print((end - start))
	input()

if __name__ == "__main__":
	crackPassword()