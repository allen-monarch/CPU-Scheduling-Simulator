# mission 15.1 Summary

def print_algorithm_summary(algorithm, data):
    print("=" * 50)
    print(algorithm)
    print("=" * 50)

    print("Average Waiting Time:",
          data["average_waiting"])

    print("Average Turnaround Time:",
          data["average_turnaround"])

    print()

# mission 15.2 Comparison Table

def print_comparison_table(results):
    print()
    print("CPU SCHEDULING RESULTS")
    print()

    print(
        f"{'Algorithm':<18}"
        f"{'Avg Waiting':<15}"
        f"{'Avg Turnaround':<15}"
    )

    print("-" * 48)

    for algorithm, data in results.items():
        print(
            f"{algorithm:<18}"
            f"{data['average_waiting']:<15.2f}"
            f"{data['average_turnaround']:<15.2f}"
        )

    print()


# mission 15.3  Schedule Display 

def print_schedule(algorithm, schedule):
    print()
    print(f"{algorithm} SCHEDULE")
    print()

    print(
        f"{'PID':<10}"
        f"{'Start':<10}"
        f"{'End':<10}"
    )

    print("-" * 30)


    for item in schedule:
        print(
            f"{item['pid']:<10}"
            f"{item['start']:<10}"
            f"{item['end']:<10}"
        )

    print()

# mission 15.4   Gantt Data


def prepare_gantt_data(schedule):
    gantt_data = []

    for item in schedule:
        duration = item["end"] - item["start"]

        gantt_data.append(
            {
                "pid": item["pid"],
                "start": item["start"],
                "duration": duration,
            }
        )

    return gantt_data