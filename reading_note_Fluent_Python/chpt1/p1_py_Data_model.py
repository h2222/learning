# coding = utf-8



'''
p29 data model
You can think of the data model as a description of Python as a framework. 
It formalizes the interfaces of the building blocks of the language itself, 
such as sequences, iterators, functions, classes, context managers, and so on. 
'''

# let obj support obj[key] by implemented __getitem__
class my_collection:
    def __init__(self, a):
        self.a = a

    def __getitem__(self, key):
        return self.a[key]

# mc = my_collection({'a':1, 'b':2})
# print('implement : ', mc['a'])



## instance , FrenchDeck (card game)
import collections
# namedtuple can construct a simple tuple to representation a card where the parameters means
# ('tuple name', ['tuple param 1', 'tuple param 2'])
Card = collections.namedtuple('Card', ['rank', 'unit'])

class FrenchDeck:
    # 2-11, J, Q, K, A
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # unit , spades diamonds clubs hearts
    units = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, unit) for unit in self.units for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

card = Card('7', 'diamond')
print(card)
fd = FrenchDeck()
print(len(fd))

# by implemented __getitem__, we can do below thing to obj:
# key-value pair 
print(fd[21])
# slice
print(fd[2:10:3])
# iterable
for c in fd[1:10]:
    pass
# reverse
for c in reversed(fd):
    pass

# choice a random card ? (choice a random item from a sequence obj)
from random import choice
print(choice(fd))


