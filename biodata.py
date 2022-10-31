name=str(input("enter your name:-"))

age=int(input("enter your age:-"))

fname=str(input("enter your fathers name:-"))

mname=str(input ("enter your mothers name:-"))

thislist=[str(input("enter your address:-").upper().strip())]

pno=int(input("enter your phone number:-"))

sname=str(input("enter your school name:-"))

iname=str(input("enter your intermediate college name:-"))

dname=str(input("enter your degree college name:-"))

cname=str(input("enter your course:-"))

a=str(input("enter your hobbies:-"))

print("         BIODATA")

print("NAME                 :",name[0:21].strip().upper())

print("AGE                  :",age)

print("PHONE NUMBER         :",pno)

print("ADDRESS              :",thislist)

print("MOTHER'S NAME        :",mname.strip().upper())

print("FATHER'S NAME        :",fname.strip().upper())

print("SCHOOL               :",sname.strip().upper())

print("INTERMEDIATE COLLEGE :",iname.strip().upper())

print("DEGREE COLLEGE       :",dname.strip().upper())

print("COURSE               :",cname.strip().upper())

print("HOBBIES              :",a.strip().upper())
