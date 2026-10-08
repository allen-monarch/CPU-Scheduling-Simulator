# Process work
# mission 1 =>  PID , 
# Arrival Time =>  When the process enters the system/ready queue.
# Burst Time => The time required for a process to fully utilize the CPU.


class Process:                            
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time   # mission 9


    def __repr__(self):
        return (
            f"Process("
            f"pid='{self.pid}', "
            f"arrival={self.arrival_time}, "
            f"burst={self.burst_time}, "
            f"priority={self.priority}"
            f")"
        )