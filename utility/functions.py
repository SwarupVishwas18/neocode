import pathlib
import textwrap
import google.generativeai as genai
import sys


user_data = "AIzaSyBAESdw0y1QQancJ7Bb9ICpc-rUxi2cHrY"
GOOGLE_API_KEY = user_data
genai.configure(api_key=GOOGLE_API_KEY)

print(sys.argv)


model = genai.GenerativeModel(
    model_name="gemini-pro",
)


def findAlgo(data):
    print("Taken")

    # model = genai.GenerativeModel("gemini-pro")
    print(model)
    prompt = data + " Give me Algorithm Name used in above code"
    print(prompt)
    try:
        response = model.generate_content(prompt, stream=False)
    except:
        return "Error Occured"
    str = ""
    for chuck in response:
        str += chuck.text

    print(str)

    return str


text = """
from logic import *
from normal import *

while True:
    printBrand("OS Scheduling Simulator")
    ch = myMenu(["FCFS", "SJF", "Priority", "About Me", "Exit"])
    proc = Processes()
    proc.takeProcesses()
    print("Processes That You've Entered..!!")
    proc.displayProcesses()
    # print("Our Solution..!!")
    # proc.fcfs()
    if ch == 1:
        proc.fcfs()
    if ch == 2:
        proc.sjf()
    if ch == 3:
        proc.priority()
    if ch == 4:
        aboutMe()
    if ch == 5:
        quitMe()
    # print(Fore.WHITE)
    # proc.displayProcesses()
"""

with open(sys.argv[1]) as f:
    text = f.read()
    print(findAlgo(text))
