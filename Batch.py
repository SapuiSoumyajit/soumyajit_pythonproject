import csv
import pandas
import json
from matplotlib import pyplot
from department import createDepartment

##Creating new batch file:
def newBatchFile():
    ##creating a csv files with appropriate headers:
    with open("Batch.csv","w") as obj:
        fobj=csv.writer(obj)
        fobj.writerow(['Batch ID','Batch Name','Department Name','List of courses''List of Students'])
        while True:
            batch_id=input("Enter the Batch id number")
            batch_name=input("Enter the Batch name")
            dept_name=input("Enter the department name")
            course_lst=[]
            len=int(input("Enter the number of courses"))
            for i in range(0,len):
                course_name=input("Enter the course name")
                course_lst.append(course_name)
            print(course_lst)
            stu_lst=[]
            stu_len=int(input("Enter the number of students"))
            for i1 in range(0,stu_len):
                stu_name=input("Enter the student name")
                stu_lst.append(stu_name)
            print(stu_lst)
            record=[batch_id,batch_name,dept_name,course_lst,stu_lst]
            fobj.writerow(record)
            ch=int(input("1->Enter More\n2->exit\nEnter your choice:"))
            if ch==2:
                break;
def pieChart(batch_id):
    with open("Course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    students = []
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == batch_id):
            check = 1
            students = csv_reader[i][4].split(":")
            break
    if(check == 0):
        print("Batch ID does not exist")
        return
    percentages = [">=90", ">=80", ">=70", ">=60", ">=50", "Failed"]
    numbers = [0, 0, 0, 0, 0, 0]
    for student in students:
        with open("./db/course.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        all_marks = []
        for i in range(1, len(csv_reader)):
            all_marks.append(json.loads(csv_reader[i][2]))
        total_marks = 0
        divs = 0
        for subjects in all_marks:
            if(isinstance(subjects.get(student), int)):
                total_marks += subjects.get(student)
                divs += 1
        percentage = total_marks/divs
        if(percentage >= 90):
            numbers[0] += 1
        elif(percentage >= 80):
            numbers[1] += 1
        elif(percentage >= 70):
            numbers[2] += 1
        elif(percentage >= 60):
            numbers[3] += 1
        elif(percentage >= 50):
            numbers[4] += 1
        else:
            numbers[5] += 1
    for i in range(len(numbers) - 1, -1, -1):
        if(numbers[i] == 0):
            del numbers[i]
            del percentages[i]
    pyplot.pie(numbers, labels = percentages)
    pyplot.show()
                
##List of students in the batch:
def student_batch_list():
    df=pd.read_csv('Batch.csv')
    a=pd.DataFrame(df)
    
    cname=input("Enter batch name:")
    for i,j in a.iterrows():
        if cname==j['Batch Name']:
            print(j['List of Students'])

##LIST of all courses in a batch:
def course_batch_list():
    df=pd.read_csv('Batch.csv')
    a=pd.DataFrame(df)
    
    cname=input("Enter batch name:")
    for i,j in a.iterrows():
        if cname==j['Batch Name']:
            print(j['List of courses'])
