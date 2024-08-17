# payrollListNonOOP.py

'''
Create a non-Object-Oriented Python console program which does the following:

https://www.w3schools.com/python/python_lists_methods.asp

1.	Uses one or more lists to get the following information about employees:

	a.	Employee number      (must be unique)
	b.	Employee firstName   (cannot be empty)
	c.	Employee lastName    (cannot be empty)
	d.	Employee hoursWorked (must be >= 0.00 and <= 84.0)
	e.	Employee hourlyRate  (must be >= 0.00 and <= 99.99)
	f.	For each employee,   calculate straight time (Non-OT) Gross Pay as: 
		                       hoursWorked * hourlyRate
		  Employees get overtime (time and one-half) for hours > 40
	g.	Utilize the following Python List Methods to:
		1.	append()		      Adds an employee at the end of the list(s)
		2.	clear()			      Removes all employees from the list(s)
		3.	copy()			      Creates a copy of the employee list(s)
		4.	count()			      Returns the number of employees in the list(s)
		5.	index()			      Returns the index of the employee with that emp number
		6.	insert()		      Adds an employee at the specified position
		7.	pop()			        Removes the employee at the specified position
		8.	remove()		      Removes the employee with the specified employee number
		9.	reverse()		      Reverses the order of the list(s)
		10.	sort()			      Sorts the list(s)

Write each input as its own function. Do NOT use object-oriented 
programming in this program
'''

import pythonHeader as pheader
import importlib
importlib.invalidate_caches()
import pythonListMenu as pmenu

def main():
    pheader.getTitle("Lists")
    pmenu.theListMenu()

if __name__ == "__main__":
    main()