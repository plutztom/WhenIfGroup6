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
            d = []
            for c in currentTerm:
              d.append({"Course":{'name':c.getName(),"tag":c.getTag(),"online":True}})
            data.append({self.terms[startQ]+", "+str(year):d})
            takenCourses += currentTerm
            courseOrder.append(currentTerm)
            courses = set(courses) - set(currentTerm)
            startQ += 1

        print("\n\nElective Courses: \n",self.program.info[self.program.getName()])
        data.append({"ElectiveInfo":self.program.info[self.program.getName()]})
        return json.dumps(data,sort_keys=True,indent =4)


if __name__ == "__main__":
    courses = loadCourses.load()
    computerScience = Program("Computer Science")
    g = programBuilder(2017,0,3,computerScience)
    print(g.planCourses())
