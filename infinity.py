import os
import sys
import time as t
import pyfiglet

clear = os.system("clear")

#InfinityModuleArt -BANNER


banner = pyfiglet.figlet_format(" InfinityTools!")
print( banner)
print("\033[92m                 ---@TheUnqualifiedDev")


#List of tools
print("\n\n")
print("\033[94m -DECIDE THE TOOLS TO INSTALL ! RUN INFINITYTOOLS WITH SU PERMISSION- \n")

print(" \033[91m  [01]  \033[93m Update Packages")
print("  \033[91m [02] \033[93m  Upgrade Packages")
print(" \033[91m  [03]  \033[93m Install Git")
print("  \033[91m [04]  \033[93m Install Wget")
print("  \033[91m [05]  \033[93m Install Crunch")
print("  \033[91m [06]  \033[93m Install Aircrack")
print(" \033[91m  [07]  \033[93m Handshake 2 Password Cracker")
print(" \033[91m  [08]  \033[93m Install Hydra")
print("\n \033[91m  [99]  \033[93m Exit ")


print("\n\n")
def execute():
    num= input("  \033[92m@\033[93minfinitytools:  ")
    print("\n \033[94m")
    workdone(num)

def workdone(num):
    if num == "1" or num == "01":
        task = os.system(" apt-get update")
    
    if num == "99" :
        print("  \033[91m Exiting the tool. Thanks for using \033[94m @ The unqualified dev \n ")
        t.sleep(2)
        exit()

    if num == "2" or num == "02":
        task = os.system(" apt-get upgrade")

    if num == "3" or num == "03":
        task = os.system(" apt-get install git")

    if num == "4" or num == "04":
        task = os.system(" apt-get install wget")

    if num == "5" or num == "05":
        task = os.system(" apt-get install crunch")

    if num == "6" or num == "06":
        task = os.system(" apt-get install aircrack-ng")
    
    if num == "8" or num == "08":
        task = os.system(" apt-get install hydra")
    else:
        print("No such tools found ! Try again <3 ")
    
    
    
    print("")
    execute()
    



   




execute()





