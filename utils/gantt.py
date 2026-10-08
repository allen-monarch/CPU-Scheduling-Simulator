# misson 16
import matplotlib.pyplot as plt


def draw_gantt_chart(gantt_data, title="Gantt Chart"):
    fig, ax = plt.subplots(figsize=(12, 4))

    for item in gantt_data:

        start = item["start"]
        duration = item["duration"]
        pid = item["pid"]

        ax.barh(0, duration, left=start, height=0.5)

        ax.text( start + duration / 2,0,pid,ha="center",va="center")

        ax.axvline(start,linewidth=0.8)

    if gantt_data:
        last_end = (gantt_data[-1]["start"] + gantt_data[-1]["duration"])

        ax.axvline(last_end,linewidth=0.8)

        ax.text(last_end, -0.38, str(last_end), ha="center")
        

    ax.set_title(title)

    ax.set_xlabel("Time")

    ax.set_ylabel("CPU")

    ax.set_yticks([0])

    ax.set_yticklabels(["CPU"])

    ax.set_xlim(0,
        max(item["start"] + item["duration"]for item in gantt_data)
    )

    ax.set_ylim(-0.7, 0.7)

    ax.grid(axis="x")

    plt.tight_layout()

    plt.show()

#-------------------------------------------------------------------

def draw_algorithm_gantt(results, algorithm):
    schedule = results[algorithm]["schedule"]

    gantt_data = []

    for item in schedule:
        gantt_data.append(
            {
                "pid": item["pid"],
                "start": item["start"],
                "duration": item["end"] - item["start"],
            }
        )

    draw_gantt_chart(gantt_data, title=f"{algorithm} - Gantt Chart")

#-------------------------------------------------------------------

def show_algorithm_gantt(results, algorithm):
    if algorithm not in results:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    schedule = results[algorithm]["schedule"]

    gantt_data = []

    for item in schedule:
        gantt_data.append(
            {
                "pid": item["pid"],
                "start": item["start"],
                "duration": item["end"] - item["start"],
            }
        )


    draw_gantt_chart(gantt_data, title=f"{algorithm} - Gantt Chart")