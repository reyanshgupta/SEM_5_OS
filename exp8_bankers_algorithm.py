p = 5  # Number of processes
r = 3  # Number of resources

# Max resources needed by each process
max = [[7, 5, 3],
       [3, 2, 2],
       [9, 0, 2],
       [2, 2, 2],
       [4, 3, 3]]

# Allocated resources to each process
alloc = [[1, 4, 2],
         [2, 0, 3],
         [3, 2, 2],
         [2, 1, 1],
         [1, 1, 2]]

available = [1, 3, 2]

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
        if proc_complete[i] == 0: #processes hasn't completed
            flag = 0 #flag to check if need is less than available
            for j in range(r):
                if need[i][j] > available[j]:
                    flag = 1 #cant be allocated
                    break
            if flag == 0:
                answer[index] = i #add to safe sequence
                index += 1
                for k in range(r):
                    available[k] += alloc[i][k] #add allocated to available when process is completed
                proc_complete[i] = 1 #process completed

print("Safe Sequence: ")
for i in range(p - 1):
    print("P", answer[i], "->", end=" ")
print("P", answer[p - 1])
