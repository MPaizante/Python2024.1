letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse=True)
print(sorted_letters)

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)


medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals.keys())
print(alphabetical)

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
y = sorted(medals.keys(), key= lambda x : medals[x], reverse=True)
top_three = []
i = 0
while i < 3:
    top_three.append(y[i])
    i +=1
print(top_three)