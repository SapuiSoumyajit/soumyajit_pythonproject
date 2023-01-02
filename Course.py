import json
import csv
import pandas
import matplotlib.pyplot
def newCourseFile():
    with open("Course.csv","w") as obj:
        fobj=csv.writer(obj)
        fobj.writerow(['Course ID','Course Name','Marks Obtained'])
        ##creating course:
        while True:
            course_id=input("Enter the course id number")
            course_name=input("Enter the course name")
            marks_obtained={}
            length=int(input("Enter the number of students:"))
            while len(marks_obtained)<length:
                student_id=input("Enter the student id:")
                marks=int(input("Enter marks:"))
                marks_obtained[student_id]=marks
                print(marks_obtained)
                
            record=[course_id,course_name,marks_obtained]
            fobj.writerow(record)
            ch=int(input("1->Enter More\n2->exit\nEnter your choice:"))
            if ch==2:
                break;

##View performance of all students in the course.
def course_perf():
    df=pd.read_csv('Course.csv')
    a=pd.DataFrame(df)
    
    cname=input("Enter course name:")
    for i,j in a.iterrows():
        if cname==j['Course Name']:
            print(j['Marks Obtained'])
#View Course statistics:
def courseStatistics(course_id):
    csv_reader = []
    with open("Course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == course_id):
            check = 1
            break
    if(check == 0):
        print("Course ID does not exist")
        return
    x = checkPerformance(course_id)
    grades = []
    for a in x:
        grades.append(gradeCheck(a[3]))
    grades.sort()
    letter_counts = Counter(grades)
    df = pandas.DataFrame.from_dict(letter_counts, orient='index')
    df.plot(kind='bar')
    matplotlib.pyplot.show()
