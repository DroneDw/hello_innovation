import os
from datetime import datetime

if not os.path.exists("gratitudes"):
    os.makedirs("gratitudes")

today = datetime.now().strftime("%d-%m-%y")
file = f"gratitudes/gratitude_{today}.txt"

greatful = input("whats one thing you are thanksful for today?")
difference = input("who made a difference in your day?")
moment = input("what is the best moment you want to remember?")

with open(file, "w") as new:
    new.write(f"greatful: {greatful}\n")
    new.write(f"defference: {difference}\n")
    new.write(f"moment: {moment}\n")