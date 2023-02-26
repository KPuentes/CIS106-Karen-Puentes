principle= int(input("Enter principle on CD:$"))
yearstomaturity= int(input("Enter the years to maturity:"))

if principle>100000 and yearstomaturity==5:
  interest=0.06
elif principle>50000 and principle<100000 and yearstomaturity==10:
  interest=0.05
elif principle>50000 and principle<100000 and yearstomaturity==5:
  interest=0.04
else:
  interest=0.02

firstyrint= principle*interest

print("The principle is:$", principle)
print("The interest in decimal is:", interest)
print("The total first year interest is:$", firstyrint)