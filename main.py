email = input("What is your email address?: ").strip()

username = email[:email.index("@")]

domain = email[email.index("@")+1:]

print(f" Your username is {username} and your domian name is {domain}")
