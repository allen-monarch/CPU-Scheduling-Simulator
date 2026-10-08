# mission 11 => Shortest Remaining Time

def srt(processes):
    processes = processes.copy()

    current_time = 0
    completed = 0
    schedule = []

    while completed < len(processes):

        available_processes = [process for process in processes if process.arrival_time <= current_time
            and process.remaining_time > 0]


        if not available_processes:
            current_time += 1
            continue

        selected_process = min(available_processes, key=lambda process: process.remaining_time)


        start_time = current_time


        current_time += 1        # مهم
        selected_process.remaining_time -= 1

        end_time = current_time
        # مرتب نگه داشتن  Gantt Chart
        if (
            schedule
            and schedule[-1]["pid"] == selected_process.pid
            and schedule[-1]["end"] == start_time
        ):
            
            schedule[-1]["end"] = end_time
        
        else:
            schedule.append(
                {
                    "pid": selected_process.pid,
                    "start": start_time,
                    "end": end_time,
                }
            )


        if selected_process.remaining_time == 0:
            completed += 1


    return schedule