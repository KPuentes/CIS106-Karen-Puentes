#input phase
pricepershare = float(input("Enter the price per share when purchased: $"))
currentprice = float(input("Enter the current price per share: $"))
quantity = float(input("Enter amount of shares purchased:"))
#process phase
valuechange = currentprice - pricepershare
#output phase
print("Your total profit/loss is:$", valuechange)
