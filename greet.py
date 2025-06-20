import datetime

#def greet(name):
#    return f"Hello, {name}! Welcome to GitHub." #modification

#if __name__ == "__main__":
#    user = input("Enter your name:")
#    print(greet(user)) 

def greet(name):
    now = datetime.datetime.now()   #used to assign the current time to the now variable
    return f"Hello, {name}! Current time is {now:%Y-%m-%d%H:%M:%S}"

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))