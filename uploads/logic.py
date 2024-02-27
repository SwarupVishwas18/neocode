import operator
from colorama import Fore

class Processes:
    def __init__(self) -> None:
        self.processes = []
        

    def takeProcesses(self):
        print(Fore.CYAN)
        num = int(input("Enter the number of Processes you want to add : "))

        for i in range(num):
            print("-"*20)
            print(f"Process {i+1}".center(20))
            print("-"*20)
            at = int(input("Enter th Arrival Time : "))
            bt = int(input("Enter the burst time :"))
            pt = int(input("Enter the priority of the process : "))
            self.processes.append({"id": i+1,"at":at, "bt": bt, "pt":pt})
        
        self.processes = sorted(self.processes, key=lambda i: i['at'])
    
    def displayProcesses(self):
        i = 0
        for process in self.processes:
            # print(process)
            print(Fore.YELLOW)
            print("-"*20)
            print(f"Process {i+1}".center(20))
            print("-"*20)
            for k, v in process.items():
                print(k ," : ", v)
            i+=1
    
    def fcfs(self):
        ft = 0
        sumtt = 0
        sumwt = 0
        # i = 0
        # ft += self.processes[0]['at']
        for process in self.processes:
            if ft < process['at']:
                ft += (process['at']-ft)
            ft += process['bt']
            print()
            process['ft'] = ft
            process['tt'] = process['ft'] - process['at']
            process['wt'] = process['tt'] - process['bt']

            sumtt += process['tt']
            sumwt += process['wt']

        print(Fore.LIGHTGREEN_EX)
        print("Average Turn Around Time : ",sumtt/(len(self.processes)))
        print("Average Waiting Time : ",sumwt/(len(self.processes)))
        self.displayProcesses()

    def sjf(self):
        ft = 0
        sumtt = 0
        sumwt = 0

        # self.processes = sorted(self.processes, key=operator.itemgetter('at'))
        self.processes = sorted(self.processes, key=lambda i: i['bt'])

        for process in self.processes:
            ft += process['bt']
            print()
            process['ft'] = ft
            process['tt'] = process['ft'] - process['at']
            process['wt'] = process['tt'] - process['bt']

            sumtt += process['tt']
            sumwt += process['wt']

        print(Fore.LIGHTGREEN_EX)
        print("Average Turn Around Time : ",sumtt/(len(self.processes)))
        print("Average Waiting Time : ",sumwt/(len(self.processes)))
        self.displayProcesses()

    def priority(self):
        ft = 0
        sumtt = 0
        sumwt = 0

        self.processes = sorted(self.processes, key=operator.itemgetter('at', 'pt'))

        for process in self.processes:
            ft += process['bt']
            print()
            process['ft'] = ft
            process['tt'] = process['ft'] - process['at']
            process['wt'] = process['tt'] - process['bt']

            sumtt += process['tt']
            sumwt += process['wt']

        print(Fore.LIGHTGREEN_EX)
        print("Average Turn Around Time : ",sumtt/(len(self.processes)))
        print("Average Waiting Time : ",sumwt/(len(self.processes)))
        self.displayProcesses()

