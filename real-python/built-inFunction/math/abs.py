from decimal import Decimal
from fractions import Fraction

# abs(): untuk menghitung nilai absolut(mutlak) suatu angka.
# contoh:
print(abs(-42))
print(abs(42))

print(abs(-42.42))
print(abs(42.42))

print(abs(complex("-2+3j")))
print(abs(complex("2+3j")))

print(abs(Fraction(-1 / 2)))
print(abs(Fraction(1 / 2)))

print(abs(Decimal("-0.5")))
print(abs(Decimal("0.5")))
print("\n")


# studi kasus: hitung laba dan rugi perusahaan dlm satu bulan.
transactions = [-200, 300, -100, 500]

incomes = sum(income for income in transactions if income > 0)
expenses = abs(sum(expense for expense in transactions if expense < 0))

print(f"Total incomes: ${incomes}")
print(f"Total expenses: ${expenses}")
print(f"Total profit: ${incomes - expenses}")

# https://realpython.com/python-built-in-functions/#using-math-related-built-in-functions
