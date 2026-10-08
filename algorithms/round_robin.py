# mission 9 => What is Round Robin? In Round Robin, each process is allowed to use the CPU for only one time quantum.
from collections import deque


def round_robin(processes, quantum):
    processes = sorted(processes, key=lambda process: process.arrival_time)

    queue = deque()
    schedule = []

    current_time = 0
    process_index = 0
    completed = 0

    while completed < len(processes):

        while (
            process_index < len(processes)
            and processes[process_index].arrival_time <= current_time
        ):
            
            queue.append(processes[process_index])
            process_index += 1

        if not queue:
            current_time = processes[process_index].arrival_time
            continue

        process = queue.popleft()

        execution_time = min(quantum , process.remaining_time)

        start_time = current_time
        current_time += execution_time
        process.remaining_time -= execution_time

        schedule.append(
            {
                "pid": process.pid,
                "start": start_time,
                "end": current_time,
            }
        )

        while (
            process_index < len(processes)
            and processes[process_index].arrival_time <= current_time
        ):
            
            queue.append(processes[process_index])
            process_index += 1


        if process.remaining_time > 0:
            queue.append(process)
        else:
            completed += 1


    return schedule