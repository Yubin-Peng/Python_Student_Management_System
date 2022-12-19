#package for csv
import csv

#the path for the csv file

class students():
    
    #entering the first data csv tile
    def __init__(self):
        self.dataPath = r"F:\py\student_data\student_data.csv"
        title = ["id","name","gender","year","class"]
        students = [
        ["00001","Michael Jordan","male","1999","001"],
        ["00002","Kobe Bryant","male","1995","003"],
        ["00003","Lionel Messi","male","1998","001"],
        ["00004","Michael Jackson","male","1997","002"],
        ["00005","Cristiano Ronaldo","male","1999","003"],

    ]

        with open(self.dataPath,"w+",newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow(title)
            writer.writerows(students)
    
    def studentManage(self):
        while True:
            print("============Student Information System============")
            print("1-Add       2-Update     3-Remove      4-List      5-Exit")
            print("==================================================")
            choice = int(input("Please enter your option: "))
            
            #adding a new student, without duplicate id
            if choice == 1:
                
                
                newId = input("Please enter a new student ID: ")
                flag = False
                with open(self.dataPath,"r",newline="\n") as f:
                    data = csv.reader(f)
                    for i in data:
                        if(i[0]==newId):
                            flag = True
                            print("============Student Information System============")
                            print("A duplicated student ID was entered! Please try again.")
                            print("==================================================") 
                            break

                if flag == False:
                    newName = input("Please enter a new student name: ")
                    newGender = input("Please enter a new student gender: ")
                    newYear = input("Please enter a new student birth year: ")
                    newClass = input("Please enter a new student class: ")
                    newStudent = [newId,newName,newGender,newYear,newClass]
                    with open(self.dataPath,"a",newline="\n") as f:
                        csv.writer(f).writerow(newStudent)
                    print("The student was entered!") 
                    print("==================================================")

            #updating a student by the id
            elif choice == 2:
                print("============Student Information System============")
                newId = input("Please enter the student ID to update: ")
                temp = []

                #open file, read them into a list
                with open(self.dataPath,"r",newline="\n") as f:
                    data = csv.reader(f)
                    for i in data:
                        temp.append(i)
                
                #find the index of the student to update
                newIndex = -1
                index = -1
                for i in temp:
                    newIndex += 1
                    if i[0] == newId:
                        index = newIndex
                        break
                
                if index != -1:
                    newName = input("Please enter a new student name: ")
                    newGender = input("Please enter a new student gender: ")
                    newYear = input("Please enter a new student birth year: ")
                    newClass = input("Please enter a new student class: ")
                    newStudent = [newId,newName,newGender,newYear,newClass]
                    temp[index] = newStudent
                    with open(self.dataPath,"w",newline="\n") as f:
                        csv.writer(f).writerows(temp)
                    print("The student was updated!")   
                    print("==================================================") 
                else:
                    print("The student ID was not found! Please try again.")
                    print("==================================================") 

            #removing a student by the id
            elif choice == 3:
                print("============Student Information System============")
                newId = input("Please enter the student ID to remove: ")
                temp = []
                with open(self.dataPath,"r",newline="\n") as f:
                    data = csv.reader(f)
                    for i in data:
                        temp.append(i)
                
                newIndex = -1
                index = -1
                for i in temp:
                    newIndex += 1
                    if i[0] == newId:
                        index = newIndex
                        break
                
                if index != -1:
                    temp.pop(index)
                    with open(self.dataPath,"w",newline="\n") as f:
                        csv.writer(f).writerows(temp)
                    print("The student was removed!")  
                    print("==================================================") 
                else:
                    print("The student ID was not found! Please try again.")
                    print("==================================================") 
            
            #listing all students
            elif choice == 4:
                print("============Student Information System============")
                with open(self.dataPath,"r",newline="\n") as f:
                    data = csv.reader(f)
                    for i in data:
                        print(i)
                print("==================================================")  

            #exiting the system
            elif choice == 5:
                print("============Student Information System============")
                print("Goodbye, thank you for using Student Information System!")
                print("==================================================")
                raise SystemExit()

            else:
                print("============Student Information System============")
                print("Not an option! Please enter an option from 1-5.")
                print("==================================================")
            
if __name__=="__main__":
    test=students()
    test.studentManage()
