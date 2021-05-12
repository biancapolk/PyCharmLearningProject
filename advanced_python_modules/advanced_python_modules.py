"""Python Collections Module"""

from collections import Counter, defaultdict

list = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,]
l = Counter(list)
print(f"Printing the top 3 MOST COMMON numbers as the key and the number of instances as the values: {l.most_common()}")

sentence = 'How many times does each WORD show up in the sentence? Is there a pattern? If so, what is it?'
print(Counter(sentence.split()))

"""Default Dictionary"""
d = {'a':  10, 'b': 20, 'c': 30}
print(d['b'])

# calling the wrong key results in a Traceback : Key Error
# print(d['Wrong'])

d = defaultdict(lambda: 0)

d['correct'] = 100 # creating and calling a correct key

print(d['correct'])

print(d['Incorrect!']) # now using an incorrect value and the default value returns to zero

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
"""Named Tuples"""
mytuple = (10,20,30)
from collections import namedtuple
Dog = namedtuple('Dog', ['age','breed','name']) # constructing a named tuple it is like created a new object in OOP- it is a named index for the value in the format : namedtuple(type name, field name(s))
nea = Dog(age=10, breed='dauchund', name='Nea Polk')
print(nea)