from Login import *
from ModuleManager import *
from datetime import date
MODULE_FILE = "Modules.txt"

def main():

    menu = ["Record Attendance", "Generate Statistics", "Exit"]

    login_status, name = checkLogin()

    if login_status == True:
        print("\nWelcome ", name)
        print("\nModule Record System - Options")
        print("---------------------------------")


        choice = ""

        while choice == "":
            for i in range(len(menu)):
                print(i + 1, ". ", menu[i])

            choice = input(">")

            if choice == "1":
                recordAttendance(name)

            elif choice == "2":
                generateStatistics(name)

            elif choice == "3":
                exit(-1)
            else:
                choice = ""
                print("Error! input out of range!\n")
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

    choice = int(input(">"))

    if 1 <= choice <= len(modules):
        module = modules[choice - 1]

        module_statistics = module.generate_statistics()
        print(module_statistics)
        module.save_statistics(module_statistics)
    else:
        print("Error! Input out of range!")



def recordAttendance(name):
    print("Module Record System(Attendance) - Choose a Module")
    print("---------------------------------------------------")
    moduleManager = ModuleManager(MODULE_FILE)

    modules = moduleManager.getModulesByLecturer(name)
    for i in range(len(modules)):
        print(i+1, ". ", modules[i].code)

    choice = int(input(">"))

    if 1 <= choice <= len(modules):
        module = modules[choice - 1]

        print("There are ", str(len(module.students)), " students enrolled.")
        for i in range(len(module.students)):
            student = module.students[i]

            user_input = ""
            while user_input == "":
                print("Student #", i + 1, " ", student.name)
                print("1. Present")
                print("2. Absent")
                print("3. Excused")

                user_input = int(input(">"))

                if user_input == 1:
                    student.present += 1
                elif user_input == 2:
                    student.absent += 1
                elif user_input == 3:
                    student.excused += 1
                else:
                    user_input = ""
                    print("Error! Input out of range!\n")

            if user_input != "":
                module.update()
    else:
        print("Error! Input out of range\n")


main()