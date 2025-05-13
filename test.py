import datetime

name = input("What's your name? ")
now = datetime.datetime.now()

print(f"Hello, {name}!")
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
