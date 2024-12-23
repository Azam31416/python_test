def sum_of_evens(list):
	even_sum = 0
	for x in list:
		if x%2 == 0:
			even_sum +=x
	return even_sum
print(sum_of_evens([1,2,3,4,3,5,2]))