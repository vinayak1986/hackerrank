# The first version of the code caused code timeout issues. This is an attempt to fix
# it by looping through a in reverse order - n-1 to 1. We exit the loop at the first
# encounter of a number satisfying the condition - a & b < k. If nothing was found,
# we add 0 to the results list.
if __name__ == '__main__':
	t = int(input())
	results = []
	for t_itr in range(t):
		found = 0
		nk = input().split()
		n = int(nk[0])
		k = int(nk[1])
		valid_a_and_b = []
		for a in range(n - 1, 0, -1):
			for b in range(a + 1, n + 1):
				if ((a & b) < k) and ((a & b) > 0):
					results.append(str(a & b))
					found = 1
					break
			if found == 1:
				break
		if not found:
			results.append(str(0))
	print('\n'.join(results))
