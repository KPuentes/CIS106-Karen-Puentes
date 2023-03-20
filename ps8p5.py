f=open("ps8p5.txt","r")
c=0
totaltuition=0
lstnm=f.readline()
while lstnm !="":
  dstcode=f.readline()
  crdhrs=float(f.readline())

  if dstcode=="I":
    cph=250
  else:
    cph=500
  tuition=cph*crdhrs
  c=c+1
  totaltuition=totaltuition+tuition
  print("The sutdent's last name is:", lstnm)
  print("The amount of credit hours taken is:", crdhrs)
  print("The total tuition is: $", tuition)
  lstnm=f.readline()

print("The total number of students is: ", c)
print("The total tuition owed is: $", totaltuition)