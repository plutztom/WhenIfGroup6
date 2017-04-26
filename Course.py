class Course:
    name = ""
    tag = ""
    peoplesoft = 0
    quarters = []
    dormant = False
    prereqs = []

    def __init__(self,name,tag,peoplesoft,quarters,dormant,prereqs):
        self.name = name
        self.tag = tag
        self.peoplesoft = peoplesoft
        self.quarters = quarters
        self.dormant = dormant
        self.prereqs = prereqs

    def getName(self):
        return self.name

    def getTag(self):
        return self.tag

    def getPrereqs(self):
        return self.prereqs

    def getTerms(self):
        return self.quarters




