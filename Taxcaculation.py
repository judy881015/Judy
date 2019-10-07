#TaxCalculation

status=input("Enter your filing status(single/married):")
tax=input("Enter your taxable income:")
tax=float(tax)
if status == "single":
    if 21450.00>=tax>=0.00:
        print("your tax is 15%:",tax*0.15)
    elif 51900>=tax>21450:
        print("your tax is 3217.5+tax28%:",3217.5+(tax-21450)*0.28)
    elif tax>51900:
        print("your tax is 19566.00+31%:",19566.00+(tax-51900)*0.31)
    else:
        print("Please enter the correct income!")
elif status == "married":
    if 35800.00>=tax>=0.00:
        print("your tax is 15%:",tax*0.15)
    elif 86500>=tax>35800:
        print("your tax is 5370.00+28%:",5370.00+(tax-35800)*0.28)
    elif tax>86500:
        print("19566.00+31%:",19566.00+(tax-86500)*0.31)
    else:
        print("Please enteer the correct income!")
else:
    print("Please enter the correct status!")
