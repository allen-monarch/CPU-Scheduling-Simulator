from models.process import Process

# mission 2 => Creating processes and simulating entry
# mission 12 => Process Manager



def create_processes(process_data=None):
    if process_data is None:
        return [
            Process("P1", 0, 5, 2),
            Process("P2", 1, 3, 1),
            Process("P3", 2, 8, 3),
            Process("P4", 4, 2, 2),
        ]

    processes = []

    for data in process_data:
        process = Process(
            data["pid"],
            data["arrival_time"],
            data["burst_time"],
            data.get("priority", 0)
        )

        processes.append(process)

    return processes