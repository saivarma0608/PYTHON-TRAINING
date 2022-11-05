name=str(input("ENTER YOUR NAME:-"))

B=int(input("ENTER YOUR AGE:-"))

C=str(input("ENTER YOUR FATHER'S NAME:-"))

D=str(input("ENTER YOUR MOTHERS NAME:-"))

E=[str(input("ENTER YOUR ADDRESS:-").upper().strip())]

F=int(input("ENTER YOUR PHONE NUMBER:-"))

G=str(input("ENTER YOUR HOBBIES:-"))

for i in range(0,1):
    print((name,B,C,D,E,F,[G]))

    
print("ENTER YOUR EDUCATION DETAILS")

a=(input("ENTER YOUR SCHOOL NAME:").upper().strip())

b=(input("ENTER YOUR INTERMEDIATE COLLEGE  NAME:").upper().strip())

c=(input("ENTER YOUR DEGREE COLLEGE NAME:").upper().strip())

d=int(input("ENTER YEAR OF PASSING:"))

e=(input("ENTER YOUR DEGREE PERCENTAGE:").upper().strip())
for i in range(0,1):
    print((a,b,c,d,e))
    
print('ENTER YOUR TECHNICAL SKILLS')

z=(input("ENTER THE CODING LANGUAGE SKILLS:").upper().strip())
x=(input("ENTER THE STANDARD OF YOUR COMMUNICATION SKILL('good','average','excellent'):").upper().strip())
for i in range(0,1):
    print([z],[x])

print("ENTER YOUR EXTRA CIRCULAR ACTIVITIES")

G=(input("ENTER YOUR EXTRA CIRCULAR ACTIVITIES:").upper().strip())

for i in range(0,1):
    print([G])


