# pythonTupleNonOOP.py

'''
Create a non-Object-Oriented Python console program which does the following:

1.	Uses one or more tuples to get the following information about employees:

	a.	Employee number      (must be unique)
	b.	Employee firstName   (cannot be empty)
	c.	Employee lastName    (cannot be empty)
	d.	Employee hoursWorked (must be >= 0.00 and <= 84.00)
	e.	Employee hourlyRate  (must be >= 0.00 and <= 99.99)
	f.	For each employee,   calculate straight time (Non-OT) Gross Pay as: 
		                       hoursWorked * hourlyRate
		  Employees get overtime (time and one-half) for hours > 40
	g.	Utilize the following Python Tuple Methods to:
			1.	count()					Returns the number of times a specified value 
            							occurs in a tuple
			2.	index()					Searches the tuple for a specified value and 
            							returns the position of where it was found

Write each input as its own function. Do NOT use object-oriented 
programming in this program
'''

import pythonHeader as pheader
import importlib
importlib.invalidate_caches()
import pythonTupleMenu as ptmenu
import pythonTupleMethods as ptm

def main():
    pheader.getTitle("Tuples")
    ptmenu.theTupleMenu()

if __name__ == "__main__":
    main()