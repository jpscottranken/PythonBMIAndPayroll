# Gleaned from the following URL:
# https://stackoverflow.com/questions/320929/currency-formatting-in-python
import locale
locale.setlocale( locale.LC_ALL, '' )

first = "Jeff"
last  = "Scott"
hours = 40.0
rate  = 25.0
gross = float(hours) * float(rate)
print (f"{first} {last} worked {hours} hours last week.")
print (f"at {locale.currency(rate)} an hour made {locale.currency(gross)}")