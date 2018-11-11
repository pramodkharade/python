def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return (total)



print(add(1,2,3,4,5,6,7,8,9))

def about(name,age,likes):
    sentence = "Meet {}! They are {} years old and they likes{}".format(name,age,likes)
    return sentence


dictionary = {"age":26,"name":"Pramod","likes":"Python"}

print(about(**dictionary))


def foo(**kwargs):
    for key,value in kwargs.items():
        print("{} : {}".format(key,value))


foo(pramod = "Male",deepika="Female")



