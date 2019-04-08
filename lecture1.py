print ("ABCD")
a = 5 # is a integer type
b = 5.1 # this is a float type
c = "Hello World" #this is a string
print (c)
d, e = True, False #two assignements together, one should avoid such assignments
f = None

z = a # no new memory location created but is same as 'a'
print (a is z) # checking if a and z are stored in the same location, or to say are these same objects

print (type(a))

w = 5
u = 5
print (w is u) # this is a result of memory optimisation. The output will be true

t = 500
y = 500
print (t is y)  # this will throw up false because it is not optimised

a + b
print (float (a+b)) #keeps the decimal point
print (int (a+b)) # chops off the decimal

a += 5 # adds 5 to the exisitng value of a. Can be useful in assigning counters for loops

c = "how are ya' doing"
print (c.upper())

print (c.split("are"))

#Python Container and Indexing

a = ['a', 'b'] # square brackets for list
b = {} 
c = ('a' , 'b') # is tuple. Tuple is immutable
d = set(['a', 'b']) # Elements of a set need to be unique. If not it will drop all the elements

x = [1, 1, 2 ,3 ,4 ,5] #redundacy is not a problem for list
print (x = set(x)) # will remove the redundant 1's. Is used to create unique list
y = set([1, 2])
z = set([5, 6, 7])

print (x)
print (y)
print (z)

print (x.difference(z)) # performing the set operation of x minus z

x = [1, 2, 3, 4, 5, 5]
x = list(set(x))
print (x)

a, b, c = [1, 2, 3] # this is called unpacking
print (a)
print (b)

a, b,*c = [1, 2, 3, 4] 

print (c) # the * sign creates a list

print(c[0]) #returns the first element which is indexed as 0

d = [1, 2, 3, 4, 5, 'aa', True, False, 'yes', ['hi', 'bye'], None]
print (d[2:4]) #returns everything from position 3 to position 5. Check on the openess of the range

print (d[:]) #returns the entire list. Is useful to assign the set of elements to a new memory location
print (d[::2]) # returns every second term starting from index 0
print (d[::-2]) #reversing the list


