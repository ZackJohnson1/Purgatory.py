def main():
    '''This function gathers the input data necessary
    for the compound interest formula'''
# Getting input for Balance
    balance = float(input("Balance: $ "))
# Getting input for Interest Rate
    intRate = float(input("Interest Rate (%) : "))
# Getting input for Number of Years
    years = int(input("Years: "))
    newBalance = calcBalance(balance, intRate, years)

    print ("New balance:  $%.2f"  %(newBalance))

def calcBalance(bal, int, yrs):
    '''This function calculates the compound interest from
    the inputs in the above function'''
    newBal = bal
    for i in range(yrs):
        newBal = newBal + newBal * int/100
    return newBal

# Program run
main()