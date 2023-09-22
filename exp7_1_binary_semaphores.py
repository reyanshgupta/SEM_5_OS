a = 10
semaphore = 1
wait_queue = []

def process1():
    global a
    wait()
    a += 10
    print("for P1, A is: ", a)
    signal()
                                                                            
def process2():
    global a
    wait()
    a -= 10
    print("for P2, A is: ", a)
    signal()

def wait():
    global semaphore
    if semaphore == 1:
        semaphore = 0
    else:
        wait_queue.append(1)

def signal():
    global semaphore, wait_queue
    if not wait_queue:
        semaphore = 1
    else:
        process_to_wake = wait_queue.pop(0)
        if process_to_wake == 1:
            process1()
        else:
            process2()

process1()
process2()
process2()
process1()