# mission 3 => FCFS Implementation   First Come, First Served
# Whichever process enters the ready queue earlier gets the CPU earlier.


def fcfs(processes):
    sorted_processes = sorted(processes,key=lambda process: process.arrival_time)     # sort the processes based on: arrival_time 

    current_time = 0
    schedule = []

    for process in sorted_processes:

        if current_time < process.arrival_time:
            current_time = process.arrival_time

        start_time = current_time                          # It is the process start time.
        end_time = start_time + process.burst_time        # It is the process completion time.

        schedule.append(
            {
                "pid": process.pid,
                "start": start_time,
                "end": end_time,
            }
        )

        current_time = end_time

    return schedule