import random;


prob = random.random()
print(int(prob*100))

diceThrow = random.randrange(1,100)
print(diceThrow)

subtotal = input("Enter total before tax:")
tax = float(subtotal) * 0.8
tax = int(tax)
print("tax on", subtotal, "is:", tax)
