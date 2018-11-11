#number = 1
#while number <=10:
    #if number % 2==0:
      #print("EVEN",number)
   # else:
         #print("ODD ",number)
    #number = number + 1

l=[]
while len(l)<= 3:
    new_name = input("Please add a new name?: ").strip().capitalize()
    l.append(new_name)
print(l)
print("{} sorry list is full".format(new_name))
print(new_name)
