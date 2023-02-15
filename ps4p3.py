#input phase
total = float(input("Enter the total:$"))
tippercent = float(input("Enter the percent you would like to tip:$"))
#process phase
tip = total * tippercent
totalwtip = total + tip
#output phase
print("Your total after tip comes out to be $", totalwtip)