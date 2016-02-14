import random

# this sort of does the trick, but I am creating n lists in l. I only print item so result looks ok, but if I print n I print n lists with n items.
def printmatrix(n):
	d = [[] for x in range(n)]
	for l in d:
		l = [[(random.getrandbits(1))]] * n
		for item in l:
			item.append((random.getrandbits(1)))
		print(item)
	
def main():
	n = input("Enter n:")
	n = int(n)
	printmatrix(n)

main()
