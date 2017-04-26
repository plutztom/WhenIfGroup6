class Program:
    name = ""
    courses = []

    def __init__(self,name,courses):
        self.name = name
        self.courses = courses

    def getCourses(self):
        return self.courses

    def getName(self):
        return self.name