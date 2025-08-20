#writing content to the file
user=input('Enter the data to be written:')
file=open('data.txt','w')
writing=file.write(user)
#print(writing)
file.close()

#appending the same file
add=input('Enter the data to be appended to the same file:')
file=open('data.txt','a')
adding=file.write(add)
#print(adding)
file.close()

#reading the same file
file=open('data.txt','r')
reading=file.readline()
print('the final content of the file is:\n')
print(reading)
file.close()
