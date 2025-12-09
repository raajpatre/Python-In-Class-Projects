key=[]
with open("key.txt",'r') as f:
    data=f.readlines()
    for line in data:
        word=line.split()
    key.extend(word)
students=[]
with open("students.txt",'r') as f:
    data=f.readlines()
    for line in data:
        word=line.split()
        students.append(word)
for i in range(len(students)):
    students[i][1]=students[i][1].split(',')

score=[]
for student in students:
    answers = student[1]
    ct=0
    for i in range(len(answers)):
        if answers[i]==key[i]:
            ct+=1
    score.append(ct)
for i in range(len(students)):
    print(students[i][0],str(score[i])+'/5')
   
