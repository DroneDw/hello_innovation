import os
from datetime import datetime

if not os.path.exists("logs"):
    os.makedirs("logs")

today = datetime.now().strftime("%y-%m-%d")
fileName = f"logs/log_{today}.txt"


print("ANSWER THE FOLLOWING")

# 🧠 Ask daily log questions
print("Welcome to your Daily Log!")

energy = input("⚡ How's your energy today (1–10)? ")
lesson = input("📘 What did you learn today? ")
idea = input("💡 Any idea you had today? ")# 📝 Write responses to today's log file
with open(filename, "w") as file:
    file.write(f"🗓️ Date: {today}\n")
    file.write(f"⚡ Energy: {energy}\n")
    file.write(f"📘 Learned: {lesson}\n")
    file.write(f"💡 Idea: {idea}\n")
