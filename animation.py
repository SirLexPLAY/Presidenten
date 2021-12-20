import time
import os
clear = lambda: os.system('clear')
clear()

def animation():

    speed = 0.01

    print("\n")
    lines = [
    "██████╗░██████╗░███████╗░██████╗██╗██████╗░███████╗███╗░░██╗████████╗███████╗███╗░░██╗",
    "██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔════╝████╗░██║",
    "██████╔╝██████╔╝█████╗░░╚█████╗░██║██║░░██║█████╗░░██╔██╗██║░░░██║░░░█████╗░░██╔██╗██║",
    "██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗██║██║░░██║██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░██║╚████║",
    "██║░░░░░██║░░██║███████╗██████╔╝██║██████╔╝███████╗██║░╚███║░░░██║░░░███████╗██║░╚███║",
    "╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝"
    ]

    for line in lines:
        time.sleep(speed)
        print("   ", end="")
        print(line)

    clear()
    for i in range(len(lines)):
        print("\n")
        j = 0
        for line in lines:
            if j == i:
                print("    ", end="")
                print(line)
            else:
                print("   ", end="")
                print(line)
            j += 1
        time.sleep(speed)
        clear()

    for i in range(len(lines)):
        print("\n")
        j = 0
        for line in lines:
            if j == i:
                print("  ", end="")
                print(line)
            else:
                print("   ", end="")
                print(line)
            j += 1
        time.sleep(speed)
        clear()

    print("\n")
    for line in lines:
        print("   ", end="")
        print(line)






    print("\n")
