# Student Record System Using Arrays and Strings
names = []
marks = []

for i in range(3):
    names.append(input("Enter name: "))
    marks.append(int(input("Enter marks: ")))

for i in range(3):
    print(names[i], marks[i])