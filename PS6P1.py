qty = int(input("Enter quantity of widgets: "))

if qty > 1000:
  extprice = 10
elif qty >500 and qty<1000:
  extprice = 20
elif qty<500:
  extprice=30

tax=extprice*0.07
total=extprice+tax
print("Your price before tax is:$", extprice)
print("Your total tax is:$", tax)
print("Your total after tax is:$", total)