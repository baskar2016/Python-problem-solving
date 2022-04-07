
s=input("Enter the string : ")
l = s.split()
k = []
for i in l:
 
    
    if (s.count(i)>=1 and (i not in k)):
        k.append(i)
   
j=' '.join(k)
print("The distinct words are :",j)

