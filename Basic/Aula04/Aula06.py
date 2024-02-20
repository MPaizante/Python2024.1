
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

x = scores.split()
b= []
for a in x:
    b.append(int(a))
print(b)
a_scores=[]

for i in b:
    if i >= 90:
        a_scores.append(i)
        
a_scores = len(a_scores)
print(a_scores)