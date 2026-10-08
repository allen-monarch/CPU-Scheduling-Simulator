# pip install matplotlib
# mission 6 => Gantt chart for FCFS
import matplotlib.pyplot as plt


def draw_gantt_chart(schedule):
    fig, ax = plt.subplots(figsize=(10, 2))

    for item in schedule:
        start = item["start"]
        end = item["end"]
        pid = item["pid"]

        ax.barh(0, end - start, left=start, height=0.5)

        ax.text((start + end) / 2, 0, pid, ha="center", va="center")

    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title("FCFS - Gantt Chart")

    ax.set_xlim(0, schedule[-1]["end"])

    plt.show()