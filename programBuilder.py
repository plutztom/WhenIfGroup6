import json
import loadCourses
from Program import Program


class programBuilder:
    terms = ["Fall","Winter","Spring"]
    startYear = 0
    coursesPerQuarter = 0
    program = ""
    startQuarter = ""
    
    def __init__(self,startYear,startQuarter,coursesPerQuarter,program):
        self.startYear = startYear
        self.coursesPerQuarter = coursesPerQuarter
        self.program = program
        self.startQuarter = startQuarter
    
    def planCourses(self):
        courses = self.program.getCourses()
        takenCourses = []
        courseOrder = []
        data = []
        year = self.startYear
        startQ = self.startQuarter
        while len(courses) > 0:
            if startQ == 3:
                startQ = 0
                year += 1
            coursesLeft = self.coursesPerQuarter
            currentTerm = []
            print(self.terms[startQ], year, ": ")
            for node in courses:
                if node.getTerms()[startQ] == True and coursesLeft > 0 and (all(
                                j in takenCourses for j in node.getPrereqs()) or node.getPrereqs() == [None]):
                    currentTerm.append(node)
                    coursesLeft -= 1
                    print(node.getTag(), ": ", node.getName())
            takenCourses += currentTerm
            courseOrder.append(currentTerm)
            courses = set(courses) - set(currentTerm)
            startQ += 1

        return courseOrder


if __name__ == "__main__":
    courses = loadCourses.load()
    computerScience = Program("Information Systems - Business Analysis/Systems Analysis")
    g = programBuilder(2017,0,3,computerScience)
    g.planCourses()