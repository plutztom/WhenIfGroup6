from Program import Program
from programBuilder import programBuilder
import loadCourses
import sqlite3
import sys

if __name__ == "__main__":
    name = input("Enter your username: ")
    pss = input("Enter your password: ")
    print("login successful")
    while (True):
        print("input 'run' to search or 'quit' to quit")
        inpt = input('>')

        if inpt == 'run':
            courses = loadCourses.load()
            pgm = Program("Computer Science")
            g = programBuilder(2017,0,3,pgm)
            g.planCourses()
        elif inpt == "quit" or "Quit":
            sys.exit()

        else:
            print("Invalid Login")

        

    

    
