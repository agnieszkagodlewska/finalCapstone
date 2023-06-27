# This program allows the user to access two different financial calculators:
# an investment calculator and a home loan repayment calculator.

import math

print("investment - to calculate the amount of interest you'll earn on your investment")  # noqa
print("bond - to calculate the amount you'll have to pay on a home loan\n")
select = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()  # noqa

if select == "investment":

    amount = float(input("Enter the amount of money that you are depositing:\n"))  # noqa
    rate = float(input("Enter the interest rate (as a percentage):\n"))
    r = rate/100  # Changing procentages to fractions in intrest rate.
    time = float(input("Enter the number of years you plan on investing:\n"))
    intrest = input("Enter 'simple' or 'compound' intrest:\n").lower()

    if intrest == "simple":

        total_amount = amount*(1+r*time)
        print("Your total amount is "+str(total_amount)+"£.")

    elif intrest == "compound":

        total_amount = round(amount*math.pow((1+r), time), 2)
        print("Your total amount is "+str(total_amount)+" £.")

elif select == "bond":
    value = float(input("Enter the present valueof the house:\n"))
    rate = float(input("Enter the interest rate (as a percentage):\n"))
    i = (rate/100)/12  # The monthly interest rate.
    time = float(input("Enter the number of months you plan to take to repay the bond.\n")) # noqa
    repayment = (i*value)/(1-(1+i)**(-time))
    repayment = round(repayment, 2)  # Round float to 2 decimals place.
    print("You should to repay "+str(repayment)+" £ each month.")

else:
    print("Invalid input. Please, try again.")
