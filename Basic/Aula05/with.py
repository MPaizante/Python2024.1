fname = 'square.txt'
with open(fname, "r") as md:
    for line in md:
        print(line)
md.close()
