# Using lambda : Simple functions that do nothing more than evaluate an 
# expression

divide = lambda x, y: x / y

print divide(10., 20)
print divide(50, 60.)

# Python supports a style of programming called functional programming 
# where you can pass functions to other functions to do stuff.

names = [
	'Larry Bird', 'Michael Jordan', 'Magic Johnson', 
	'Kareem Abdul-Jabbar', 'Lebron James', 'Koby Bryant'  
]

print sorted(names)

print sorted(names, key = lambda name: name.split()[-1].lower())

# Return the values that their division by 2 yields zero
mult3 = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print mult3

# otherwise the lengthier

def filterfunc(x):
    return x % 2 == 0

mult4 = filter(filterfunc, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print mult4

# Lambda allows you to define a simple function, but its use is highly 
# restricted. In particular, only a single expression can be specified, 
# the result of which is the return value.

# From docs
# filter(function, iterable)

# Construct a list from those elements of iterable for which function 
# returns true. iterable may be either a sequence, a container which 
# supports iteration, or an iterator. If iterable is a string or a tuple, 
# the result also has that type; otherwise it is always a list. 
# If function is None, the identity function is assumed, that is, 
# all elements of iterable that are false are removed.
#
#