student={}
n=int(input('Enter the number of students:'))
for i in range(1,n+1):
    key=input('Enter the name of the student:')
    value=int(input('Enter the marks of the student:'))
    student[key]=value
name=input('Enter a name for which you want to find the marks:')
if name in student:
    print('The marks of {} is:'.format(name),student[name])
else:
    print('Name not found')