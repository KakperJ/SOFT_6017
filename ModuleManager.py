from datetime import date
import os

class ModuleManager:

    def __init__(self, module_file):
        self.modules = []

        #create file if it doesn't exist :)
        if not os.path.exists(module_file):
            with open(module_file, 'w+') as file:
                pass


        with open(module_file, 'r') as file:
            for row in file:
                module_details = row.split(",")
                module = Module(module_details[0], module_details[1], module_details[2].replace("\n", ""))
                self.modules.append(module)




    #Gets the modules
    def getModulesByLecturer(self, lecturer):
        list = []
        for module in self.modules:
            if module.lecturer == lecturer:
                list.append(module)
        return list

#this is a module
#Holds all info about modules
class Module:

    def __init__(self, code, name, lecturer):
        self.code = code
        self.name = name
        self.lecturer = lecturer
        self.students = []

        #create file if it doesn't exist :)
        if not os.path.exists(code + ".txt"):
            with open(code + ".txt", 'w+') as file:
                pass


        #Adds students to the module
        with open(code + ".txt", 'r+') as f:
            for row in f:
                student_details = row.split(",")
                student = Student(student_details[0], student_details[1], student_details[2], student_details[3].replace("\n", ""))
                self.students.append(student)

        if len(self.students) > 0:
            student = self.students[0]
            self.classes = student.present + student.absent + student.excused
        else:
            self.classes = 0

    #get attendance for best, low, and non attenders
    def getAttendance(self):
        best_attenders = []
        low_attenders = []
        non_attenders = []

        avg = 0
        best = 0

        # Calculate best, low and non attenders
        for student in self.students:
            avg += student.present

            # Add best students to list
            if student.present > best:
                best_attenders = []
                best = student.present
            if student.present == best:
                best_attenders.append(student)

            # Non attenders if they've never been present
            if student.present == 0:
                non_attenders.append(student)

            # Low attenders if they've been present less than 70%
            if (student.present / self.classes) < 0.7:
                low_attenders.append(student)

        # Calculate average attendance
        avg_attendance = avg / len(self.students)

        return avg_attendance, best_attenders, low_attenders, non_attenders


    #updates the module information to a file
    def update(self):
        with open(self.code + ".txt", 'w+') as file:
            for student in self.students:
                file.write(student.name + "," + str(student.present) + "," + str(student.absent) + "," + str(student.excused) + "\n")

        print(self.code + ".txt updated with latest attendance records")

    #Writes the module statistics to a file
    def save_statistics(self, module_statistics):
        with open(self.code + "_" + str(date.today()), 'w+') as f:
            f.write(module_statistics)

    #Generates the statistics for the module
    def generate_statistics(self):
        avg_attendance, best_attenders, low_attenders, non_attenders = self.getAttendance()

        module_statistics = ""

        module_statistics += "Module: " + self.code + "\n"
        module_statistics += "Number of students: " + str(len(self.students)) + "\n"
        module_statistics += "Number of Classes: " + str(self.classes) + "\n"
        module_statistics += "Average Attendance: " +  str(round(avg_attendance)) +  " days\n"
        module_statistics += "Low Attenders: under 70.0%\n"


        for student in low_attenders:
            module_statistics += "\t" + student.name + "\n"

        module_statistics += "Non Attenders:\n"
        for student in non_attenders:
            module_statistics += "\t" +  student.name + "\n"

        module_statistics += "Best Attenders:\n"
        for student in best_attenders:
            module_statistics += "\t" + student.name + "\n"

        return module_statistics

#Holds information on students
class Student:

    def __init__(self, name, days_present, days_absent, days_excused):
        self.name = name
        self.present = int(days_present)
        self.absent = int(days_absent)
        self.excused = int(days_excused)