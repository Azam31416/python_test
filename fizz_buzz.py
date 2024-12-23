def fizz_buzz(number):
	list = []
	for num in range(1,number+1):
		name = ''
		if num%3 == 0:
			name = "Fizz"
		if num%5 == 0:
			name += "Buzz"
		if name != '':
			list.append(name)
		else:
			list.append(num)
	return list
print(fizz_buzz(15))