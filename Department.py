import json
import csv
from matplotlib import pyplot
##Create new department file:
def newDepartmentFile():
    ##creating a csv files with appropriate headers:
    with open("Department1.csv","a") as obj:
        fobj=csv.writer(obj)
        ##fobj.writerow(['Department ID','Department Name','List of batches'])
        while True:
            dept_id=input("Enter the department id number")
            dept_name=input("Enter the department name")
            batch_lst=[]
            len=int(input("Enter the number of batch"))
            for i in range(0,len):
                batch_name=input("Enter the batch name")
                batch_lst.append(batch_name)
            print(batch_lst)
            record=[dept_id,dept_name,batch_lst]
            fobj.writerow(record)
            ch=int(input("1->Enter More\n2->exit\nEnter your choice:"))
            if ch==2:
                break;

##Show all batches in a department:
def batch_dept_lst():
    df=pd.read_csv('Department.csv')
    a=pd.DataFrame(df)
    entry=input("Enter the dept id")
    for i,j in a.iterrows():
        if entry==j["Department ID"]:
        print(j["List of batches"])
 #View Performance
def viewPerformanceD(department_id):
    with open("Department.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    batches = []
    for i in range(1, len(csv_reader)):
        if(csv_reader[i][0] == department_id):
            check = 1
            batches = csv_reader[i][2].split(":")
            break
    if(check == 0):
        print("Department ID does not exist")
        return
    if(len(batches) == 0):
        print("No batches in department")
        return
    performances = []
    for batch in batches:
        students = []
        student_performances = []
        with open("Batch.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        for i in range(0, len(csv_reader)):
            if(csv_reader[i][0] == batch):
                students = csv_reader[i][4].split(":")
                break
        for student in students:
            with open("Course.csv", "r", newline = "\n") as f:
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
            if(divs != 0):
                student_performances.append(total_marks/divs)
            else:
                student_performances.append(0)
        total_marks = 0
        divs = 0
        for x in student_performances:
            total_marks += x
            divs += 1
        if(divs != 0):
            performances.append(total_marks/divs)
        else:
            performances.append(0)
    total_marks = 0
    divs = 0
    for i in range(0, len(batches)):
        total_marks += performances[i]
        divs += 1
    avg_percentage = 0
    if(divs != 0):
        avg_percentage = total_marks/divs
    print("Average percantage obtained by all batches in " + department_id + ": " + str(avg_percentage))
#View graph
def linePlot(department_id):
    with open("Department.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    batches = []
    for i in range(1, len(csv_reader)):
        if(csv_reader[i][0] == department_id):
            check = 1
            batches = csv_reader[i][2].split(":")
            break
    if(check == 0):
        print("Department ID does not exist")
        return
    if(len(batches) == 0):
        print("No batches in department")
        return
    performances = []
    for batch in batches:
        students = []
        student_performances = []
        with open("Batch.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        for i in range(0, len(csv_reader)):
            if(csv_reader[i][0] == batch):
                students = csv_reader[i][4].split(":")
                break
        for student in students:
            with open("Course.csv", "r", newline = "\n") as f:
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
            if(divs != 0):
                student_performances.append(total_marks/divs)
            else:
                student_performances.append(0)
        total_marks = 0
        divs = 0
        for x in student_performances:
            total_marks += x
            divs += 1
        if(divs != 0):
            performances.append(total_marks/divs)
        else:
            performances.append(0)
    pyplot.plot(batches, performances)
    pyplot.show()
