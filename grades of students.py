#PROGRAM TO FIND GRADE OF STUDENTS
Marks=int(input("Enter the marks:"))
PercentageScore=Marks/1000*100  
if(PercentageScore>=90):
    print("Student has got A")
elif(PercentageScore>=80 and PercentageScore<90):
    print("Student has got B")
elif(PercentageScore>=70 and PercentageScore<80):
    print ("Student has got C")
else :
    print("Student has got D")
print("Perecntage of student",PercentageScore)
