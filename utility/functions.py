import pathlib
import textwrap
import google.generativeai as genai


user_data = "AIzaSyBAESdw0y1QQancJ7Bb9ICpc-rUxi2cHrY"
GOOGLE_API_KEY = user_data
genai.configure(api_key=GOOGLE_API_KEY)
config = {"temperature": 0, "top_k": 20, "top_p": 0.9, "max_output_tokens": 500}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=config,
    safety_settings=safety_settings,
)


def findAlgo(data):
    print("Taken")

    # model = genai.GenerativeModel("gemini-pro")
    print(model)
    prompt = data + " Give me Algorithm Name used in above code"
    print(prompt)
    response = model.generate_content(prompt, stream=False)
    str = ""
    for chuck in response:
        str += chuck.text

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

print(findAlgo(text))
