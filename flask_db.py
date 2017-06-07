import sqlite3 as sql, loadCourses
from programBuilder import programBuilder
from flask import Flask, request
from Program import Program
app = Flask(__name__)

@app.route('/user/<username>',methods = ['POST', 'GET'])
def get_user():
    if request.method == 'POST':
        try:
           name = request.form['FullName']
           user = request.form['username']
           depaul = request.form['DePaulID']
           dob = request.form['dateofbirth']
           email = request.form['email']
           phone = request.form['phone']
           major = request.form['major']
            with sql.connect('classes2.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Users(FullName,username,DePaulID,dateofbirth,email,phone,major) VALUES (?,?,?,?,?,?,?)",
                (name,user,depaul,dob,email,phone,major) )

                con.commit()
            except:
                con.rollback()

            finally:
                con.close()
        
@app.route('/program', methods = ['POST', 'GET'])
def get_program(username):
    con = sql.connect('classes2.db')
    cur = con.cursor()
    cur.execute("SELECT major FROM Users WHERE username = ?", username)
    user = cur.fetchone();
    #have the user, now build their program
    courses = loadCourses.load()


    if user = "Computer Science":
        CS = Program("Computer Science")
        csBuild = programBuilder(2017,0,3,CS)
        return csBuild.planCourses()
    
    elif user = "Information Systems - Standard":
        IS0 = Program("Information Systems - Standard")
        is0Build = programBuilder(2017,0,3,IS0)
        return is0Build.planCourses()

    elif user = "Information Systems - Business Analysis/Systems Analysis":
        IS1 = Program("Information Systems - Business Analysis/Systems Analysis")
        is1Build = programBuilder(2017,0,3,IS1)
        return is1Build.planCourses()

    elif user = "Information Systems - Business Intelligence":
        IS2 = Program("Information Systems - Business Intelligence")
        is2Build = programBuilder(2017,0,3,IS2)
        return is2Build.planCourses()

    elif user = "Information Systems - DB Administration":
        IS3 = Program("Information Systems - DB Administration")
        is3Build = programBuilder(2017,0,3,IS3)
        return is3Build.planCourses()
        
    elif user = "Information Systems - IT Enterprise Management":
        IS4 = Program("Information Systems - IT Enterprise Management")
        is4Build = programBuilder(2017,0,3,IS4)
        return is4Build.planCourses()

if __name__ == '__main__':
    app.run()


    
