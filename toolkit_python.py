def test_print():
	print("Python Toolkit")

def indent(spaces):
	indent = ' ' * spaces
	return indent

def dict_navigation(dictionary):
	for x in dictionary.keys():
		print(f'{indent(4)}{x}')
	user_input = input()
	if user_input in dictionary:
		if user_input == dict:
			sub_dict = dictionary[user_input]
			for y in sub_dict:
				print(f'{indent(4)}{y}: {sub_dict[y]}')
		else:
			print(f'{indent(4)} {dictionary[user_input]}')
	elif int(user_input) == 0:
		print('Goodbye')
	else:
		print('Data Type does not exist')

def data_type_library():
	data_type_dict = {
		'integer': {
			'Class': 'int', 
			'Category':'numerics',
			'Kind': 'primative',
			'Mutable': 'No'
			},
		'float': {
			'Class': 'float', 
			'Category':'numerics',
			'Kind': 'primative',
			'Mutable': 'No'
			},
		'boolean': {
			'Class': 'bool', 
			'Category':'booleans',
			'Kind': 'primative',
			'Mutable': 'No'
			},
		'string': {
			'Class': 'str', 
			'Category':'text sequences',
			'Kind': 'primative',
			'Mutable': 'No'
			},
		}

	print('See below for all data types. Type the name of one to see details')
	dict_navigation(data_type_dict)

def collections_library():
	collections_dict = {
		'range': {
			'Class': 'range', 
			'Category':'sequences - homogeneous',
			'Kind': 'non-primative',
			'Mutable': 'No',
			'example': 'my_range = range()'
		},
		'tuples': {
			'Class': 'range', 
			'Category':'sequences - heterogeneous',
			'Kind': 'non-primative',
			'Mutable': 'No',
			'example': 'my_tuple = (any data type)'
		},
		'lists': {
			'Class': 'range', 
			'Category':'sequences - heterogeneous',
			'Kind': 'non-primative',
			'Mutable': 'Yes',
			'example': 'my_list = [any data type]'
		},
		'dictionaries': {
			'Class': 'dict', 
			'Category':'maps',
			'Kind': 'non-primative',
			'Mutable': 'Yes',
			'example': 'my_dict = {key:value, key:value}'
		},
		'sets': {
			'Class': 'set', 
			'Category':'set',
			'Kind': 'non-primative',
			'Mutable': 'Yes',
			'example': 'my_set = set(any data type)'
		},
		'frozen sets': {
			'Class': 'frozenset', 
			'Category':'set',
			'Kind': 'non-primative',
			'Mutable': 'No',
			'example': 'my_set = set(any data type)'+f'\n{indent(13)}frozen_set = frozenset(my_set)'
		},
	}
	print('See below for all collection types. Type the name of one to see details')
	dict_navigation(collections_dict)

def loop_library():
	library_dict = {
		'while loops': 'example',
		'for loops': 'example',
		'comprehensions': {
			'list comprehensions': 'my_list = [expression for element in iterable if condition]',
			'dict comprehensions': 'my_dict = {key:value for element in iterable if condition}',
			'set comprehensions': 'my_set = {expression for element in iterable if condition}',
		},
	}
	print('See below for all collection types. Type the name of one to see details')
	dict_navigation(library_dict)

#def function_method_library():

def concept_library():
	concept_dict = {
		'Truthiness': '''Truthiness is how python evaluates a value. All values are truthy except the following:
	- False
	- None
	- 0
	- 0.0
	- "" (an empty string)
	- [] (an empty list)
	- {} (an empty dictionary)
	- () (an empty tuple)
	- set() (an empty set)
	- frozenset() (an empty frozenset)
	These values are all considered falsy.

A truthy value allows for the use of any conditional or logical expression, while a falsy value will not''',
	'Precedence': '''The rules that dictate what order Python executes operands. Use parentheses to override the default order.'''
	}
	print('See below for a list of concepts. Type the name of one to see explaination')
	dict_navigation(concept_dict)


