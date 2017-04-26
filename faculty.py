class faculty:
    facultyID = 0
    peopleSoftID = 0
    fName = ""
    lName = ""
    job = ""

    def __init__(self,facultyID,fName,lName,peopleSoftID,job):
        self.facultyID = facultyID
        self.fName = fName
        self.lName = lName
        self.peopleSoftID = peopleSoftID
        self.job = job
