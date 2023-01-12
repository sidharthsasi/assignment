import math
print("It Must be 9 digit")
id=(input("Enter your student id"))
car=int(input("enter train car"))
print(type(id))
ids=slice(3,10)
a=int(id[ids])
print(a)
print(type(a))
d=a/100
print(d)
r=d/2
print(r)
total_volume = 3.14*(r*2)*50
print("total_volume :",total_volume)



volume2=30100*3.79*car
print(volume2)

h=volume2/(3.14*(r*2))
print("height:",h)


no_of_train = total_volume/volume2
print("no_of_train:",no_of_train)

