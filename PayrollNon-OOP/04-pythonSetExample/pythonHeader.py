# pythonHeader.py

import pythonSetMenu as psmenu
import pythonSetMethods as psm

def getTitle(titleType):
    print(f"Welcome To My Python Payroll Program")
    print(f"This program will utilize Python {titleType}")
    psmenu.theSetMenu()
    psm.showSetsForMethodExamples()
