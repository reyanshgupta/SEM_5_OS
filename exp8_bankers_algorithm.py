p = int(input("Enter the number of processes: "))
r = int(input("Enter the number of resources: "))

# Max resources needed by each process
max = []
print("Enter the maximum resources needed by each process:")
for i in range(p):
    resources = list(map(int, input().split()))
    max.append(resources)

# Allocated resources to each process
alloc = []
print("Enter the allocated resources to each process:")
for i in range(p):
    resources = list(map(int, input().split()))
    alloc.append(resources)

available = list(map(int, input("Enter the available resources: ").split()))

proc_complete = [0] * p
answer = [0] * p
index = 0

for i in range(p):
    proc_complete[i] = 0
    #to keep track of completed processes

need = [[0] * r for i in range(p)] #need matrix
for i in range(p):
    for j in range(r):
        need[i][j] = max[i][j] - alloc[i][j] #calculating need matrix

for x in range(p):
    for i in range(p):
        if proc_complete[i] == 0: #processes haven't completed
            flag = 0 #flag to check if need is less than available
            for j in range(r):
                if need[i][j] > available[j]:
                    flag = 1 #can't be allocated
                    break
            if flag == 0:
                answer[index] = i #add to safe sequence
                index += 1
                for k in range(r):
                    available[k] += alloc[i][k] #add allocated to available when the process is completed
                proc_complete[i] = 1 #process completed

if index < p:
    print("No safe sequence found. The sequence is unsafe.")
else:
    print("Safe Sequence: ")
    for i in range(p - 1):
        print("P", answer[i], "->", end=" ")
    print("P", answer[p - 1])
