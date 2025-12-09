# Raw string input

data = """Date,Desc,Amount

2023-01-01,Salary,5000

2023-01-02,Rent,-1200

2023-01-03,Groceries,-150

2023-01-04,Freelance,300"""


rows = data.split('\n')

# Hint: rows[0] is the header, start loop from rows[1]
row=list(data.split())
newarr=[]
for i in range(len(row)):
    newarr.append(row[i].split(','))
print(f"{newarr[0][0]}\t\t{newarr[0][1]}\t{newarr[0][2]}")
for i in range(1,len(newarr)):
    for j in range(len(newarr[i])):
        print(newarr[i][j],end="\t")
    print()
print()
tot=0
ern=0
lar=0

for i in range(1,len(newarr)):
    if int(newarr[i][2])>0:
        ern+=int(newarr[i][2])
    else:
        tot+=int(newarr[i][2])
    if int(newarr[i][2])>lar:
        lar=int(newarr[i][2])
        ind=i
print(f"Total spent {tot*(-1)} ₹")
print()
print(f"Total earned {ern} ₹")
print()
print(f"Spent largest on {newarr[i][1]}")
print()
print()