counter=0
totalex=0
response=input("Would you like to calculate your exam score average? Enter Yes or No.:")

while response=="Yes":
  counter= counter+1
  lstnm= input("Enter student's last name:")
  score1=float(input("Enter the first exam's score"))
  score2= float(input("Enter the second exam's score:"))
  avgscr= (score1 + score2)/2
  print(lstnm, ":")
  print("Average test score is", avgscr)
  totalex= totalex+score1
  response=input("Would you like to calculate your exam score average? Enter Yes or No.")

avgex= totalex/counter
print("Total number of students is:",counter )
print("For exam 1, the average test score is:",avgex)
