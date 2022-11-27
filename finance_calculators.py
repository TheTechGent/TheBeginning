""" SE T12 capstone project 1 """

# math module used to calculate power later in code
import math
# os module used to clear console for clarity when using the program
import os

# welcome message
print("""
     _____________________
    |  _________________  |
    | |              0. | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | x | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|

Welcome to the finance calculator
""")

# conditional flag for continuous running of calculator program
FINANCE_CALCULATOR_RUNNING = True

# loop that stays true until the user enters "end"
while FINANCE_CALCULATOR_RUNNING:


    # opening request asking user to choose which calculator they require
    chosen_calculator = input("""
Choose either 'investment' or 'bond' from the menu below to proceed:
    
investment\t-\tto calculate the amount of interest you'll earn on your investment
bond\t\t-\tto calculate the amount you'll have to pay on a home loan
end\t\t-\tto close finance calculator

Enter choice: """).lower()

    # checks which os this program is running on, then runs appropriate clear command to clear the console
    if os.name == "nt":
        os.system("cls") # for Windows users
    else:
        os.system("clear") # for Mac users
        
    # first condition for main program function, runs if user selected investment.
    if chosen_calculator == "investment":
        
        # 3 user inputs asking for money to deposit, interest rate and years to invest.
        money_deposited = float(input("How much would you like to deposit?\nDeposit:\t£"))

        interest_rate = float(input("\nWhat is the interest rate? exclude % sign\nInterest rate:\t").strip("%"))
        interest_rate_decimal = interest_rate / 100
        
        years_investing = int(input("\nHow many years do you plan to invest this money?\nyears:\t\t"))

        # conditional flag for loop to catch any typos when asking for type of interest
        INCORRECT_INTEREST_TYPE = True

        # loop that stays true until correct options are chosen: simple or compound
        while INCORRECT_INTEREST_TYPE:
            
            # 4th user input - interest type in string
            interest = input("\nWhat type of interest would you like: 'simple' or 'compound'?\ninterest type:\t").lower()

            # conditional block that runs different calculations based on user input of simple or compound, and catches typos
            if interest == "simple":

                total_earned = money_deposited * (1 + interest_rate_decimal * years_investing)
                INCORRECT_INTEREST_TYPE = False
            
            elif interest == "compound":

                total_earned = money_deposited * math.pow((1 + interest_rate_decimal), years_investing)
                INCORRECT_INTEREST_TYPE = False

            else:

                print("Please try again, that was not one of the options.\n")
        
        # tells user total earnings from their chosen inputs to 2 decimal places.
        print(f"\nBased on the figures given, your invested total earnings would be:\n\n£{total_earned:.2f}")
    
    # second condition for main program function, runs if user selected bond.
    elif chosen_calculator == "bond":

        # 3 user inputs requesting house value, interest rate and total number of months to repay
        house_value = float(input("What is the present value of your house?\nHouse Value:\t£").replace("," , ""))

        bond_interest_rate = float(input("\nWhat is the annual interest rate? exclude % sign\ninterest rate:\t").strip("%"))
        monthly_interest_rate = (bond_interest_rate / 12) / 100

        months_repayment = int(input("\nHow many months will you take to repay the bond?\nTotal Months:\t"))

        # bond calculation
        repayment = monthly_interest_rate * house_value / (1 - math.pow(monthly_interest_rate + 1, -months_repayment))

        # tells user total earnings from their chosen inputs to 2 decimal places.
        print(f"\nBased on the figures given, your monthly payments will be:\n\n£{repayment:.2f} per month")
    
    # third condition for main program function, runs if user selected bond.
    elif chosen_calculator == "end":

        FINANCE_CALCULATOR_RUNNING = False
    # final condition for main program function, runs if user did not choose one of the options or had typo.
    else:

        print("That is not one of the three choices, please type your choice again.")

# lines to separate previous results of program running with beginning of next loop, when program starts again
    print("-"*40)

# final print statement when loop breaks and program ends
print("\nThank you for using the Finance Calculator\n")
