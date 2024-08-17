# payrollDictionaryNonOOP.py

'''
Create a non-Object-Oriented Python console program which does the following:

https://www.w3schools.com/python/python_dictionaries_methods.asp

1.	Uses one or more dictionaries to get the following information about employees:

	a.	Employee number      (must be unique)
	b.	Employee firstName   (cannot be empty)
	c.	Employee lastName    (cannot be empty)
	d.	Employee hoursWorked (must be >= 0.00 and <= 84.0)
	e.	Employee hourlyRate  (must be >= 0.00 and <= 99.99)
	f.	For each employee,   calculate straight time (Non-OT) Gross Pay as: 
		                       hoursWorked * hourlyRate
		  Employees get overtime (time and one-half) for hours > 40
	g.	Utilize the following Python Dictionary Methods to:
			1.	clear()					Removes all the elements from the dictionary
			2.	copy()					Returns a copy of the dictionary
			3.	fromkeys()			Returns a dictionary with the specified keys and valueS
			4.	get()						Returns the value of the specified key
			5.	items()					Returns a list containing a tuple for each key value pair
			6.	keys()					Returns a list containing the dictionary's keys
			7.	pop()						Removes the element with the specified key
			8.	popitem()				Removes the last inserted key-value pair
			9.	setdefault()		Returns the value of the specified key. 
            							If the key does not exist: insert the key, 
                          with the specified value
			10.	update()				Updates the dictionary with the specified key-value pairs
			11.	values()				Returns a list of all the values in the dictionary

Write each input as its own function. Do NOT use object-oriented 
programming in this program
'''

import pythonHeader as pheader
import importlib
importlib.invalidate_caches()
import pythonDictionaryMenu as pdmenu
import pythonDictionaryMethods as pdm

def main():
    pdm.sleepThenClear()
    pheader.getTitle("Dictionaries")
    pdmenu.theDictionaryMenu()

if __name__ == "__main__":
    main()