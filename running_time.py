# Check if a series of numbers are prime or not. We check for divisibility of
# numbers from 2 till n - 1 with n. If any of them is fully divisible, the number
# is not prime. 
# The first version used a brute-force method to check for divisibility with all
# numbers. There are more efficient techniques available. The code has been 
# re-written to implement the logic detailed here:
# https://en.wikipedia.org/wiki/Primality_test


def is_prime(num):
	if num <= 3:
		return num > 1
	elif (num % 2 == 0) or (num % 3 == 0):
		return False
	i = 5
	while i * i <= num:
		if (num % i == 0) or (num % (i + 2) == 0):
			return False
		i = i + 6
	return True

if __name__ == "__main__":
	results = []
	t = int(input())
	for _ in range(t):
		num = int(input())
		if not is_prime(num):
			results.append('Not prime')
		else:
			results.append('Prime')
	print('\n'.join(results))
		
		
