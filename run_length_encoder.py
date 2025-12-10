s=input()
ct=1
newar=[]
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        newar.append(str(ct)+s[i])
        ct=1
    else:
        ct+=1
newar.append(str(ct)+s[i])
print("".join(newar))