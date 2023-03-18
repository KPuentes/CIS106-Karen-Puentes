response= input("Would you like to calculate your discounted total?")

while response == "Yes":
  price= float(input("Enter the unit price of items purchased $:"))
  qty= float(input("Enter the quantity of items purchased:"))
  extprice= qty * price
  if extprice> 10000:
    discamt = extprice*0.25
  else:
    discamt = extprice*0.10
  total= extprice-discamt
  print("Your original price was $", extprice, "Your amount discounted is $", discamt, "and your total comes out to be $", total)
  response= input("Would you like to calculate your discounted total?")