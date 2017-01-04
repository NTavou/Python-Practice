# A list comprehension creates a new list by applying an expression to each 
# element of an iterable. 

squares = [x * x for x in range(10) if x % 2 == 0]

print squares

# else the lengthier

def mult_if_mod_zero(my_iterable):
	my_list = []
	for x in my_iterable:
		if x % 2 == 0:
			my_list.append(x * x) 
	return my_list

print mult_if_mod_zero(range(10))

# Just checking 
print type(range(10))

# From docs
# range(start, stop[, step])
# This is a versatile function to create lists containing arithmetic 
# progressions. It is most often used in for loops.

print mult_if_mod_zero((1,2,3,4,10,20))