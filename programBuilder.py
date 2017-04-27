from Course import Course
from Program import Program
import time

class programBuilder:
    terms = ["Fall","Winter","Spring"]
    startYear = 0
    coursesPerQuarter = 0;
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
        year = self.startYear
        startQ = self.startQuarter
        while len(courses) > 0:
            if startQ == 3:
                startQ = 0
                year += 1
            coursesLeft = self.coursesPerQuarter
            currentTerm = []
            print(self.terms[startQ], year,": ")
            for node in courses:
                if node.getTerms()[startQ] == True and coursesLeft > 0 and  all(j in takenCourses for j in node.getPrereqs()):
                    currentTerm.append(node)
                    coursesLeft -= 1
                    print(node.getTag(),": ",node.getName())
            takenCourses += currentTerm
            courses = list(set(courses) - set(currentTerm))
            startQ += 1




if __name__ == "__main__":
    CSC400 = Course("Discrete Structures for Computer Science", "CSC400", 41865, False,[True, True, True], [])
    CSC401 = Course("Introduction to Programming", "CSC401", 41988, False,[True, True, True], [])
    CSC402 = Course("Data Structures I", "CSC402", 41863, False,[True, True, True], [CSC401])
    CSC403 = Course("Data Structures II", "CSC403", 41932, False, [True, True, True], [CSC402])
    CSC406 = Course("Systems I", "CSC406", 41866, False, [True, True, True], [CSC401])
    CSC407 = Course("Systems II", "CSC407", 41930, False, [True, True, True], [CSC406, CSC402])
    CSC421 = Course("Applied Algorithms and Structures", "CSC421", 33381, False, [True, True, True], [CSC403, CSC400])
    CSC435 = Course("Distributed Systems I", "CSC435", 33386, False, [True, True, True], [CSC403, CSC407])
    CSC447 = Course("Concepts of Programming Languages", "CSC447", 33388, False, [True, True, True], [CSC403, CSC406])
    CSC453 = Course("Database Technologies", "CSC453", 33396, False, [True, True, True], [CSC403])
    SE450 = Course("Object-Oriented Software Development", "SE450", 33293, False, [True, True, True], [CSC403])

    computerScience = Program("Computer Science",[CSC400, CSC401, CSC402, CSC403, CSC406, CSC407, CSC421, CSC435, CSC447, CSC453, SE450],"Software Development")
    g = programBuilder(2017,0,3,computerScience)
    g.planCourses()