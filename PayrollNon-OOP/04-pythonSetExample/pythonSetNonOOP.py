# pythonSetNonOOP.py

'''
Create a non-Object-Oriented Python console program which does the following:

1.	Uses one or more sets to create a payroll program which also demonstrates
		the following Python Set methods:

a.	add()	 							Adds an element to the set (not implemented)
b.	clear()	 						Removes all the elements from the set
c.	copy()	 						Returns a copy of the set
d.	difference()				Returns a set containing the difference between two or more sets
e.	difference_update()	-=		Removes the items in this set that are also included in another, specified set
f.	discard()	 					Remove the specified item
g.	intersection()			&	Returns a set, that is the intersection of two other sets
h.	intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
i.	isdisjoint()	 			Returns whether two sets have a intersection or not
j.	issubset()					<=	Returns whether another set contains this set or not
k. 	<				14						Returns whether all items in this set is present in other, specified set(s)
l.	issuperset()				>=	Returns whether this set contains another set or not
m. 	>										Returns whether all items in other, specified set(s) is present in this set
n.	pop()	 							Removes an element from the set
o.	remove()	 					Removes the specified element
p.	symmetric_difference()	^	Returns a set with the symmetric differences of two sets
q.	symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
r.	union()							|	Return a set containing the union of sets
s.	update()						|=	Update the set with the union of this set and others

Write each input as its own function. Do NOT use object-oriented 
programming in this program
'''

import pythonHeader as pheader
import importlib
importlib.invalidate_caches()
import pythonSetMenu as psmenu
import pythonSetMethods as psm

def main():
    pheader.getTitle("Sets")
    psmenu.theSetMenu()

if __name__ == "__main__":
    main()