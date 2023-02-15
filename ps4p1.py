#input phase
exam1 = float(input("Enter score for exam 1 :"))
exam2 = float(input("enter score for exam2 :"))
#process phase
score1 = exam1 * 0.6
score2 = exam2 * 0.4
grade = score1 + score2
#output phase
print("Your total score for the class is", grade)