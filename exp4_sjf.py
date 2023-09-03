def calculateWaitingTime(processes, n, waiting_time):
    remaining_time = [0] * n
    for i in range(n):
        remaining_time[i] = processes[i][1]
    completed = 0
    current_time = 0
    min_remaining_time = float('inf')
    shortest_process = 0
    found_shortest = False

    while (completed != n):
        for j in range(n):
            if (processes[j][2] <= current_time) and (remaining_time[j] < min_remaining_time) and remaining_time[j] > 0:
                min_remaining_time = remaining_time[j]
                shortest_process = j
                found_shortest = True
        if not found_shortest:
            current_time += 1
            continue

        remaining_time[shortest_process] -= 1
        min_remaining_time = remaining_time[shortest_process]
        if min_remaining_time == 0:
            min_remaining_time = float('inf')

        if remaining_time[shortest_process] == 0:
            completed += 1
            found_shortest = False
            finish_time = current_time + 1
            waiting_time[shortest_process] = (finish_time - processes[shortest_process][1] - processes[shortest_process][2])

            if waiting_time[shortest_process] < 0:
                waiting_time[shortest_process] = 0

        current_time += 1

def calculateTurnAroundTime(processes, n, waiting_time, turnaround_time):
    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

def calculateAverageTimes(processes, n):
    waiting_time = [0] * n
    turnaround_time = [0] * n

    calculateWaitingTime(processes, n, waiting_time)
    calculateTurnAroundTime(processes, n, waiting_time, turnaround_time)

    print("Processes Burst Time     Waiting",
          "Time     Turn-Around Time")
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

if __name__ == "__main__":
    processes_info = [[0, 4, 2], [4, 5, 1],
                      [3, 5, 2], [7, 4, 3]]
    num_processes = 4
    calculateAverageTimes(processes_info, num_processes)
