class ModuleManager:

    def __init__(self, module_file):
        self.modules = []

        with open(module_file, 'r') as file:
            for row in file:
                module_details = row.split(",")
                module = Module(module_details[0], module_details[1], module_details[2].replace("\n", ""))
                self.modules.append(module)


    def getModulesByLecturer(self, lecturer):
        list = []
        for module in self.modules:
            if module.lecturer == lecturer:
                list.append(module)
        return list


class Module:

    def __init__(self, code, name, lecturer):
        self.code = code
        self.name = name
        self.lecturer = lecturer
        self.students = []

        with open(code + ".txt", 'r') as f:
            for row in f:
                student_details = row.split(",")
                student = Student(student_details[0], student_details[1], student_details[2], student_details[3].replace("\n", ""))
                self.students.append(student)

        if len(self.students) > 0:
            student = self.students[0]
            self.classes = student.present + student.absent + student.excused
        else:
            self.classes = 0

        self.best_attenders = []

        avg = 0
        best = 0
        for student in self.students:
            avg += student.present

        self.avg_attendance = avg / len(self.students)


    def getAverageAttendance(self):
        avg = 0
        for student in self.students:
            pass


class Student:

    def __init__(self, name, days_present, days_absent, days_excused):
        self.name = name
        self.present = int(days_present)
        self.absent = int(days_absent)
        self.excused = int(days_excused)