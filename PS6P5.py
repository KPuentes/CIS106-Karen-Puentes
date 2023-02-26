lstnm = input("enter employee last name: ")
salary = float(input("Enter yearly salary:$"))
joblvl = int(input("Enter job level:"))

if joblvl==10 or joblvl>10:
  bonusrt=0.25
elif joblvl>4 and joblvl<10:
  bonusrt=0.20
else:
  bonusrt=0.10

bonus = salary*bonusrt

print("Employee:", lstnm)
print("Bonus:$", bonus)
