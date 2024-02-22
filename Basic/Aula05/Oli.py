olympios =[("Jhon", 31 , "Cross"), ("Mina", 30 ,"Sailing")
    ,("Valdemar", 54, "Art"), ("Makoka",18,"Cycling")]


outfile = open("Oli.csv","w")
outfile.write("Name,Age,Sport")
outfile.write("\n")

for olympio in olympios:
    row ="{},{},{}".format(olympio[0],olympio[1],olympio[2])
    outfile.write(row)
    outfile.write("\n")
outfile.close()