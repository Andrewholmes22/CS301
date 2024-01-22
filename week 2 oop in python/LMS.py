import datetime


class user():
    def __init__(self, name, DOB,number, email,iD):
        self.name=name
        self.DOB=datetime.datetime.strptime(DOB,'%m/%d/%Y')
        self.email=email
        self.number=number
        self.iD=iD
    def getinfo(self):
        print("name:"+self.name)
        print("DOB: " + self.DOB.strftime('%m/%d/%Y'))
        print("Phone number:"+self.number)
        print("email:"+self.email)
        print("ID:"+self.iD)
andrew=user("andrew","04/14/1998","9708675309","andrew@gmail.com", "310031831")
kevin=user("kevin","04/14/1998","9708675309","kevin@gmail.com", "310031831")
students = [Student("Andrew"), Student("Kevin")]
andrew.getinfo()

def Course():
    def __init__(self,name,code,dept,complete,instructor,semester,Enrolled_Students ):
        self.name=name
        self.code=code
        self.dept=dept
        self.complete=complete  
        self.instructor=instructor
        self.semester=semester
        self.Enrolled_Students=Enrolled_Students
    def getStudents(self):
        print("Enrolled Students:"+self.Enrolled_Students)
        for student in self.Enrolled_Students:
            print(student)
    def addStudent(self,student):
        self.Enrolled_Students.append(student)
        return True
    def removeStudent(self,student):
        self.Enrolled_Students.remove(student)
        return True
    def setInstructor(self,instructor):
        self.instructor=instructor
        return True
    def printInfo(self):
        print("name:"+self.name)
        print("code:"+self.code)
        print("dept:"+self.dept)
        print("complete:"+self.complete)
        print("instructor:"+self.instructor)
        print("semester:"+self.semester)
        getStudents()
course1=Course("CS","CS101","Computer Science","false","Dr. Smith","Fall 2019",students)
course1.printInfo()