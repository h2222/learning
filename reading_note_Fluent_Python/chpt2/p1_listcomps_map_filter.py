import time



'''
which one is faster ? listcomps vs map + filter
'''

symbols = '$¢£¥€¤' 

start_t1 = time.time()
l1 = [ord(x) for x in symbols if ord(x) > 127]
print('time1:', time.time() - start_t1)


start_t2 = time.time()
l2 = list(filter(lambda x : x > 127, map(ord, symbols)))
print('time2:', time.time() - start_t2)


'''
To initialize tuples, arrays, and other types of sequences, 
you could also start from a listcomp.

but a genexp saves memory because it yields items one by one using 
the iterator protocol instead of building a whole list just to feed 
another constructor. 
'''
import array

# implement a generator by gen-comps
g1 = (ord(x) for x in symbols)
print(g1)

# initialize a tuple by using generator expressions
g2 = tuple((ord(x) for x in symbols))
# or
# If the generator expression is the single argument in a function call,
#  there is no need to duplicate the enclosing parentheses.
g3 = tuple(ord(x) for x in symbols)
print(g3)
# initialize a array by using g-exp
array_g1 = array.array('I', g2)
print(array_g1)


# T-shirt size and color sizes = [S, M, L] colors = [white, black]
sizes = ['S', 'M', 'L']
colors = ['white', 'black']
for tshirt in ('%s %s' % (color, size) for color in colors for size in sizes):
    print(tshirt)