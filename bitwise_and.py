# The previous version of the code was fixed to address the code timeout issue in the first version.
# It ended up failing basic test cases on hackerrank. This version combines the approaches from
# the previous versions - looping through a in reverse and exiting the loop on a condition.
# The maximum possible value of k less than k is k - 1 and if we see this value in any a & b
# evaluation, we exit the inner loops and add the value to the final results list. If it is
# not encountered, we find the maximum of the other 'valid' (a & b less than k) values.
# This version passed all basic and hidden test cases on hackerrank and is the final submission.
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
				if (a & b) == k - 1:
					results.append(str(a & b))
					found = 1
					break
				if (a & b) < k:
					valid_a_and_b.append((a & b))
			if found == 1:
				break
		if not found:
			results.append(str(max(valid_a_and_b)))
	print('\n'.join(results))
