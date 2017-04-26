from Course import Course
from Program import Program

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
                if node.getTerms()[startQ] == True and coursesLeft> 0 and all(i not in currentTerm for i in node.getPrereqs()) and all(j in takenCourses for j in node.getPrereqs()):
                    currentTerm.append(node)
                    takenCourses.append(node)
                    courses.remove(node)
                    coursesLeft -= 1
                    print(node.getTag(),": ",node.getName())
            startQ += 1




if __name__ == "__main__":
    CSC400 = Course("Discrete Structures for Computer Science", "CSC400", 41865, [True, True, True], False, [])
    CSC401 = Course("Introduction to Programming", "CSC401", 41988, [True, True, True], False, [])
    CSC402 = Course("Data Structures I", "CSC402", 41863, [True, True, True], False, [CSC401])
    CSC403 = Course("Data Structures II", "CSC403", 41932, [True, True, True], False, [CSC402])
    CSC406 = Course("Systems I", "CSC406", 41866, [True, True, True], False, [CSC401])
    CSC407 = Course("Systems II", "CSC407", 41930, [True, True, True], False, [CSC406, CSC402])
    CSC421 = Course("Applied Algorithms and Structures", "CSC421", 33381, [True, True, True], False, [CSC403, CSC400])
    CSC435 = Course("Distributed Systems I", "CSC435", 33386, [True, True, True], False, [CSC403, CSC407])
    CSC447 = Course("Concepts of Programming Languages", "CSC447", 33388, [True, True, True], False, [CSC403, CSC406])
    CSC453 = Course("Database Technologies", "CSC453", 33396, [True, True, True], False, [CSC403])
    SE450 = Course("Object-Oriented Software Development", "SE450", 33293, [True, True, True], False, [CSC403])


    computerScience = Program("Computer Science",[CSC400, CSC401, CSC402, CSC403, CSC406, CSC407, CSC421, CSC435, CSC447, CSC453, SE450])
    g = programBuilder(2017,0,3,computerScience)
    g.planCourses()
