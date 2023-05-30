import math


def investment_calculator(amount, interest_rate, years, interest):
    if interest == "simple":
        future_value = amount * (1 + interest_rate/100)**years
    else:
        future_value = amount * math.pow((1 + interest_rate/100), years)
        return future_value


def home_loan_repayment_calculator(amount, interest_rate, years):
    monthly_interest_rate = interest_rate / 12
    number_of_payments = years * 12
    monthly_payment = amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate)**(-number_of_payments))
    return monthly_payment


def main():
    print("Welcome to the financial calculator!")
    while True:
        print("Please choose what you would like to calculate:")
        print("1. Investment")
        print("2. Home loan repayment")
    

        choice = input("Enter your choice: ")

        if choice == "1":
            print("You have chosen to calculate an investment.")
            amount = float(input("Enter the amount of money you want to invest: "))
            interest_rate = float(input("Enter the interest rate (as a percentage): "))
            years = int(input("Enter the number of years you want to invest for: "))

            interest = input("Would you like simple or compound interest? ")

            future_value = investment_calculator(amount, interest_rate, years, interest)

            print("The future value of your investment is R", future_value)
            break

        elif choice == "2":
            print("You have chosen to calculate a home loan repayment.")


            present_value = float(input("Enter the present value of the house: "))
            interest_rate = float(input("Enter the interest rate: "))
            years = int(input("Enter the number of months you plan to take to repay the bond: "))

            monthly_payment = home_loan_repayment_calculator(present_value, interest_rate, years)
            print("Your monthly repayment will be R", monthly_payment)

        elif choice == "3":
            print("Thank you for using the financial calculator!")
            break

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
