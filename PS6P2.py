partno=int(input("Enter the part number:"))
qty=input("Enter the quanity to purchase:")

if partno==10 or partno==55:
  unitprice=1
elif partno==90:
  unitprice=2
elif partno==70 or partno==80:
  unitprice=3
else:
  unitprice=5

total= float(qty)*unitprice

print("Part number:", partno)
print("Unit price: $", unitprice)
print("Total:$", total)
