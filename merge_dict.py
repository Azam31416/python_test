def merge_dicts(a,b):
	new_dict = a
	for key in b:
		new_dict[key] = b[key]
	print(new_dict)

merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})