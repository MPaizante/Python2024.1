print(len("Hello"))

print(2*len("Hello")+len("goodbye"))

n = input("Please enter you name: ")
print("Your name is: "+ str(n))


str_seconds = input("Please enter the number of seconds you wish to convert: ")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still = total_secs % 3600
minutes = secs_still //60
secs_finally = secs_still %60
print("Hrs:", hours , "mins:",minutes,"secs:", secs_finally)