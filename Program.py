import loadCourses
class Program:
    name = ""
    concentration = ""

    requiredClasses = []


    def __init__(self,name):
        self.name = name
        self.requiredClasses = {
            "Information Systems - Business Analysis/Systems Analysis": [loadCourses.getCourse("IS421"), loadCourses.getCourse("CSC451"), loadCourses.getCourse("IS422"), loadCourses.getCourse("IS430"), loadCourses.getCourse("CNS440"),
                                                                         loadCourses.getCourse("IS435"), loadCourses.getCourse("IS485"), loadCourses.getCourse("IS535"), loadCourses.getCourse("IS560")],
            "Information Systems - Business Intelligence": [loadCourses.getCourse("CSC401"),loadCourses.getCourse("IT403"), loadCourses.getCourse("IS421"), loadCourses.getCourse("CSC451"), loadCourses.getCourse("IS422"), loadCourses.getCourse("IS430"), loadCourses.getCourse("IS574"),loadCourses.getCourse("IS435"), loadCourses.getCourse("CSC423"),
                                 loadCourses.getCourse("CSC402"), loadCourses.getCourse("CSC403"), loadCourses.getCourse("IS467"), loadCourses.getCourse("IS549")],
            "Information Systems - DB Administration": [loadCourses.getCourse("CSC401"),loadCourses.getCourse("IS421"), loadCourses.getCourse("CSC451"), loadCourses.getCourse("IS422"), loadCourses.getCourse("IS430"),
                                                        loadCourses.getCourse("IS549"), loadCourses.getCourse("CSC454"), loadCourses.getCourse("CSC452"), loadCourses.getCourse("CSC554")],
            "Information Systems - IT Enterprise Management": [loadCourses.getCourse("IS421"), loadCourses.getCourse("CSC451"), loadCourses.getCourse("IS422"), loadCourses.getCourse("IS430"), loadCourses.getCourse("ECT424"), loadCourses.getCourse("IS556"),
                                                               loadCourses.getCourse("IS570"), loadCourses.getCourse("IS535")],
            "Information Systems - Standard": [loadCourses.getCourse("IS421"), loadCourses.getCourse("CSC451"), loadCourses.getCourse("IS422"), loadCourses.getCourse("IS430")],
            "Computer Science": [loadCourses.getCourse("CSC400"), loadCourses.getCourse("CSC401"),
                                 loadCourses.getCourse("CSC402"), loadCourses.getCourse("CSC403"),
                                 loadCourses.getCourse("CSC406"), loadCourses.getCourse("CSC407"),
                                 loadCourses.getCourse("CSC421"), loadCourses.getCourse("CSC435"),
                                 loadCourses.getCourse("CSC447"), loadCourses.getCourse("CSC453"),
                                 loadCourses.getCourse("SE450")]
        }


    def getCourses(self):
        return self.requiredClasses[self.name]

    def getName(self):
        return self.name