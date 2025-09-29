person = {"name" : "iyazz",
          "age" : "22",
          "class" : "400"
          }
print(person["age"])
person["country"] = "United states"

person["age"] = 24
person.pop("class")
print(person)
for key, value in person.items():
    print(key, ":", value)
   
student ={"name" : "iyazz",
          "age" : "23",
          "scores" : {"math" : 94,
                      "biology" : 87}}
print(student["scores"]["biology"])

numbers = [1,2,3,4,5]
count = 0
sum = 0
for i in numbers:
    count = count +i
    sum = count
print(sum)

me = {"name" : "iyazz", 
      "age" : 23,
      "field" : "engineering"}
print([me])
for key, value in me.items():
    print(key, ":", value)

time = int(input("what is your age:"))
if 66 > time >= 20:
    print("you are an adult")
elif 19>= time > 12:
    print("you are a teenager")
elif 117 > time >= 65:
    print("you are a senior")
else:
    print("invalid age")

n = 2
while n <= 20:
    print(n)
    n += 2

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

x = 1
while x <= 10:
    print(x)
    x += 1

