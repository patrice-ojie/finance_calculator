"""The purpose of this project is to create a program that allows the user to access two different financial
calculators: an investment calculator and a home loan repayment calculator."""
import math
# The section is an introduction to the options that are available so the user can make an informed choice
print("Welcome to this Finance Calculator\nInvestment - to calculate the amount of interest "
      "you'll earn on your investment\nBond - to calculate the amount you'll have to pay on a home loan\n")
while True:
    user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if user_choice not in ['investment', 'bond']:
        print("You have made an invalid choice. Please try again.")
    else:
        break

# This section works out the return on an investment, accounting for simple or compound interest
if user_choice == "investment":
    while True:
        try:
            deposit = float(input("How much money are you depositing? £"))
            int_rate = float(input("What is the interest rate. Please only enter the value, the '%' sign isn't "
                                        "needed: "))
            years = int(input("How many years do you want to invest for? "))
            break
        except Exception:
            print("You have entered an invalid value. Please try again.")
    interest_type = input("Do you want simple or compound interest? ").lower()
    
    while True:
        if interest_type not in ['simple', 'compound']:
            print("You have made an invalid choice. Please try again.")
        else:
            break
    if interest_type == "simple":
        simple_return = deposit*(1 + (int_rate/100)*years)
        print(f"You will have £{simple_return:.2f} after {years} years with a deposit of £{deposit:.2f}")
    else:
        compound_return = round(deposit*math.pow((1+int_rate/100), years), 2)
        print(f"You will have £{compound_return} after {years} years with a deposit of £{deposit}")
# This section works out the return on a bond
else:
    while True:
        try:
            house_value = float(input("Please enter the current value of your house: £"))
            house_interest = float(input("What is the interest rate. Please only enter the value, the '%' sign isn't "
                                         "needed: "))
            monthly_interest = house_interest/1200
            months = int(input("How many months will it take for you to repay the bond? "))
            break
        except Exception:
            print("You have entered an invalid value. Please try again.")
    month_fee = (monthly_interest*house_value)/(1-(1+monthly_interest)**(-months))
    print(f"Your monthly repayment will be £{month_fee:.2f}")
