"""The purpose of this project is to create a program that allows the user to access two different financial
calculators: an investment calculator and a home loan repayment calculator."""
import math
# The section is an introduction to the options that are available so the user can make an informed choice
print("Welcome to this Finance Calculator\nInvestment - to calculate the amount of interest "
      "you'll earn on your investment\nBond - to calculate the amount you'll have to pay on a home loan\n")
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

lower_case_choice = user_choice.lower()
if lower_case_choice != "investment" and lower_case_choice != "bond":
    print("You have made an invalid choice.")
# This section works out the return on an investment, accounting for simple or compound interest
elif lower_case_choice == "investment": 
    deposit = float(input("How much money are you depositing? £"))
    interest_rate = float(input("What is the interest rate. Please only enter the value, the '%' sign isn't needed: "))
    years = int(input("How many years do you want to invest for? "))
    interest_type = input("Do you want simple or compound interest? ")
    lower_case_interest = interest_type.lower()
    
    if lower_case_interest != "simple" and lower_case_interest != "compound":
        print("You have made an invalid choice.")
    elif lower_case_interest == "simple":
        simple_return = round(deposit*(1 + (interest_rate/100)*years), 2)
        print(f"You will have £{simple_return} after {years} years with a deposit of £{deposit}")
    else:
        compound_return = round(deposit*math.pow((1+interest_rate/100), years), 2)
        print(f"You will have £{compound_return} after {years} years with a deposit of £{deposit}")
# This section works out the return on a bond
else:
    house_value = float(input("Please enter the current value of your house: £"))
    house_interest = float(input("What is the interest rate. Please only enter the value, the '%' sign isn't needed: "))
    monthly_interest = house_interest/1200
    months = int(input("How many months will it take for you to repay the bond? "))
    monthly_repayment = round((monthly_interest*house_value)/(1-(1+monthly_interest)**(-months)), 2)
    print(f"Your monthly repayment will be £{monthly_repayment}")
