f=open("ps8p4.txt", "r")
c=0
ttlextp=0
item= str(f.readline().rstrip('\n'))
while item!="":
  qty=float(f.readline())
  price=float(f.readline())
  extp= qty*price
  ttlextp=ttlextp+extp
  c=c+1
  
  print("The item is : ", item)
  print("The quantity is : ", qty)
  print("The price is : $", price)
  print("The extended price is : $", extp)

  item=str(f.readline().rstrip('\n'))

print("The sum of all extended prices are: $", ttlextp)
print("The total number of orders is: ", c)
avg=ttlextp/c
print("The average cost per order is :$", avg)

