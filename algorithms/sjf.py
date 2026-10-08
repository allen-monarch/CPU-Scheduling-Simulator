# mission 7 => Shortest Job First
#Among the processes that have arrived and are ready for execution, the process with the shortest burst time is selected.
# CPU Time >  Which processes have been entered? >  Which of them has less burst? > Execute that same thing.
# > Carry it out to the end  > Check again.


def sjf(processes):
    processes = processes.copy()

    current_time = 0
    schedule = []
    completed = []

    while len(completed) < len(processes):

        available_processes = [process for process in processes if process.arrival_time <= current_time and process not in completed]

        if not available_processes:
            current_time = min(process.arrival_time for process in processes if process not in completed)
            continue


        selected_process = min(available_processes, key=lambda process: process.burst_time)


        start_time = current_time
        end_time = start_time + selected_process.burst_time

        schedule.append(
            {
                "pid": selected_process.pid,
                "start": start_time,
                "end": end_time,
            }
        )

        current_time = end_time
        completed.append(selected_process)


    return schedule