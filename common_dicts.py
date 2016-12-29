# Finding common keys, values or key-values between dictionaries

a = { 
	'x' : 11, 
	'y' : 9, 
	'z' : 3 
}

b = { 
	'w' : 7, 
	'x' : 11, 
	'y' : 2 
}

c = { 
	'z' : 8, 
	'x' : 11, 
	'y' : 2 
}

# Find common keys 

print set(a.keys()) & set(b.keys()) & set(c.keys())

# Find common values

print set(a.values()) & set(b.values()) & set(c.values())

# Find keys in a that are not in b and c

print set(a.values()) - set(b.values()) - set(c.values())

# Find common (key, value) pairs 

print set(a.items()) & set(b.items()) & set(c.items())