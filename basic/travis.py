known_user = ["Pramod","Santosh","Sushant","Kishor","Shital","Linda","Vijay"]
print(len(known_user))

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_user:
        print("Hello {}  your name has been recognised!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?").lower()
        if remove =='y':
            known_user.remove(name)
        elif remove=='n':
            print("No problem, I didn't want you to leave anyway!")
            
    else:
        print("Hmmm I don't think I have met you yet{}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?").strip().lower()
        if add_me =='y':
            known_user.append(name)
        elif add_me=='n':
            print("No worries, see you around!")
