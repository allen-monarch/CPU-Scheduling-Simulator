# CPU Scheduling Simulator

A Python-based desktop application developed as a university project to simulate CPU scheduling algorithms and demonstrate fundamental Operating Systems concepts.

The simulator provides a graphical user interface, scheduling performance metrics, and Gantt chart visualization to help users understand how different scheduling strategies affect process execution.

## Implemented Algorithms

The following five CPU scheduling algorithms are implemented:

1. **FCFS (First Come, First Served)**
2. **SJF (Shortest Job First)**
3. **Round Robin (RR)**
4. **SRT (Shortest Remaining Time)**
5. **MLFQ (Multilevel Feedback Queue)**

## Features

* Add processes through the graphical user interface.
* Remove processes from the process table.
* Define process information:

  * Process ID (PID)
  * Arrival Time
  * Burst Time
  * Priority
* Select and run a CPU scheduling algorithm.
* Validate user input.
* Prevent duplicate Process IDs.
* Calculate average waiting time.
* Calculate average turnaround time.
* Generate Gantt charts to visualize process execution.
* Represent CPU idle periods when no process is available for execution.
* Run automated tests for the scheduling algorithms.

## Technologies

* **Python 3**
* **Tkinter** — Graphical User Interface
* **Matplotlib** — Gantt chart visualization
* **Object-Oriented Programming**
* **Pytest** — Automated testing

## Project Structure

```text
CPU Scheduling Simulator/
│
├── algorithms/
│   ├── fcfs.py
│   ├── sjf.py
│   ├── round_robin.py
│   ├── srt.py
│   └── mlfq.py
│
├── gui/
│   ├── main_window.py
│   └── gantt.py
│
├── models/
│   └── process.py
│
├── simulation/
│   └── process_manager.py
│
├── tests/
│   ├── test_fcfs.py
│   ├── test_sjf.py
│   ├── test_round_robin.py
│   ├── test_srt.py
│   └── test_mlfq.py
│
├── utils/
│   ├── calculations.py
│   ├── display.py
│   └── gantt.py
│
├── main.py
├── simulator.py
├── requirements.txt
└── README.md
```

## Requirements

* Python 3
* Tkinter
* Matplotlib
* Other Python dependencies listed in `requirements.txt`

Tkinter is included with many standard Python installations. On some Linux systems, it may need to be installed separately.

## Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/allen-monarch/CPU-Scheduling-Simulator.git
cd CPU-Scheduling-Simulator
```

Alternatively, download the repository as a ZIP file and extract it.

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

The graphical interface allows you to add processes, choose a scheduling algorithm, run the simulation, and view the results.

### 4. Run the Tests

To run the automated tests, install pytest if it is not already available:

```bash
python -m pip install pytest
```

Then execute:

```bash
python -m pytest
```

## Process Input

Each process is defined by the following parameters:

| Parameter        | Description                                          |
| ---------------- | ---------------------------------------------------- |
| **PID**          | A unique identifier for the process                  |
| **Arrival Time** | The time when the process enters the system          |
| **Burst Time**   | The total CPU execution time required by the process |
| **Priority**     | The priority value assigned to the process           |

## Performance Metrics

The simulator calculates scheduling metrics to help compare algorithm performance.

### Waiting Time

The total time a process spends waiting in the ready queue before receiving CPU time.

### Turnaround Time

The total time between a process's arrival and its completion.

**Turnaround Time = Completion Time − Arrival Time**

### Average Metrics

The simulator displays the average waiting time and average turnaround time for the selected scheduling algorithm.

## Gantt Chart

After a scheduling algorithm is executed, the simulator generates a Gantt chart showing the execution order and timing of processes.

Example:

```text
|  P1  |  P2  |  P3  |  P1  |
0      2      4      6      8
```

This is an illustrative example of a Gantt chart. Actual execution order and timing depend on the selected scheduling algorithm and process inputs.

CPU idle periods are also considered when no process is available for execution.

## Example Processes

The following example illustrates the process information used in the simulator.

| PID | Arrival Time | Burst Time | Priority |
| --- | -----------: | ---------: | -------: |
| P1  |            0 |          5 |        2 |
| P2  |            1 |          3 |        1 |
| P3  |            2 |          8 |        3 |
| P4  |            4 |          2 |        2 |

Different scheduling algorithms may produce different execution orders and performance metrics for the same set of processes.

## Project Goal

The goal of this project is to provide a practical simulation of CPU scheduling algorithms and demonstrate how different scheduling strategies affect process waiting time, turnaround time, and CPU execution order.

The project is intended to support learning about operating systems through implementation, visualization, and experimentation.

## Academic Purpose and Usage

This project was developed primarily for a university assignment and educational presentation.

**You are free to use, copy, share, publish, and modify this project.** You may adapt the source code, experiment with the algorithms, and extend the application with your own ideas and improvements.

If you redistribute a modified version, please indicate that changes have been made.

This statement describes the intended usage of the project. No separate formal open-source license has been added to this repository.

## AI Assistance

AI tools were used to assist with parts of the development process. The project was assembled, reviewed, and tested as part of its development.

## Author

**GitHub:** [allen-monarch](https://github.com/allen-monarch)

**Repository:** [CPU Scheduling Simulator](https://github.com/allen-monarch/CPU-Scheduling-Simulator)
