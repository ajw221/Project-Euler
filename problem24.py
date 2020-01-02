from itertools import permutations
def problem24():
	string = "0123456789"
	combos = list(permutations(string,len(string)))
	arr = []
	for a in combos:
		temp = ""
		for b in range(len(a)):
			temp+=a[b]
		arr.append(int(temp))
	arr.sort()
	return arr[999999]