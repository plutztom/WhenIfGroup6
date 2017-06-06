import sqlite3
from Course import Course

courses = []
roughCourses = []

def load():
    conn = sqlite3.connect('classes2.db')
    c = conn.cursor()
    rough = []
    roughCourses = c.execute('''SELECT * FROM Courses2''')
    for r in roughCourses:
        rough.append(r)
        q = [0,1,2]
        if "Fall" in r[4]:
            q[0] = True
        else:
            q[0] = False
        if "Winter" in r[4]:
            q[1] = True
        else:
            q[1] = False
        if "Spring" in r[4]:
            q[2] = True
        else:
            q[2] = False

        c = Course(r[0], r[1], r[3], True, q, [])
        courses.append(c)

    for i in range(len(courses)):
        splitCourses = rough[i][2].split(" ")
        prereq = []
        for s in splitCourses:
            prereq.append(getCourse(s))
        courses[i].prereqs = prereq
    return courses


        


def getCourse(name):
    for c in courses:
        if name == c.getTag():
            return c


if __name__ == "__main__":
    load()

