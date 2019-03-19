# We check the conditions for no fine first - if the actual date of return
# is earlier than the expected date. If these are not met, we proceed to
# check for late returns and levy an appropriate fine as determined by
# the delay period.
if __name__ == "__main__":
	actual_date = input().split(' ')
	expected_date = input().split(' ')
	actual_day, actual_month, actual_year = int(actual_date[0]), int(actual_date[1]), int(actual_date[2])
	expected_day, expected_month, expected_year = int(expected_date[0]), int(expected_date[1]), int(expected_date[2])
	if actual_year < expected_year:
		fine = 0
	elif (actual_year == expected_year) and (actual_month < expected_month):
		fine = 0
	elif (actual_month == expected_month) and (actual_day <= expected_day):
		fine = 0
	elif (actual_year == expected_year) and (actual_month == expected_month) and (actual_day > expected_day):
		fine = (actual_day - expected_day) * 15
	elif (actual_year == expected_year) and (actual_month > expected_month):
		fine = (actual_month - expected_month) * 500
	else:
		fine = 10000
	print(fine)
