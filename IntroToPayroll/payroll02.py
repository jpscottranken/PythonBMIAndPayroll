# Gleaned from the following URL:
# https://stackoverflow.com/questions/320929/currency-formatting-in-python
import locale
locale.setlocale( locale.LC_ALL, '' )

first = input("Please enter your first name:\t")
last  = input("Please enter your last  name:\t")
hours = input("Please enter your hours worked:\t")
rate  = input("Please enter your hourly  rate:\t")
hwork = float(hours)
hrate = float(rate)
gross = hwork * hrate
print (f"{first} {last} worked {hwork} hours last week.")
print (f"at {locale.currency(hrate)} an hour made {locale.currency(gross)}")