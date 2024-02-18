origlist = [45,32,88]
aliaslist = origlist
origlist += ["cat"]
origlist = origlist + ["cow"]

print(origlist is aliaslist)
print(origlist, aliaslist)

