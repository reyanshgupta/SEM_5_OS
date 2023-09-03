#taking inputs and storing them
n = int(input("Enter number of tasks: "))
arrival_time = []
burst_time = []
for i in range(n):
    print("Enter arrival time for Task ", i+1, ": ")
    artime = int(input())
    arrival_time.append(artime)
    print("Enter burst time for Task ", i+1, ": ")
    bursttime = int(input())
    burst_time.append(bursttime)

wait_time = [0] * n
turnaround_time = [0] * n
completion_time = [0]*n
total_waittime = 0
total_turnaroundtime = 0

# Sort tasks based on arrival time
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if arrival_time[j] > arrival_time[j + 1]:
            arrival_time[j], arrival_time[j + 1] = arrival_time[j + 1], arrival_time[j]
            burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]
            
#completion time calculation          
for i in range(n):
    if completion_time[i-1]<arrival_time[i]:
        completion_time[i] = arrival_time[i]+burst_time[i]
    else:
        completion_time[i] = completion_time[i-1]+burst_time[i]
        
#turnaroundtime calc
for i in range(n):
    turnaround_time[i]=completion_time[i] - arrival_time[i]
total_turnaroundtime = sum(turnaround_time)
#wait time calc
for i in range(n):
    wait_time[i] = turnaround_time[i] - burst_time[i]
total_waittime = sum(wait_time)
#printing outputs
print("Task   Arrival Time   Burst Time   Completion Time   Wait Time   Turnaround Time")
for i in range(n):
    print(i + 1,"\t\t",arrival_time[i],"\t\t",burst_time[i],"\t\t",completion_time[i],"\t\t",wait_time[i],"\t\t",turnaround_time[i])


avg_waittime = round(total_waittime / n, 2)
avg_turnaroundtime = round(total_turnaroundtime / n, 2)

print("Average Wait Time: ", avg_waittime)
print("Average Turnaround Time: ", avg_turnaroundtime)
print("Total Wait Time: ", total_waittime)
print("Total Turnaround Time: ", total_turnaroundtime)
