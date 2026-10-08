# mission 13.1 MLFQ => Multi-Level Feedback Queue
# 13.1 → ساخت Queueها  ✅
# 13.2 → ورود Process به Queue 0  ✅
# 13.3 → اجرای Queue 0        ✅
# 13.4 → انتقال به Queue 1    ✅
# 13.5 → انتقال به Queue 2    ✅
# 13.6 → مدیریت Processهای جدید   ✅  Actual process arrival based on arrival time
# 13.7 → تست کامل MLFQ      ✅

from collections import deque    # تابع


def create_queues():
    queue_0 = deque()
    queue_1 = deque()
    queue_2 = deque()

    return queue_0, queue_1, queue_2

# --------------------------------------------

def add_process_to_queue_0(queue_0, process):
    queue_0.append(process)

# --------------------------------------------

def run_queue_0(queue_0, queue_1, current_time, quantum=2):
    schedule = []

    while queue_0:

        process = queue_0.popleft()

        execution_time = min(quantum,process.remaining_time)

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

        if process.remaining_time > 0:
            queue_1.append(process)

    return schedule, current_time


# --------------------------------------------

def run_queue_1(queue_1, queue_2, current_time, quantum=4):
    schedule = []

    while queue_1:

        process = queue_1.popleft()

        execution_time = min(quantum,process.remaining_time)

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

        if process.remaining_time > 0:
            queue_2.append(process)

    return schedule, current_time


# --------------------------------------------

def run_queue_2(queue_2, current_time):
    schedule = []

    while queue_2:

        process = queue_2.popleft()

        start_time = current_time

        current_time += process.remaining_time
        process.remaining_time = 0

        schedule.append(
            {
                "pid": process.pid,
                "start": start_time,
                "end": current_time,
            }
        )

    return schedule, current_time


# --------------------------------------------

def add_arriving_processes(processes, process_index, current_time, queue_0):
    while (
        process_index < len(processes)
        and processes[process_index].arrival_time <= current_time
    ):
        
        queue_0.append(processes[process_index])
        process_index += 1

    return process_index

# --------------------------------------------

def mlfq(processes, quantum_0=2, quantum_1=4):
    processes = sorted(processes,key=lambda process: process.arrival_time)

    queue_0, queue_1, queue_2 = create_queues()

    current_time = 0
    process_index = 0
    completed = 0

    schedule = []

    while completed < len(processes):

        process_index = add_arriving_processes(processes, process_index, current_time, queue_0)

        if not queue_0 and not queue_1 and not queue_2:

            current_time = processes[process_index].arrival_time

            continue

        if queue_0:

            process = queue_0.popleft()

            execution_time = min(quantum_0,process.remaining_time)

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

            process_index = add_arriving_processes(processes, process_index, current_time, queue_0)

            if process.remaining_time > 0:
                queue_1.append(process)
            else:
                completed += 1


        elif queue_1:

            process = queue_1.popleft()

            execution_time = min(quantum_1,process.remaining_time)

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

            process_index = add_arriving_processes(processes, process_index, current_time, queue_0)

            if process.remaining_time > 0:
                queue_2.append(process)
            else:
                completed += 1


        else:

            process = queue_2.popleft()

            start_time = current_time

            current_time += process.remaining_time
            process.remaining_time = 0

            schedule.append(
                {
                    "pid": process.pid,
                    "start": start_time,
                    "end": current_time,
                }
            )

            completed += 1

    return schedule