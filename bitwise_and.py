# We loop through all possible combinations of a & b from 1 to n -1 and a + 1 to n respectively. 
# All valid values matching the required condition (a & b < k) are added to a running list.
# At the end of the two inner loops, the maximum value of the running list is added to a
# results list.
if __name__ == '__main__':
	t = int(input())
	results = []
	for t_itr in range(t):
		nk = input().split()
		n = int(nk[0])
		k = int(nk[1])
		valid_a_and_b = []
		for a in range(1, n):
			for b in range(a + 1, n + 1):
				if (a & b) < k:
					valid_a_and_b.append(a & b)
		results.append(str(max(valid_a_and_b)))
	print('\n'.join(results))

