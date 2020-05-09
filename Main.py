from Login import *
from ModuleManager import *

MODULE_FILE = "Modules.txt"

def main():

    menu = ["Record Attendance", "Generate Statistics", "Exit"]

    login_status, name = checkLogin()

    if login_status == True:
        print("\nWelcome ", name)
        print("\nModule Record System - Options")
        print("---------------------------------")

        for i in range(len(menu)):
            print(i+1, ". ", menu[i])

        choice = ""

        while choice == "":
            choice = input("")

            if choice == "1":
                pass
            elif choice == "2":
                generateStatistics(name)
                pass
            elif choice == "3":
                pass
            else:
                choice = ""
    else:
        print("Module Record System - Login Failed")
        exit(-1)

def generateStatistics(name):
    print("Module Record System(Statistics) - Choose a Module")
    print("---------------------------------------------------")
    moduleManager = ModuleManager(MODULE_FILE)

    modules = moduleManager.getModulesByLecturer(name)

    for i in range(len(modules)):
        print(i+1, ". ", modules[i].code)

    choice = int(input(""))

    if 1 <= choice <= len(modules):
        module = modules[choice - 1]
        print("Module: ", module.code)
        print("Number of students: ", len(module.students))
        print("Number of Classes: ", module.classes)
        print("Average Attendance: ", round(module.avg_attendance), " days")
        print("Low Attenders: under 70.0%")
        for student in module.low_attenders:
            print("\t", student.name)
        print("Non Attenders:")
        for student in module.non_attenders:
            print("\t", student.name)
        print("Best Attenders:")
        for student in module.best_attenders:
            print("\t", student.name)

main()