print("HI")
lis = [1,2,3,4,5,6,7,8,9,0]
for i in lis:
    print(i,end=":")

lis2 = ["abcd", "efgh", "ijkl", "mnop"]
for j in lis2:
<<<<<<< HEAD
    print(j, end=":")

lis3 = ["a", "b", "c", "d"]
for x in lis3:
    print(x, end=":")


def triangle(n):
	k = n - 1
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 1
		for j in range(0, i+1):
			print("* ", end="")
		print("\r")
n = 5
triangle(n)


def contnum(n):
	num = 1
	for i in range(0, n):
		for j in range(0, i+1):
			print(num, end=" ")
			num = num + 1
		print("\r")
n = 5
contnum(n)

