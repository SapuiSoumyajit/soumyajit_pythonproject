import pandas as pd
import csv
import json
##CREATING NEW STUDENT FILE.
def newStudentFile():
    ##creating a csv files with appropriate headers:
    with open("Student.csv","w") as obj:
        fobj=csv.writer(obj)
        fobj.writerow(['Student ID','Name','Class Roll Number','Batch Name'])
        ##creating student:
        while True:
            student_id=input("Enter the student id number")
            student_name=input("Enter the student's name")
            student_class_roll_no=int(input("Enter"+" "+student_name+"'s"+" "+"class roll number"))
            student_batch_name=input("Enter"+" "+student_name+"'s"+" "+"batch number")
            record=[student_id,student_name,student_class_roll_no,student_batch_name]
            fobj.writerow(record)
            ch=int(input("1->Enter More\n2->exit\nEnter your choice:"))
            if ch==2:
                break;
              

 ##ENTERING NEW STUDENT DATA.
def enternewstudent():
    with open("Student.csv","a") as obj:
        fobj=csv.writer(obj)
        while True:
            student_id=input("Enter the student id number")
            student_name=input("Enter the student's name")
            student_class_roll_no=int(input("Enter"+" "+student_name+"'s"+" "+"class roll number"))
            student_batch_name=input("Enter"+" "+student_name+"'s"+" "+"batch number")
            record=[student_id,student_name,student_class_roll_no,student_batch_name]
            fobj.writerow(record)
            ch=int(input("1->Enter More\n2->exit\nEnter your choice:"))
            if ch==2:
                break;

##UPDATING A STUDENT'S INFO:
def updatestudentdata():
    df=pd.read_csv('Student.csv')
    a=pd.DataFrame(df)
    entry=input("Enter the student name")
    for i,j in a.iterrows():
        if entry==j["Name"]:
            new_name=input("Enter the name to be updated to:")
            df.loc[i,'Name']=new_name
            df.to_csv("Student.csv", index=False)
            print(df)

##REMOVING A STUDENT DATA:
def remove_student():
    df=pd.read_csv('Student.csv')
    entry=input("Enter the student name to be deleted")
    for i,j in df.iterrows():
        df.drop(i,axis=0,inplace=True)
        df.to_csv("Student.csv",index=False)
        print(df)
        break;
 #Creating report card
 def reportCard(student_id):
    name = ""
    csv_reader= []
    with open("Student.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == student_id):
            check = 1
            name = csv_reader[i][1]
            break
    if(check == 0):
        print("Student ID does not exist")
        return
    f = open((student_id + ".txt"), "w")
    a = "Student ID: " + student_id + "\n"
    b = "Name: " + name + "\n"
    f.writelines([a, b])
    with open("Course.csv", "r", newline = "\n") as fx:
        csv_reader = list(csv.reader(fx, delimiter=","))
    marks = []
    subjects = []
    for i in range(1, len(csv_reader)):
        marks.append(json.loads(csv_reader[i][2]))
        subjects.append(csv_reader[i][1])
    total_marks = 0
    divs = 0
    for i in range(0, len(subjects)):
        temp = marks[i]
        if(isinstance(temp.get(student_id), int)):
            subject_marks = "Marks in " + subjects[i] + ": " + str(temp.get(student_id)) + "% \n"
            divs += 1
            total_marks += temp.get(student_id)
            f.write(subject_marks)
    grade = "Grade obtained: " + gradeCheck(total_marks/divs) + " \n"
    f.write(grade)
    f.close()

def gradeCheck(a):
    if(a >= 90):
        return "A"
    elif(a >= 80):
        return "B"
    elif(a >= 70):
        return "C"
    elif(a >= 60):
        return "D"
    elif(a >= 50):
        return "E"
    else:
        return "F"
