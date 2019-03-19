full_list = []
score_list = []
lowest_names = []
for _ in range(int(input())):
	name = input()
	score = float(input())
	full_list.append([name, score])
	score_list.append(score)
score_list = list(set(score_list))
score_list.sort()
second_lowest = score_list[1]
for score in full_list:
	if score[1] == second_lowest:
		lowest_names.append(score[0])
lowest_names.sort()
print("\n".join(lowest_names))

