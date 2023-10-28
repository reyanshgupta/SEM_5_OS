import numpy as np
def bestFit(segments,process_size):
    for i in range(len(process_size)):
        best_fit_index = -1  # Initialize to an invalid index
        best_fit_gap = float('inf')  # Initialize to positive infinity

        for j in range(len(segments)):
            if segments[j][0] == 0 and segments[j][1] >= process_size[i]:
                gap = segments[j][1] - process_size[i]

                if gap < best_fit_gap:
                    best_fit_gap = gap
                    best_fit_index = j

        if best_fit_index != -1:
            segments[best_fit_index][0] = 1
            process_size[i] = best_fit_index + 1  # Mark the process as allocated to segment best_fit_index
            print(f"Process {i + 1} allocated to memory block {best_fit_index + 1}")
        else: 
            print(f"Process {i+1} couldn't be allocated to any memory block.")
            
def worstFit(segments,process_size):
    biggest_segment_index = -1
    for i in range(len(process_size)):
        worst_fit_size = -1
        for j in range(len(segments)):
            if segments[j][0] == 0 and segments[j][1] >= process_size[i]:
                if worst_fit_size == -1 or segments[j][1] > segments[biggest_segment_index][1]:
                    biggest_segment_index = j
                    worst_fit_size = segments[j][1]

        if biggest_segment_index != -1:
            segments[biggest_segment_index][0] = 1
            process_size[i] = biggest_segment_index + 1  # Mark the process as allocated to the segment
            print(f"Process {i + 1} allocated to memory block {biggest_segment_index + 1}")
        else: 
            print(f"Process {i+1} couldn't be allocated to any memory block.")

def firstFit(segments, process_size):
    for i in range(len(process_size)):
        for j in range(len(segments)):
            if segments[j][0] == 0 and segments[j][1] >= process_size[i]:
                segments[j][0] = 1
                process_size[i] = j + 1  # Mark the process as allocated to segment j
                print(f"Process {i + 1} allocated to memory block {j + 1}")
                break
                           
segments = np.array([[0, 256], [0, 512], [0, 256], [0, 512], [0, 256], [0, 128]]) # Used or not flag with size of segments
# process_size = np.zeros(len(segments), dtype=int) # Allocated or not flag with size of processes
process_size = np.array([412,231,312, 241, 501,111])

# for i in range(len(segments)):
#     print(f"Enter process {i + 1} size: ")
#     process_size[i] = int(input())

print("Enter your choice for memory allocation: \n1. Best Fit\n2. Worst Fit\n3. First Fit")
choice = int(input())

if choice == 1:
    bestFit(segments,process_size)
    
if choice == 2:
    worstFit(segments,process_size)

if choice == 3:
    firstFit(segments, process_size)
