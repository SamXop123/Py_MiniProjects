import threading
import time

# Shared variables
flag = [False, False]
turn = 0

def process_0():
    global turn
    for i in range(3):
        # Entry section
        flag[0] = True
        while flag[1]:
            if turn != 0:
                flag[0] = False
                while turn != 0:
                    pass  # busy wait
                flag[0] = True

        # ---- Critical Section ----
        print("Process 0: Entering critical section")
        time.sleep(1)
        print("Process 0: Leaving critical section")
        # --------------------------

        # Exit section
        turn = 1
        flag[0] = False

        # Remainder section
        time.sleep(0.5)

def process_1():
    global turn
    for i in range(3):
        # Entry section
        flag[1] = True
        while flag[0]:
            if turn != 1:
                flag[1] = False
                while turn != 1:
                    pass  # busy wait
                flag[1] = True

        # ---- Critical Section ----
        print("Process 1: Entering critical section")
        time.sleep(1)
        print("Process 1: Leaving critical section")
        # --------------------------

        # Exit section
        turn = 0
        flag[1] = False

        # Remainder section
        time.sleep(0.5)

# Create two threads simulating two processes
t1 = threading.Thread(target=process_0)
t2 = threading.Thread(target=process_1)

# Start both threads
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()