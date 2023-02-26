qty= int(input("Enter total tickets purchased:"))

if qty==25 or qty>25:
  priceperticket= 50
elif qty>10 and qty<24:
  priceperticket=60
elif qty>5 and qty<9:
  priceperticket=70
else:
  priceperticket=75

totalcost = qty * priceperticket
print("Total tickets bought:", qty)
print("Price per ticket:$", priceperticket)
print("Total cost:$", totalcost)
