p= float(input("Enter the the principal: $ "))
r=float(input("Enter the interest rate in decimal form: "))

for count in range (1, 6):
  i= p*r
  endingbal= p+i
  print(count, "    ", p, "   ", endingbal)

  p=endingbal