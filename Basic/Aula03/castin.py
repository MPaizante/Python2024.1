items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0

for i in items:
    for x in i:
        if x == "w":
            acc_num += 1
            break

print(acc_num)