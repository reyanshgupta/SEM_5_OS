def calculateWaitingTime(processes, n, waiting_time):
    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1]

def calculateTurnAroundTime(processes, n, waiting_time, turnaround_time):
    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

def calculateAverageTimes(processes, n):
    waiting_time = [0] * n
    turnaround_time = [0] * n
    calculateWaitingTime(processes, n, waiting_time)
    calculateTurnAroundTime(processes, n, waiting_time, turnaround_time)
    
    print("\nProcesses Burst Time Waiting",
          "Time Turn-Around Time")
    total_waiting_time = 0
    total_turnaround_time = 0
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
        print(" ", processes[i][0], "\t\t",
              processes[i][1], "\t\t",
              waiting_time[i], "\t\t", turnaround_time[i])

    print("\nAverage waiting time = %.5f " % (total_waiting_time / n))
    print("Average turn around time =", total_turnaround_time / n)


def priorityScheduling(processes, n):
    processes = sorted(processes, key=lambda proc: proc[2], reverse=True)

    print("Order in which processes get executed:")
    for i in processes:
        print(i[0], end=" ")
    calculateAverageTimes(processes, n)

if __name__ == "__main__":
    processes_info = [[1, 3, 1],
                      [2, 5, 0],
                      [3, 8, 1]]
    num_processes = 3
    priorityScheduling(processes_info, num_processes)