noofemployees=0
sumofgrosspay=0
response= input("Would you like to calculate your gross pay?")

while response == "Yes":
  noofemployees=noofemployees+1
  lstnm= input("Enter last name:")
  hours= float(input("Enter hours worked:"))
  wage= float(input("Enter your hourly wage:"))
  if hours>= 40:
    grosspay = (wage*40)+((hours-40)*(wage*1.5))
  else:
    grosspay=wage*hours
  sumofgrosspay= sumofgrosspay+ grosspay
  print(lstnm, "Gross pay is $:", grosspay)
  response= input("Would you like to calculate your gross pay?")

  avggrosspay= sumofgrosspay/noofemployees
  print("The total sum of all gross pay is $:", sumofgrosspay)
  print("The total number of employees is:", noofemployees)
