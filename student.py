class student:
    studentID = 0
    fName = ""
    lName = ""
    status = ""

    termStart = ""
    termEnd = ""
    peopleSoftID = ""

    dob = ""
    phone = 0
    email = ""
    address = ""

    def __init__(self,id,fName,lName):
        self.studentID = id
        self.lName = lName
        self.fName = fName

    def __init__(self,id,fName,lName,status,termStart,termEnd,peopleSoft,dob,phone,address,email):
        self.studentID = id
        self.lName = lName
        self.fName = fName
        self.status = status
        self.termStart = termStart
        self.termEnd = termEnd
        self.peopleSoftID = peopleSoft
        self.dob = dob
        self.phone = phone
        self.address = address
        self.email = email
