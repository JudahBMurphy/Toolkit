def indent(spaces):
    indent = ' ' * spaces
    return indent

def dict_navigation(dictionary):
    for x in dictionary.keys():
        print(f'{indent(4)}{x}')
    user_input = input()
    if user_input in dictionary:
        if isinstance(dictionary[user_input], dict):
            sub_dict = dictionary[user_input]
            for y in sub_dict:
                print(f'{indent(4)}{y}: {sub_dict[y]}')
        else:
            print(f'{indent(4)} {dictionary[user_input]}')
    elif int(user_input) == 0:
        print('Goodbye')
    else:
        print('Data Type does not exist')

def display_functions_library():
    function_dict = {
        '.abs()': {
            'Arguements': 'Any int, float,',
            'Description': 'Returns the absolute value of a number'
            },
        '.all()': {
            'Arguements': 'iterable',
            'Description': 'Return True if all elements of the iterable are true (or if the iterable is empty).'
            },
        '.any()': {
            'Arguements': 'iterabel',
            'Description': 'Return True if any element of the iterable is true. If the iterable is empty, return False. .'
            },
        '.bool()': {
            'Arguements': 'any',
            'Description': 'Return a Boolean value, i.e. one of True or False.'
            },
        '.callable()': {
            'Arguements': 'object',
            'Description': 'Return True if the object argument appears callable, False if not.'
            },
        '.divmod()': {
            'Arguements': 'x, y',
            'Description': 'Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.'
            },
        '.enumerate()': {
            'Arguements': 'iterable, start = index',
            'Description': 'Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.'
            },
        '.float()': {
            'Arguements': 'number',
            'Description': 'Return a floating point number constructed from a number or string x.'
            },
        '.frozenset()': {
            'Arguements': 'iterable = set()',
            'Description': 'Return a new frozenset object, optionally with elements taken from iterable.'
            },
        '.hash()': {
            'Arguements': 'object',
            'Description': 'Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup.'
            },
        '.id()': {
            'Arguements': 'object',
            'Description': 'Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime.'
            },
        '.input()': {
            'Arguements': 'prompt',
            'Description': 'Get user input. If the prompt argument is present, it is written to standard output without a trailing newline.'
            },
        '.int()': {
            'Arguements': 'number',
            'Description': 'Return an integer object constructed from a number or string x, or return 0 if no arguments are given.'
            },
        '.isinstance()': {
            'Arguements': 'object, classinfo',
            'Description': 'Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect, or virtual) subclass thereof. If object is not an object of the given type, the function always returns False.'
            },
        '.issubclass()': {
            'Arguements': 'class, classinfo',
            'Description': 'Return True if class is a subclass (direct, indirect, or virtual) of classinfo. A class is considered a subclass of itself.'
            },
        '.iter()': {
            'Arguements': 'object',
            'Description': 'Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, object must be a collection object which supports the iterable protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then object must be a callable object.'
            },
        '.len()': {
            'Arguements': 'anything',
            'Description': 'Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).'
            },
        '.list()': {
            'Arguements': 'iterable',
            'Description': 'Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.'
            },
        '.map()': {
            'Arguements': 'function, iterable',
            'Description': 'Return an iterator that applies function to every item of iterable, yielding the results. If additional iterables arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.'
            },
        '.max()': {
            'Arguements': 'iterable',
            'Description': 'Return the largest item in an iterable or the largest of two or more arguments.'
            },
        '.min()': {
            'Arguements': 'iterable',
            'Description': 'Return the smallest item in an iterable or the smallest of two or more arguments.'
            },
        '.next()': {
            'Arguements': 'iterator',
            'Description': 'Retrieve the next item from the iterator by calling its __next__() method.'
            },
        '.open()': {
            'Arguements': 'file',
            'Description': 'Open file and return a corresponding file object.'
            },
        '.pow()': {
            'Arguements': 'base, exp, mod=None',
            'Description': 'Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently than pow(base, exp) % mod).'
            },
        '.print()': {
            'Arguements': 'anything',
            'Description': 'Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.'
            },
        '.range()': {
            'Arguements': 'start index, stop index',
            'Description': 'Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range.'
            },
        '.reversed()': {
            'Arguements': 'sequence',
            'Description': 'Return a reverse iterator.'
            },
        '.round()': {
            'Arguements': 'number',
            'Description': 'Return number rounded to ndigits precision after the decimal point.'
            },
        '.sorted()': {
            'Arguements': 'iterable',
            'Description': 'Return a new sorted list from the items in iterable.'
            },
        '.str()': {
            'Arguements': 'object',
            'Description': 'Return a str version of object. '
            },
        '.sum()': {
            'Arguements': 'iterable',
            'Description': 'Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string.'
            },
        '.tuple()': {
            'Arguements': 'iterable',
            'Description': 'Rather than being a function, tuple is actually an immutable sequence type, as documented in Tuples and Sequence Types — list, tuple, range.'
            },
        '.type()': {
            'Arguements': 'object',
            'Description': 'With one argument, return the type of an object.'
            },
        '.zip()': {
            'Arguements': 'iterable1, iterable2',
            'Description': 'Iterate over several iterables in parallel, producing tuples with an item from each one.'
            },
    }

    print("Python Documentation: https://docs.python.org/3/library/functions.html#type")
    print('See below for all functions. Type the name of one to see details')
    dict_navigation(function_dict)

def display_functions_methods_library():
    print('''What do you need?
Choose from list by typing in corresponding number:
    1. List built-in functions
    2. Methods by built in type
    0. End Program''')
    help_input = int(input())
    menu_loop_control = False

    while menu_loop_control != True:
        match help_input:
            case 0:
                menu_loop_control = True
            case 1:
                display_functions_library()
                menu_loop_control = True
            case 2:
                menu_loop_control = True
            case _:
                print('Command not recognized. Try again using specified options.')
                help_input = int(input())
