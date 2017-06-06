class Course:
    name = ""
    tag = ""
    peoplesoft = 0
    quarters = []
    dormant = False
    prereqs = []
    online = True

    def __init__(self,name,tag,peoplesoft,online,quarters,prereqs):
        self.name = name
        self.tag = tag
        self.peoplesoft = peoplesoft
        self.quarters = quarters
        self.prereqs = prereqs
        self.online = online

    def getName(self):
        return self.name

    def getTag(self):
        return self.tag

    def getPrereqs(self):
        return self.prereqs\


    def getTerms(self):
        return self.quarters




