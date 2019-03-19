# Check if a series of numbers are prime or not. We check for divisibility of
# numbers from 2 till n - 1 with n. If any of them is fully divisible, the number
# is not prime. 
if __name__ == "__main__":
	results = []
	t = int(input())
	for _ in range(t):
		found = 0
		n = int(input())
		for div in range(2, n):
			if n % div == 0:
				found = 1
				break
		if found or n == 1:
			results.append('Not prime')
		else:
			results.append('Prime')
	print('\n'.join(results))
		
		
