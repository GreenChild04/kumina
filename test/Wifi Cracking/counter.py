import time
import threading


def crackPassword():
	start = time.time()
	count = 0
	while count <= 218340105584896:
		count += 1
	end = time.time()
	print((end - start))

if __name__ == "__main__":
	crackPassword()