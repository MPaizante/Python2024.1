sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

x = sentence.split()

num_a_or_e = 0

for s in x:
    for a in s:
        if a =="a" or a =="e":
            num_a_or_e +=1
            break

print(num_a_or_e)