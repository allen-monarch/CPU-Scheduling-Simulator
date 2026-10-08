# mission 4 => Calculating Waiting Time and Turnaround Time

# def calculate_metrics(processes, schedule):
#     results = []

#     for process in processes:
#         item = next(
#             item for item in schedule
#             if item["pid"] == process.pid
#         )

#         completion_time = item["end"]
#         turnaround_time = completion_time - process.arrival_time    # When the process execution finishes.
#         waiting_time = turnaround_time - process.burst_time

#         results.append(
#             {
#                 "pid": process.pid,
#                 "waiting_time": waiting_time,
#                 "turnaround_time": turnaround_time,
#             }
#         )

#     return results
#-------------------------------------------------------------------------------
# mission 10 => Calculating Round-Robin Metrics

def calculate_metrics(processes, schedule):
    results = []

    for process in processes:
        process_schedule = [item for item in schedule if item["pid"] == process.pid]

        completion_time = process_schedule[-1]["end"]

        turnaround_time = completion_time - process.arrival_time
        waiting_time = turnaround_time - process.burst_time

        results.append(
            {
                "pid": process.pid,
                "waiting_time": waiting_time,
                "turnaround_time": turnaround_time,
            }
        )

    return results


def calculate_averages(results):
    total_waiting_time = sum(result["waiting_time"] for result in results)

    total_turnaround_time = sum(result["turnaround_time"] for result in results)

    number_of_processes = len(results)

    average_waiting_time = total_waiting_time / number_of_processes
    average_turnaround_time = total_turnaround_time / number_of_processes

    return average_waiting_time, average_turnaround_time


#---------------------------------------------------------------------------------

# mission 5 =>  Calculating averages

def calculate_averages(results):
    total_waiting_time = sum(result["waiting_time"] for result in results)

    total_turnaround_time = sum(result["turnaround_time"] for result in results)

    number_of_processes = len(results)

    average_waiting_time = total_waiting_time / number_of_processes
    average_turnaround_time = total_turnaround_time / number_of_processes

    return average_waiting_time, average_turnaround_time