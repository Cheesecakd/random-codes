Range = 5
Count = 0
for i in range(Range):
    for j in range(i + 1):
        print(j+1,end = " ")
        Count = j
    for k in range(Range - i):
        print(Range - Count - k, end=" ")
    print("")
