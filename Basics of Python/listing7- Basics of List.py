# List 
"""
It is a data structure in Python. Implicitly it is avaiable in Python.
-> It is a collection of items.
-> It is mutable, meaning we can change the items in the list.  Mutable--> Changeable, can be altered once it is fixed. 
-> Ordered collection of items --> Ordered - indexed 
-> Python Follows zero Indexing - The first element is always at index = 0 
-> Square brackets are used to define a list. E.g., [1, 2, "hello World", 3.14, True, [0,1]]
-> Lists can contain items of different data types, including other lists.
-> List supports negative indexing, meaning we can access elements from the end of the list using negative numbers.
"""


"""
>>> i = 10
>>> dir(i) # Returns a list of attributes (Variables) and methods (functions) of the object i
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
>>> i = -10 
>>> i.__rpow__(2) # Right Power Operator
0.0009765625
>>> i = 2
>>> i.__rpow__(2)
4
>>> i.__class__
<class 'int'>
"""

l = [1, 2, 3]
dir(l)
"""['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']""" 

print(len(l))  # Returns the number of items in the list

print(l[-1])  # Accessing the last item in the list using negative indexing

"""
append(element) method: one Argument 
The append() method is used to add an item to the end of the list.
>>> l.append(4)
>>> l
[1, 2, 3, 4]
"""

"""
insert(index, element) method: two Arguments
The insert() method is used to add an item at a specific index in the list.
>>> l.insert(0,1)
>>> l
[1, 1, 2, 3, 4]
>>> l.insert(1, 1.5)
>>> l
[1, 1.5, 1, 2, 3, 4]
"""

"""
pop() method: No Arguments
The pop() method is used to remove and return the last item from the list. If an index is specified, it removes and returns the item at that index.
>>> l.pop()
4
>>> l
[1, 1.5, 1, 2, 3]

"""

"""
remove(element) method: one Argument
The remove() method is used to remove the first occurrence of a specified item from the list. If the item is not found, it raises a ValueError.
>>> l.remove(1.5)
>>> l
[1, 1, 2, 3]    
>>> l.remove(1.5)
>>> l
[1, 1, 2]
>>> l.remove(1)
>>> l
[1, 2]
>>> l.append(1)
>>> l
[1, 2, 1]
>>> l.remove(1)
>>> l
[2, 1]
"""



