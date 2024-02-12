sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

x = sentence.split()
same_letter_count = []
for s in x:
    if s[0] == s[-1]:
        same_letter_count.append(s)

same_letter_count = len(same_letter_count)
print(same_letter_count)