f= open("ps8p3.txt", "r")
sumofbonus=0
c=0
lstnm=f.readline()
while lstnm != "":
  salary = float(f.readline())
  print()
  print("The employee's last name is: ", lstnm)
  print("The employee's salary is:$ ", format(float(salary),'10,.2f'))
  if salary>=100000:
      bonus=float(salary)*0.20
  elif salary>50000 and salary<100000:
      bonus=float(salary)*0.15
  else:
      bonus=float(salary)*0.10

  print("The employee's bonus is:$", format(bonus,'10,.2f'))
  sumofbonus=sumofbonus+bonus
  c=c+1
  lstnm=f.readline()
avg=sumofbonus/c
print("The average bonus is:$", avg)
format(float(avg),'10,.2f')

  
