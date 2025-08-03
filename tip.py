def amount(x):
    return float(x.replace("$"," "))
def percentage(y):
    return float(y.replace("%"," "))/100
def main():
    amt=amount(input("Enter the amount"))
    percent=percentage(input("What percent would you like to tip"))
    tip=amt*percent
    print (f"Pay tip:${tip:.2f}")
main()
