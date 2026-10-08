# CPU Scheduling Simulator

A Python-based CPU Scheduling Simulator developed as a university project.

This project simulates five CPU scheduling algorithms and provides scheduling results, performance metrics, and Gantt charts.

## Implemented Algorithms

The following CPU scheduling algorithms are implemented:

1. FCFS (First Come, First Served)
2. SJF (Shortest Job First)
3. Round Robin
4. SRT (Shortest Remaining Time)
5. MLFQ (Multilevel Feedback Queue)

## Features

- Add processes through the graphical user interface
- Remove processes from the process table
- Define:
  - Process ID (PID)
  - Arrival Time
  - Burst Time
  - Priority
- Select a CPU scheduling algorithm
- Simulate process scheduling
- Calculate Average Waiting Time
- Calculate Average Turnaround Time
- Generate Gantt Charts
- Handle CPU idle periods
- Validate user input
- Prevent duplicate Process IDs

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
├── utils/
│   ├── calculations.py
│   ├── display.py
│   └── gantt.py
│
├── simulator.py
├── main.py
├── requirements.txt
└── README.md


• Requirements
• Python 3.x
• Tkinter
• Matplotlib

Python dependencies can be installed using:  pip install -r requirements.txt


> How to Run :
        Clone or download the project and navigate to the project directory:


> Install the required dependencies:
                pip install -r requirements.txt


> Run the application:
            python main.py


>>> Process Input :  
• Each process contains the following information:

PID	          >  Unique Process ID
Arrival Time  >	 Time when the process enters the system
Burst Time	  >  CPU time required by the process
Priority	  >  Process priority




• Performance Metrics
    The simulator calculates:

• Waiting Time
    The amount of time a process spends waiting in the ready queue before receiving CPU time.

• Turnaround Time
    The total time from the arrival of a process until its completion.  (Turnaround Time = Completion Time - Arrival Time)

 
• Gantt Chart
After running a scheduling algorithm, the simulator generates a Gantt Chart showing the execution order and timing of processes.  

>>> Example: 
| P1 | P2 | P3 | P1 |
0    2    4    6    8
CPU idle periods are also considered when no process is available for execution.


>>> Example Processes : 
PID    Arrival Time    Burst Time    Priority
P1          0               5            2
P2          1               3            1
P3          2               8            3
P4          4               2            2


Project Goal = > The goal of this project is to provide a practical simulation of CPU scheduling algorithms and demonstrate how different scheduling strategies affect process waiting time, turnaround time, and CPU execution order.


• Technologies •
Python
Tkinter
Matplotlib
Object-Oriented Programming


•• Academic Project
This project was developed for educational purposes as a CPU Scheduling simulation project.



