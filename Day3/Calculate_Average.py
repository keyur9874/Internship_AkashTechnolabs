# Calculate Average Of five Number
n = list(map(int,input("Enter Five number").split()))
sum = 0
for i in n:
    sum = sum + i
print("Average Of Five Number : ", sum / 5)