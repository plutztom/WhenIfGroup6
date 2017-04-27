class Program:
    name = ""
    courses = []
    concentration = ""

    def __init__(self,name,courses,concentration):
        self.name = name
        self.courses = courses
        self.concentraton = concentration

    def getCourses(self):
        return self.courses

    def getName(self):
        return self.name