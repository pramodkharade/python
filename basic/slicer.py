#get user email addresss
email = input("What is your email address?: ").strip()
#slice out user name
user = email[:email.index('@')]
#slice domain name
domainname = email[email.index('@')+1:]

#format message
output = "Your username is {} and your domain name is {}".format(user,domainname)
#display output message
print(output)
