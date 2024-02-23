inventory = { 'bananas': 312, 'pears': 217, 'apples': 430,'oranges': 525}
for akey in sorted(inventory.keys()):
    print(f'Key: {akey} , Value: {inventory[akey]} ')

for x,y in inventory.items():
    print(f'Tenho {x} com valor de {y}')

total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
for akey in mydict:
   if len(akey) > 3:
      total = total + mydict[akey]
print(total)