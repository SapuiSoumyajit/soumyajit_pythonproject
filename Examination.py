import csv
import json
import pandas
from matplotlib import pyplot
def newExamFile():
    ##creating a csv files with appropriate headers:
    with open("Exam.csv","w") as obj:
        fobj=csv.writer(obj)
        fobj.writerow(['Exam Name','Course Name','Student Roll Number','Marks Obtained'])
        
        while True:
            exam_name=input("Enter the exam")
            course_name=input("Enter the course name")
            stu_no=[]
            marks_ob=[]
            length=int(input("Enter the number of students:"))
            for i in range(0,length):
                student_id=input("Enter the student id:")
                marks=int(input("Enter the marks obtained:"))
                stu_no.append(student_id)
                marks_ob.append(stu_no)
                
                
            record=[exam_name,course_name,student_id,marks]
            fobj.writerow(record)
            ch=int(input("1->Enter More\n2->exit\nEnter your choice:"))
            if ch==2:
                break;
    def viewPerformanceE(course_id):
    csv_reader = []
    with open("Course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    student_marks = {}
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][1] == course_id):
            check = 1
            student_marks = json.loads(csv_reader[i][2])
            break
    if(check == 0):
        print("Course ID does not exist")
        return
    student_ids = list(student_marks.keys())
    for student in student_ids:
        marks = student_marks[student]
        print("Marks obtained by " + str(marks))

def scatterPlot():
    csv_reader = []
    with open("Course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    all_marks = []
    for i in range(1, len(csv_reader)):
        all_marks.append(json.loads(csv_reader[i][2]))
    batches = []
    students = []
    with open("Batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    for i in range(0, len(csv_reader)):
        batches.append(csv_reader[i][0])
        students.append(csv_reader[i][4].split(":"))
    for course in all_marks:
        batch_performances = []
        batchesX = []
        for i in range(0, len(batches)):
            total_marks = 0
            divs = 0
            check = 0
            for student in students[i]:
                if(student == students[i][0]):
                    if(not isinstance(course.get(student), int)):
                        check = 1
                        break
                total_marks += course.get(student)
                divs += 1
            if(check == 1):
                continue
            else:
                batchesX.append(batches[i])
                batch_performances.append(total_marks/divs)
        pyplot.scatter(batchesX, batch_performances)
    pyplot.show()
