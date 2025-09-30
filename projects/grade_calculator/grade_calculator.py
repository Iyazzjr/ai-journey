engl = int(input("enter english test score: "))
phy = int(input("enter physics test score: "))
chm = int(input("enter chemistry test score: "))
grades = [engl, phy, chm]
sum = engl + phy + chm
num = len(grades)
average = sum/num
if average >= 80:
    print("excellent")
elif 50<= average <80:
    print("good")
elif average < 50:
    print("needs improvement")
