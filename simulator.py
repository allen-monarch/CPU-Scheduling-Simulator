from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.round_robin import round_robin
from algorithms.srt import srt
from algorithms.mlfq import mlfq
from copy import deepcopy

# mission 14 

from utils.calculations import (calculate_metrics, calculate_averages)

def run_simulation(processes):
    results = {}

    fcfs_schedule = fcfs(deepcopy(processes))

    fcfs_metrics = calculate_metrics(
        processes,
        fcfs_schedule
    )

    fcfs_average = calculate_averages(
        fcfs_metrics
    )

    results["FCFS"] = {
        "schedule": fcfs_schedule,
        "metrics": fcfs_metrics,
        "average_waiting": fcfs_average[0],
        "average_turnaround": fcfs_average[1],
    }
#-------------------------------------------------------

    sjf_schedule = sjf(deepcopy(processes))

    sjf_metrics = calculate_metrics(
        processes,
        sjf_schedule
    )

    sjf_average = calculate_averages(
        sjf_metrics
    )

    results["SJF"] = {
        "schedule": sjf_schedule,
        "metrics": sjf_metrics,
        "average_waiting": sjf_average[0],
        "average_turnaround": sjf_average[1],
    }
#-------------------------------------------------------

    rr_schedule = round_robin(deepcopy(processes),quantum=2)

    rr_metrics = calculate_metrics(
        processes,
        rr_schedule
    )

    rr_average = calculate_averages(
        rr_metrics
    )

    results["Round Robin"] = {
        "schedule": rr_schedule,
        "metrics": rr_metrics,
        "average_waiting": rr_average[0],
        "average_turnaround": rr_average[1],
    }

#-------------------------------------------------------
    srt_schedule = srt(deepcopy(processes))

    srt_metrics = calculate_metrics(
        processes,
        srt_schedule
    )

    srt_average = calculate_averages(
        srt_metrics
    )

    results["SRT"] = {
        "schedule": srt_schedule,
        "metrics": srt_metrics,
        "average_waiting": srt_average[0],
        "average_turnaround": srt_average[1],
    }

#-------------------------------------------------------
    mlfq_schedule = mlfq(deepcopy(processes),quantum_0=2,quantum_1=4)

    mlfq_metrics = calculate_metrics(
        processes,
        mlfq_schedule
    )

    mlfq_average = calculate_averages(
        mlfq_metrics
    )

    results["MLFQ"] = {
        "schedule": mlfq_schedule,
        "metrics": mlfq_metrics,
        "average_waiting": mlfq_average[0],
        "average_turnaround": mlfq_average[1],
    }

    return results

#16.6.1
# اگر اسم اشتباه وارد بشه خطا میگیریم 

def get_algorithm_result(results, algorithm):
    if algorithm not in results:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    return results[algorithm]