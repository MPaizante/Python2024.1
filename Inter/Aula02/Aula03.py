l = ['2','3','4',5]
lt = map(lambda y: float(y)*2,l)
print(list(lt))

def par(x):
    list = [float(num )for num in x if num % 2 ==0]
    return list
print(par([1,2,3,4,5,6,7,8,9]))




L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)
lst2 = [num for num in L if num >10]

print(lst2)

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
x =tester['info']
compri =[d['class standing'] for d in x]



print(compri)
