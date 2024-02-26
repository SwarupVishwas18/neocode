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
